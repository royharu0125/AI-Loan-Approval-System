import pandas as pd
from sklearn.preprocessing import LabelEncoder
import os

def preprocess_data(file_path):
    df = pd.read_csv(file_path)
    
    # 補值邏輯
    cols_to_fill_mode = ['Gender', 'Married', 'Dependents', 'Self_Employed', 'Credit_History', 'Loan_Amount_Term']
    for col in cols_to_fill_mode:
        df[col] = df[col].fillna(df[col].mode()[0])
    df['LoanAmount'] = df['LoanAmount'].fillna(df['LoanAmount'].median())

    # 編碼邏輯
    le = LabelEncoder()
    cols_to_encode = ['Gender', 'Married', 'Education', 'Self_Employed', 'Property_Area', 'Loan_Status', 'Dependents']
    for col in cols_to_encode:
        if col in df.columns:
            df[col] = le.fit_transform(df[col].astype(str))
            
    return df

if __name__ == "__main__":
    # 建立輸出資料夾
    os.makedirs('processed_data', exist_ok=True)
    
    # 處理並儲存
    clean_train = preprocess_data('data/train_u6lujuX_CVtuZ9i.csv')
    clean_train.to_csv('processed_data/clean_train.csv', index=False)
    
    print("數據預處理完成，已儲存至 processed_data/clean_train.csv")