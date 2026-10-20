"""
Run every exercise file in warmup/, drill/, and simulation/.

    python run_all.py

Each file runs on its own and prints its own pass/fail lines. Use this
to see at a glance which exercises are still failing.
"""

import argparse
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
FOLDERS = ["warmup", "drill", "simulation"]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--timeout", type=float, default=10,
                        help="maximum seconds per exercise (default: 10)")
    args = parser.parse_args()
    if not 0 < args.timeout < float("inf"):
        parser.error("--timeout must be a finite positive number")
    passed = failed = 0
    for folder in FOLDERS:
        path = os.path.join(HERE, folder)
        if not os.path.isdir(path):
            continue
        files = sorted(f for f in os.listdir(path)
                       if f.endswith(".py") and f != "testkit.py")
        print("=" * 50, flush=True)
        print(folder.upper(), flush=True)
        print("=" * 50, flush=True)
        for f in files:
            print(f"\n[{folder}/{f}]", flush=True)
            try:
                result = subprocess.run(
                    [sys.executable, os.path.join(path, f)], timeout=args.timeout
                )
                success = result.returncode == 0
            except subprocess.TimeoutExpired:
                print(f"  TIMEOUT after {args.timeout:g} seconds", flush=True)
                success = False
            passed += int(success)
            failed += int(not success)
            print("  Exercise: " + ("PASS" if success else "FAIL"), flush=True)
    print(f"\nExercises: {passed} passed, {failed} failed.", flush=True)
    return 1 if failed or passed == 0 else 0


if __name__ == "__main__":
    sys.exit(main())
