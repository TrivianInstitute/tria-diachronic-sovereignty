from __future__ import annotations

import sys
from pathlib import Path

REFERENCE_ROOT = Path(__file__).resolve().parents[1] / "11-reference-implementation"
if str(REFERENCE_ROOT) not in sys.path:
    sys.path.insert(0, str(REFERENCE_ROOT))
