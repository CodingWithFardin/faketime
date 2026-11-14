# faketime

Deterministic clock for tests: freeze, advance, snapshot.

```
python -c "from faketime import Clock;print(Clock().now())"
```

## layout

- `tests/test_faketime.py` - tests for the module next to it

## use

Runs on 3.11 and newer.

```
git clone https://github.com/CodingWithFardin/faketime.git
cd faketime
```

Tests: `tests/test_faketime.py`. The suite is the specification; start there if the code is unclear.

MIT, 2026.
