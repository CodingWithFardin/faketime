import unittest
from datetime import datetime, timezone

from faketime import Clock


class ClockTest(unittest.TestCase):
    def test_frozen(self):
        c = Clock(datetime(2026, 1, 1, tzinfo=timezone.utc))
        self.assertEqual(c.now(), c.now())

    def test_advance(self):
        c = Clock(datetime(2026, 1, 1, tzinfo=timezone.utc))
        c.advance(60)
        self.assertEqual((c.now() - c._start).total_seconds(), 60.0)

    def test_step(self):
        c = Clock(datetime(2026, 1, 1, tzinfo=timezone.utc), step=5)
        c.now()
        self.assertEqual((c.now() - c._start).total_seconds(), 10.0)


if __name__ == "__main__":
    unittest.main()
