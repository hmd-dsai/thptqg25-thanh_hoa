# ---------------------------------------------------------------------------
# PREREQUISITES
# ---------------------------------------------------------------------------
# This script depends on the output of `raw_xlsx_to_csv.py`
#
# Please run `scripts/raw_xlsx_to_csv.py` first to generate:
#   data/raw/raw.csv
# ---------------------------------------------------------------------------

from pathlib import Path
import numpy as np
import pandas as pd

# Ensure code runs regardless of CWD
ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"

# Read raw CSV dataset
path = DATA / "raw" / "raw.csv"
raw_data = pd.read_csv(path, dtype={"SOBAODANH": str})

# Standardize column names
raw_data = raw_data.rename(columns={
    "SOBAODANH": "SBD",
    "Toán": "TOAN",
    "Văn": "VAN",
    "Lí": "LI",
    "Hóa": "HOA",
    "Sinh": "SINH",
    "Tin học": "TIN",
    "Công nghệ công nghiệp": "CNCN",
    "Công nghệ nông nghiệp": "CNNN",
    "Sử": "SU",
    "Địa": "DIA",
    "Giáo dục kinh tế và pháp luật": "KTPL",
    "Ngoại ngữ": "NN",
    "Mã môn ngoại ngữ": "MA_NN"
})

# Pivot language columns into separate score columns
raw_data["MA_NN"] = raw_data["MA_NN"].map({
    "N1": "T_ANH",
    "N2": "T_NGA",
    "N3": "T_PHAP",
    "N4": "T_TRUNG",
    "N5": "T_DUC",
    "N6": "T_NHAT",
    "N7": "T_HAN"
})
lang_score = raw_data.pivot(columns="MA_NN", values="NN")
lang_score = lang_score.drop(columns=[np.nan], errors="ignore")
raw_data = pd.concat([raw_data.drop(columns=["MA_NN", "NN"]), lang_score], axis=1)

# Add province code column
raw_data.insert(2, "MA_TINH", raw_data["SBD"].str[:2])

# Return preprocessed CSV file
out_path = DATA / "raw" / "preprocessed.csv"
raw_data.to_csv(out_path, index=False)