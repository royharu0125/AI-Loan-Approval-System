# 🏦 AI Loan Approval System (Financial Services)

[繁體中文](#繁體中文) | [English](#english)

---

## English
### 📌 Project Overview
In financial services, manual loan approval is a major bottleneck due to inconsistent documentation. This project implements a robust machine learning system designed to handle these "sensitive" and "noisy" real-world cases.

### 🛠️ Core Skills & Technical Highlights
* **Data Pre-processing**: Handled missing values and performed feature engineering to ensure data quality.
* **Gradient Boosting (XGBoost)**: Utilized sequential iterative learning to outperform parallel models like Random Forest, especially when dealing with inconsistent income or missing values
* **80/10/10 Split Strategy**: Adopted a rigorous three-way split (Train/Validation/Test) to perform a second validation and mitigate overfitting before final production deployment.
* **Production Readiness**: Decoupled the workflow into modular scripts (`preprocess.py` and `train.py`) to demonstrate deployment-ready software engineering skills.

### 📊 Results & Critical Thinking
* **Accuracy**: 76% (Baseline)
* **Analysis**: The model shows high recall for approvals. Future iterations will focus on bias detection and hyperparameter tuning to refine decision boundaries.

---

## 繁體中文
### 📌 專案概述
金融服務業常面臨貸款審核流程不一致的挑戰（如：收入歷史不穩定或文件不齊）。本專案建立了一個穩健的機器學習系統，專門處理現實世界中具有「雜訊」與「敏感性」的案例。

### 🛠️ 核心技能與技術亮點
* **數據預處理**：處理缺失值並進行特徵工程，確保進入模型前的數據品質。
* **梯度提升算法 (XGBoost)**：採用循序迭代學習 (Sequential Learning)，在處理不一致的文件或缺失值時，表現優於隨機森林等並行模型。
* **80/10/10 數據拆分**：執行嚴謹的訓練、驗證與測試拆分，透過二次驗證有效防止過擬合，確保模型在真實環境的穩定性。
* **生產環境意識**：將流程解耦為模組化腳本（preprocess.py 與 train.py），展示具備實務部署能力的軟體工程思維。

### 📊 實驗分析與批判性思考
* **準確度**: 76% (基準模型)
* **深度分析**: 目前模型對核准類別具備高召回率。未來計畫引入 AI Agent 進行偏見偵測，並透過超參數調優進一步提升決策精準度。
* **生產環境意識**：將流程解耦為模組化腳本（`preprocess.py` 與 `train.py`），展示具備實務部署能力的軟體工程思維。