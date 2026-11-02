#!/usr/bin/env python3
"""Shim: the checker moved to scripts/validate-core-order.py (DDD-dec-80). Removed after v0.5.0."""
import runpy, sys
from pathlib import Path
sys.argv[0] = str(Path(__file__).resolve().parent / "scripts" / "validate-core-order.py")
runpy.run_path(sys.argv[0], run_name="__main__")
