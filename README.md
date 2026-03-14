# Financial Services Loan Approval System

[English](#english) | [繁體中文](#繁體中文)

---

## English

### Overview
This project addresses a common challenge in the financial sector: the automated screening of loan applications characterized by inconsistent documentation or complex income histories. Unlike basic classification projects, this system focuses on the reliability and interpretability required for sensitive financial decisions

### Project Structure
- `preprocess.py`: Handles raw data ingestion, missing value imputation, and label encoding.
- `train.py`: Implements the model training pipeline using XGBoost and rigorous validation.
- `data/`: Contains raw training and testing datasets.
- `models/`: Stores serialized model objects for deployment.

### Technical Decisions

#### 1. Choice of Algorithm: Gradient Boosting (XGBoost)
The decision to use XGBoost over parallel models like Random Forest was based on its sequential iterative learning approach. In financial datasets where noise (missing values or outliers) is common, Gradient Boosting's ability to minimize error through consecutive tree improvements provides a more robust decision boundary

#### 2. Validation Strategy (80/10/10 Split)
To mitigate overfitting and ensure the model generalizes to unseen real-world applications, I implemented a three-way split:
- **80% Training**: For model learning.
- **10% Validation**: For parameter tuning and second-round validation.
- **10% Test**: For unbiased final evaluation

This approach simulates a production-ready environment where the model is scored against data it has never encountered during experimentation.

### Performance Analysis
The current baseline model achieves an accuracy of 76%. While the recall for approved cases is high (1.00), the model is currently less effective at identifying rejection cases (Recall: 0.38). 

#### Challenges & Future Work
- **Data Imbalance**: The discrepancy in recall suggests the need for synthetic over-sampling (SMOTE) or adjusted class weights in future iterations.
- **Feature Engineering**: Further work is needed to create compound features such as debt-to-income ratios to improve classification precision.

---

## 繁體中文

### 專案概述
本專案針對金融產業常見的挑戰：如何自動化篩選具有不穩定收入紀錄或複雜文件的貸款申請案 。不同於基礎的分類專案，本系統專注於處理金融決策所需的可靠性與可解釋性 。

### 專案結構
- `preprocess.py`: 負責原始數據導入、缺失值填補與標籤編碼 。
- `train.py`: 實作基於 XGBoost 的模型訓練流程與嚴謹驗證 。
- `data/`: 存放訓練與測試用的原始數據。
- `models/`: 儲存訓練完成的模型檔案以便後續部署。

### 技術決策

#### 1. 演算法選擇：梯度提升 (XGBoost)
選擇 XGBoost 而非隨機森林（Random Forest）等並行模型，是基於其循序迭代學習的特性 。在常見雜訊（缺失值或異常值）的金融數據集中，梯度提升透過連續改進決策樹來極小化誤差的能力，能提供更穩健的決策邊界 。

#### 2. 驗證策略 (80/10/10 拆分)
為了防止過擬合並確保模型能泛化至現實世界的應用，我採用了三階段拆分 ：
- **80% 訓練集**: 用於模型學習 。
- **10% 驗證集**: 用於參數調優與二次驗證 。
- **10% 測試集**: 用於最終的無偏誤評估 。

這種方法模擬了生產級環境 (Production-ready)，在模型正式評分前，確保其面對未曾接觸過的數據仍具備穩定性 。

### 實驗分析
目前基準模型的準確度為 76%。雖然模型對於「核准」類別具備極高的召回率 (1.00)，但對於「拒絕」類別的識別效果尚待加強 (Recall: 0.38)。

#### 挑戰與未來計畫
- **數據不平衡**: 召回率的差異顯示未來需要引入過採樣技術 (SMOTE) 或調整類別權重。
- **進階特徵工程**: 計畫開發複合特徵（如債務收入比），以進一步提升分類精確度 。