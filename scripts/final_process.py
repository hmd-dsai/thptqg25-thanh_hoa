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
pre = pd.read_csv(in_path, dtype={"SBD": str, "MA_TINH": str})

# Extract data with province code = 28 (Thanh Hoa province)
processed = pre[pre["MA_TINH"] == '28']

# Dropping subjects with few students registering
processed = processed.drop(columns=[
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

# Add columns for total scores of common subject combinations (khối thi)
processed["A00"] = processed[["TOAN", "LI", "HOA"]].sum(axis=1, min_count=3)
processed["A01"] = processed[["TOAN", "LI", "T_ANH"]].sum(axis=1, min_count=3)
processed["B00"] = processed[["TOAN", "HOA", "SINH"]].sum(axis=1, min_count=3)
processed["C00"] = processed[["VAN", "SU", "DIA"]].sum(axis=1, min_count=3)
processed["D01"] = processed[["TOAN", "VAN", "T_ANH"]].sum(axis=1, min_count=3)

# Return final processed CSV file
out_path = DATA / "processed" / "thanhhoa_processed.csv"
processed.to_csv(out_path, index=False)