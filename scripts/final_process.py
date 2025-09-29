# ---------------------------------------------------------------------------
# PREREQUISITES
# ---------------------------------------------------------------------------
# This script depends on the output of `preprocess.py`
#
# Please run `scripts/preprocess.py` first to generate:
#   data/raw/preprocessed.csv
# ---------------------------------------------------------------------------

from pathlib import Path
import numpy as np
import pandas as pd

# Ensure code runs regardless of CWD
ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"

# Read preprocessed data
in_path = DATA / "raw" / "preprocessed.csv"
pre = pd.read_csv(in_path, dtype={"SBD": str})

# Extract data with province code = 28 (Thanh Hoa province)
processed = pre[pre["MA_TINH"] == 28]

# Dropping subjects with few students registering
processed = pre.drop(columns=[
    "TIN",
    "CNNN",
    "CNCN",
    "T_DUC",
    "T_HAN",
    "T_NGA",
    "T_NHAT",
    "T_PHAP",
    "T_TRUNG"
])

# Return final processed CSV file
out_path = DATA / "processed" / "thanhhoa_processed.csv"
processed.to_csv(out_path, index=False)