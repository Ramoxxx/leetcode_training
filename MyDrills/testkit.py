"""
Tiny test helper used by every exercise file.

Usage at the bottom of an exercise file:

    from testkit import check, report

    check("empty input", my_func([]), [])
    check("basic case", my_func([1, 2, 2]), [2])
    report()

Run the file directly:  python warmup/contains_duplicate.py
"""

import math


_PASSED = 0
_FAILED = 0


def _equal(got, expected):
    """Check types too: True must not pass a test expecting the integer 1."""
    if type(got) is not type(expected):
        return False
    if isinstance(expected, float):
        return math.isclose(got, expected, rel_tol=1e-9, abs_tol=1e-9)
    if isinstance(expected, (list, tuple)):
        return len(got) == len(expected) and all(
            _equal(a, b) for a, b in zip(got, expected)
        )
    return got == expected


def check(name, got, expected):
    """Compare values and types; allow small floating-point rounding errors."""
    global _PASSED, _FAILED
    if _equal(got, expected):
        _PASSED += 1
        print(f"  PASS  {name}")
    else:
        _FAILED += 1
        print(f"  FAIL  {name}")
        print(f"        expected: {expected!r}")
        print(f"        got:      {got!r}")


def report():
    """Print a summary line. Call once at the end of a file."""
    total = _PASSED + _FAILED
    print("-" * 40)
    if total == 0:
        print("No tests ran: exercise failed.")
    elif _FAILED == 0:
        print(f"All {total} tests passed.")
    else:
        print(f"{_PASSED}/{total} passed, {_FAILED} failed.")
    print()
    raise SystemExit(1 if _FAILED or total == 0 else 0)
