import { initWasm, Resvg } from 'https://cdn.jsdelivr.net/npm/@resvg/resvg-wasm@2.6.2/index.mjs';

const canvas=document.getElementById('canvas'), status=document.getElementById('status');
const message=document.getElementById('message'), progress=document.getElementById('progress');
let runtime, game, context, master, audioPaused=false, audioUnlocked=false;
const buffers=new Map(), voices=new Map();
let startedVoices=0, decodedVoices=0, decodedNonzero=false;

window.rasterSVG = svg => {
  const renderer=new Resvg(svg,{font:{loadSystemFonts:false}});
  try {
    const image=renderer.render();
    try{return Uint8Array.from(image.asPng());}finally{image.free();}
  } finally {renderer.free();}
};
window.browserAudio = {
  play(id,key,encoded,volume,pan,loops) {
    this.stop(id);
    const voice={active:true};voices.set(id,voice);
    if(!buffers.has(key)) {
      const raw=atob(encoded), data=new Uint8Array(raw.length);
      for(let i=0;i<raw.length;i++)data[i]=raw.charCodeAt(i);
      buffers.set(key,context.decodeAudioData(data.buffer).catch(error=>{buffers.delete(key);throw error;}));
    }
    buffers.get(key).then(buffer=>{
      if(voices.get(id)!==voice || !voice.active)return;
      decodedVoices++;decodedNonzero ||= buffer.getChannelData(0).some(x=>Math.abs(x)>.0001);
      const source=context.createBufferSource(), gain=context.createGain();
      const stereo=context.createStereoPanner ? context.createStereoPanner() : null;
      source.buffer=buffer;source.loop=loops>1;gain.gain.value=volume;
      source.connect(gain);if(stereo){stereo.pan.value=pan;gain.connect(stereo);stereo.connect(master);}else gain.connect(master);
      voice.source=source;voice.gain=gain;voice.stereo=stereo;
      source.onended=()=>{voice.active=false;};source.start();startedVoices++;
      if(loops>1)source.stop(context.currentTime+buffer.duration*loops);
    }).catch(error=>{console.error('Audio decode:',error);voice.active=false;});
  },
  stop(id){const voice=voices.get(id);if(voice){voice.active=false;if(voice.source){try{voice.source.stop();}catch{}}voices.delete(id);}},
  active(id){return !!voices.get(id)?.active;},
  diagnostics(){return {context:context?.state, decoded:decodedVoices, started:startedVoices, nonzero:decodedNonzero, active:[...voices.values()].filter(v=>v.active).length};},
  volume(id,volume,pan){const v=voices.get(id);if(v?.gain)v.gain.gain.value=volume;if(v?.stereo)v.stereo.pan.value=pan;},
  mute(value){master.gain.value=value?0:1;},
  pause(value){audioPaused=!!value;if(value)context.suspend();else context.resume();}
};

function resumeAudio() {
  if(context && !audioPaused && context.state!=='running')context.resume().catch(()=>{});
}
function unlockAudio() {
  if(!context || audioPaused)return;
  if(!audioUnlocked) {
    const unlock=context.createBufferSource();unlock.buffer=context.createBuffer(1,1,context.sampleRate);
    unlock.connect(master);unlock.start();audioUnlocked=true;
  }
  resumeAudio();
}
function eventPoint(event) {
  const r=canvas.getBoundingClientRect();
  return [(event.clientX-r.left)*canvas.width/r.width,(event.clientY-r.top)*canvas.height/r.height];
}
function bindInputs() {
  let pointer=null;
  canvas.addEventListener('pointerdown',e=>{unlockAudio();if(pointer!==null)return;pointer=e.pointerId;canvas.setPointerCapture(pointer);const [x,y]=eventPoint(e);game.pointer_down(x,y);e.preventDefault();});
  canvas.addEventListener('pointermove',e=>{if(pointer!==null&&pointer!==e.pointerId)return;const [x,y]=eventPoint(e);game.pointer_move(x,y);e.preventDefault();});
  const up=e=>{if(pointer!==e.pointerId)return;const [x,y]=eventPoint(e);game.pointer_up(x,y);pointer=null;e.preventDefault();};
  canvas.addEventListener('pointerup',up);canvas.addEventListener('pointercancel',up);
  canvas.addEventListener('wheel',e=>{const [x,y]=eventPoint(e);game.pointer_wheel(x,y,-e.deltaY/60);e.preventDefault();},{passive:false});
  window.addEventListener('keydown',e=>{unlockAudio();game.key_down(e.key);});
  document.addEventListener('visibilitychange',()=>{if(!document.hidden)resumeAudio();});
}

async function downloadAssets() {
  const response=await fetch('dist/game.zip');
  if(!response.ok)throw Error('Game assets unavailable');
  const declared=Number(response.headers.get('Content-Length'));
  const total=Number.isSafeInteger(declared)&&declared>0&&declared<512000000?declared:0;
  const reader=response.body?.getReader();
  if(!reader)return new Uint8Array(await response.arrayBuffer());
  const chunks=[];let received=0,bytes=total?new Uint8Array(total):null;
  if(total>0){progress.max=total;progress.value=0;}
  while(true) {
    const {done,value}=await reader.read();if(done)break;
    const offset=received;received+=value.length;
    if(bytes){
      if(received>bytes.length){const larger=new Uint8Array(Math.max(received,bytes.length*2));larger.set(bytes);bytes=larger;}
      bytes.set(value,offset);
    } else chunks.push(value);
    if(total>0){progress.value=received;message.textContent=`Downloading game assets… ${Math.round(Math.min(received/total,1)*100)}%`;}
    else message.textContent=`Downloading game assets… ${(received/1000000).toFixed(1)} MB`;
  }
  if(bytes)return bytes.subarray(0,received);
  bytes=new Uint8Array(received);let offset=0;
  for(const chunk of chunks){bytes.set(chunk,offset);offset+=chunk.length;}
  return bytes;
}

window.gameReady=()=>{status.hidden=true;};
async function load() {
  try {
    await initWasm(fetch('https://cdn.jsdelivr.net/npm/@resvg/resvg-wasm@2.6.2/index_bg.wasm'));
    runtime=await loadPyodide({indexURL:'https://cdn.jsdelivr.net/pyodide/v314.0.7/full/'});
    runtime._api._skip_unwind_fatal_error=true;
    runtime.canvas.setCanvas2D(canvas);
    message.textContent='Loading Python, graphics and game assets…';
    let [assets]=await Promise.all([downloadAssets().then(data=>{
      progress.removeAttribute('value');message.textContent='Preparing the game…';return data;
    }),runtime.loadPackage(['pygame-ce','pillow'])]);
    progress.removeAttribute('value');message.textContent='Preparing the game…';
    runtime.FS.mkdir('/app');runtime.FS.chdir('/app');
    runtime.unpackArchive(assets,'zip',{extractDir:'/app'});assets=null;
    const entry=await fetch('browser_game.py');if(!entry.ok)throw Error('Browser adapter unavailable');
    runtime.FS.writeFile('/app/browser_game.py',await entry.text());
    await runtime.runPythonAsync("import sys; sys.path.insert(0, '/app'); import browser_game");
    game=runtime.globals.get('browser_game');window.gameRuntime=runtime;
    const Audio=window.AudioContext||window.webkitAudioContext;
    if(!Audio)throw Error('Browser audio is unavailable');
    context=new Audio();master=context.createGain();master.connect(context.destination);
    bindInputs();await runtime.runPythonAsync('await browser_game.run()');
  } catch(error) {console.error(error);message.textContent='Loading failed: '+error;progress.hidden=true;status.hidden=false;}
}
load();
