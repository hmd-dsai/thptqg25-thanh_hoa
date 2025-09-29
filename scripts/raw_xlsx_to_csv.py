# ---------------------------------------------------------------------------
# PREREQUISITES:
# ---------------------------------------------------------------------------
# 1. Download the raw XLSX dataset:
#   https://baochinhphu.vn/8h-sang-16-7-tra-cuu-diem-thi-tot-nghiep-thpt-nam-2025-tren-cong-thong-tin-dien-tu-chinh-phu-102250715114537341.htm
#   (Click on "TRA CỨU ĐIỂM THI TỐT NGHIỆP THPT 2025 CHƯƠNG TRÌNH 2018")
#
# 2. Rename the file to:
#   ket_qua_thptqg_2025_ct2018.xlsx
#
# 3. Save the file to: 
#   thptqg25-thanh_hoa/data/raw
# ---------------------------------------------------------------------------

from pathlib import Path
import pandas as pd

# Ensure code runs regardless of CWD
ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"

# Read Excel sheets and merge
in_path = DATA / "raw" / "ket_qua_thptqg_2025_ct2018.xlsx"
sheet1 = pd.read_excel(in_path, sheet_name=0, header=0, dtype={"SOBAODANH": str}) # Ensure leading zeros are not dropped
sheet2 = pd.read_excel(in_path, sheet_name=1, header=0, dtype={"SOBAODANH": str})
merged = pd.concat([sheet1, sheet2], ignore_index=True)

# Return merged CSV file
out_path = DATA / "raw" / "raw.csv"
merged.to_csv(out_path, index=False)