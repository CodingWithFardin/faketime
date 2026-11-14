# faketime - deterministic clock for tests. No dependencies, thread safe.
import threading
import time as _time
from datetime import datetime, timedelta, timezone


class Clock:
    def __init__(self, start=None, step=0.0):
        self._lock = threading.Lock()
        self._start = start or datetime.now(timezone.utc)
        self._offset = 0.0
        self._step = step

    def now(self):
        with self._lock:
            self._offset += self._step
            return self._start + timedelta(seconds=self._offset)

    def timestamp(self):
        return self.now().timestamp()

    def advance(self, seconds):
        with self._lock:
            self._offset += seconds
            return self

    def freeze(self):
        self._step = 0.0
        return self

    def set_step(self, seconds):
        self._step = seconds
        return self

    def reset(self):
        with self._lock:
            self._offset = 0.0
            self._step = 0.0
        return self

    def sleep(self, seconds):
        self.advance(seconds)


class RealClock:
    def now(self):
        return datetime.now(timezone.utc)

    def timestamp(self):
        return _time.time()

    def sleep(self, seconds):
        _time.sleep(seconds)
