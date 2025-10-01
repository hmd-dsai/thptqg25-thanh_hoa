# Analysis of THPTQG 2025 score data in Thanh Hoa

A mini DS project, exploring Vietnam's National High School Exam 2025 (THPTQG 2025) results of Thanh Hoa province. This is the prequel to my upcoming project, which will utilize score data of the whole country.

## Objectives
- Conduct Exploratory Data Analysis (EDA) on raw data.
- Generate a normalized (quantile transformed) version of the dataset (which I refer to as an "ideal"), and compare to the raw dataset.
- [Upcoming] Create a ML model that can predict scores of subjects that a student didn't take, and predict his/her admission outcome using real cut-off scores of some university programs.

## Interactive Notebook
- `notebooks/eda.ipynb`: [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/hmd-dsai/thptqg25-thanh_hoa/blob/main/notebooks/eda.ipynb)
- `notebooks/ideal_comparision.ipynb`: [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/hmd-dsai/thptqg25-thanh_hoa/blob/main/notebooks/ideal_comparison.ipynb)

## Dataset Source
The dataset was publicly provided in [this article](https://baochinhphu.vn/8h-sang-16-7-tra-cuu-diem-thi-tot-nghiep-thpt-nam-2025-tren-cong-thong-tin-dien-tu-chinh-phu-102250715114537341.htm). Refer to `scripts/raw_xlsx_to_csv.py` for details on how to install the dataset onto this project.

## What I Practiced in this Project
- Exploratory Data Analysis (EDA) with pandas, matplotlib, and seaborn
- Data normalization using quantile transformer from scikit-learn
- Interpreting results from the viewpoint of an education policy counselor

## Acknowledgement
This project is incomplete and is only intended as a prequel to my upcoming larger project. Even so, I welcome constructive feedback to help me improve further and make adjustments in my next projects.