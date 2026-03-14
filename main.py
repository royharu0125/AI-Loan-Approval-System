import codecs
import pandas as pd

train_df = pd.read_csv("data/train_u6lujuX_CVtuZ9i.csv")
test_df = pd.read_csv("data/test_Y3wMUE5_7gLdaTN.csv")

print('訓練集前五行資料：')
print(train_df.head())

print('\n-- 各欄位缺失直統計---')
print(train_df.isnull().sum())

cols_to_fill_mode =['Gender','Married','Dependents','Self_Employed','Credit_History','Loan_Amount_Term']
for col in cols_to_fill_mode:
    train_df[col] = train_df[col].fillna(train_df[col].mode()[0])

train_df["LoanAmount"] = train_df["LoanAmount"].fillna(train_df["LoanAmount"].median())

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()

cols_to_encode = ['Gender', 'Married', 'Education', 'Self_Employed', 'Property_Area', 'Loan_Status', 'Dependents']
for col in cols_to_encode:
    train_df[col] = le.fit_transform(train_df[col].astype(str))


print("\n--- 補值與編碼後的缺失值統計 ---")
print(train_df.isnull().sum())
print("\n--- 編碼後的資料前五筆 ---")
print(train_df.head())

    