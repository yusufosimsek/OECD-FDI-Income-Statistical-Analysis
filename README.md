📊 OECD FDI Income: Statistical Analysis & Predictive Modeling

Status: 🔄 Work in Progress
Data engineering completed — EDA and modeling in progress.

📌 Project Overview

This repository presents a comprehensive statistical analysis of Foreign Direct Investment (FDI) income flows across OECD member countries, categorized by economic activity (ISIC Rev. 4).

Using the BMD4 (Benchmark Definition of FDI, 4th Edition) framework, the project aims to:

Uncover sectoral and country-level investment patterns
Analyze structural and temporal dynamics of FDI flows
Develop predictive models for investment behavior and data reliability
Identify hidden clusters and investment archetypes
🔗 Data Source
OECD Data Explorer — FDI Income by Industry
Standard: BMD4
📈 Dataset Architecture
Attribute	Specification
Observations	10,344
Variables	24 (18 analytical, 6 excluded)
Countries	38 OECD members
Sectors	18+ (ISIC Rev. 4)
Frequency	Annual
Unit	USD (millions)
🔍 Core Research Questions
Structural Evolution:
Which sectors and countries dominate FDI income flows over time?
Feature Dependency:
What relationships exist between sector, country, and investment types?
Data Reliability:
Can OBS_STATUS be predicted from available features?
Market Segmentation:
What clusters emerge in global investment profiles?
🛠️ Analysis Framework
Phase 1 — Pre-Analysis & Taxonomy ✅
Variable role definition (feature vs target)
Removal of redundant structural variables
Data quality assessment via OBS_STATUS
End-to-end modeling roadmap design
Phase 2 — Data Engineering 🔄
SQL-based preprocessing (filtering, deduplication)
Feature engineering:
Country groupings
Sector aggregations
Time-based features
Missing data handling (statistical imputation)
Phase 3 — Exploratory Data Analysis 🔄
Distribution analysis & normality testing (Shapiro-Wilk, Q-Q)
Statistical testing:
Categorical × Categorical → Chi-square
Categorical × Numerical → ANOVA / Kruskal-Wallis
Numerical × Numerical → Pearson / Spearman
Phase 4 — Modeling & Inference ⏳
Method	Target
Regression	Predict FDI income (OBS_VALUE)
Classification	Predict data reliability (OBS_STATUS)
Clustering	Identify investment profiles
Panel Data	Cross-country & temporal dynamics
📊 Expected Outputs
📈 Statistical insights on global FDI distribution
🤖 Predictive models for income & reliability
🌍 Country/sector clustering results
📊 Interactive Power BI dashboard (planned)
🚀 Getting Started
1. Clone the Repository
git clone https://github.com/yusufosimsek/OECD-FDI-Income-Statistical-Analysis.git
cd OECD-FDI-Income-Statistical-Analysis
2. Install Dependencies
pip install -r requirements.txt
3. Run Notebooks
jupyter notebook
📂 Repository Structure
OECD-FDI-Income-Statistical-Analysis/
│
├── data/
│   └── raw/                # OECD dataset
│
├── reports/                # Analysis reports
│
├── notebooks/              # EDA & modeling (in progress)
│
├── requirements.txt
└── README.md
💻 Tech Stack
Python: Pandas, NumPy, SciPy, Statsmodels, Scikit-learn
SQL: Data preprocessing
Visualization: Matplotlib, Seaborn
BI Tool: Power BI
Environment: Jupyter Notebook
📌 Roadmap
 Complete EDA
 Build regression models
 Implement classification pipeline
 Perform clustering analysis
 Develop Power BI dashboard
 Publish final report
⚡ Key Strengths
Real-world OECD dataset
Multi-method statistical approach
Combination of econometrics + machine learning
Scalable and modular workflow
👤 Author

Yusuf Onur Şimşek

GitHub: https://github.com/yusufosimsek
LinkedIn: https://linkedin.com/in/yusuf-onur-simsek-702241224
📌 Notes

This project is actively evolving. New notebooks, models, and visualizations will be added continuously.
