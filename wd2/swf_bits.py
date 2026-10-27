"""Minimal binary tag framing used by optional source verification tools."""
import struct


class Bits:
    def __init__(self, data, offset=0):
        self.data, self.bit = data, offset*8

    def read(self, n, signed=False):
        v = 0
        for _ in range(n):
            v = (v << 1) | ((self.data[self.bit//8] >> (7-self.bit % 8)) & 1)
            self.bit += 1
        return v-(1 << n) if signed and n and v & (1 << (n-1)) else v

    def align(self):
        self.bit = (self.bit+7)//8*8
        return self.bit//8

    def matrix(self):
        sx = sy = 1.
        r0 = r1 = 0.
        if self.read(1):
            n = self.read(5)
            sx, sy = self.read(n, True)/65536, self.read(n, True)/65536
        if self.read(1):
            n = self.read(5)
            r0, r1 = self.read(n, True)/65536, self.read(n, True)/65536
        n = self.read(5)
        x, y = self.read(n, True)/20, self.read(n, True)/20
        self.align()
        return [sx, r0, r1, sy, x, y]


def records(data, start, end):
    i = 0
    while start+2 <= end:
        offset = start
        header = struct.unpack_from('<H', data, start)[0]
        start += 2
        kind, size = header >> 6, header & 63
        if size == 63:
            size = struct.unpack_from('<I', data, start)[0]
            start += 4
        if start+size > end:
            raise ValueError(f'Truncated tag at {offset}')
        yield i, kind, offset, start, size
        start += size
        i += 1
        if kind == 0:
            break
