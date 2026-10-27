"""Deterministic presentation time, independent of game turns and wall time."""
from fractions import Fraction


class PresentationClock:
    def __init__(self, frame_callback, fps=24):
        self.frame_callback = frame_callback
        self.fps = fps
        self.ticks = 0
        self.paused = False
        self.timers = {}
        self.next_id = 1

    @property
    def milliseconds(self):
        return Fraction(self.ticks * 1000, self.fps)

    def set_interval(self, callback, milliseconds):
        period = Fraction(str(milliseconds))
        if period <= 0:
            raise ValueError('Interval must be positive')
        timer_id = self.next_id
        self.next_id += 1
        self.timers[timer_id] = [self.milliseconds + period, period, callback]
        return timer_id

    def clear_interval(self, timer_id):
        self.timers.pop(timer_id, None)

    def pause(self):
        self.paused = True

    def resume(self):
        self.paused = False

    def step(self, count=1):
        for _ in range(count):
            if self.paused:
                break
            self.ticks += 1
            # Frame callbacks first; timers then run by deadline and creation ID.
            # Only timers existing at this boundary are eligible this tick.
            eligible = set(self.timers)
            self.frame_callback()
            while not self.paused:
                due = [(v[0], key) for key, v in self.timers.items()
                       if key in eligible and v[0] <= self.milliseconds]
                if not due:
                    break
                _, key = min(due)
                timer = self.timers[key]
                timer[0] += timer[1]  # Reschedule before callback, allowing cancellation.
                timer[2]()
