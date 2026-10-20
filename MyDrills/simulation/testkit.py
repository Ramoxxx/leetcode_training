"""Load the shared helper when this exercise folder is run directly."""

from pathlib import Path
import runpy

_helpers = runpy.run_path(str(Path(__file__).resolve().parents[1] / "testkit.py"))
check = _helpers["check"]
report = _helpers["report"]
