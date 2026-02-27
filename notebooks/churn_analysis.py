#data cleaning
import pandas as pd
df = pd.read_csv("C:\\Users\\Mercy Kimani\\OneDrive\\Desktop\\Telco-Customer-Churn.csv")
print(df.head())
#check missing values
df.isnull()
# fix data types
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
df['TotalCharges'].isnull().sum()
df['SeniorCitizen'] = df['SeniorCitizen'].astype('category')
#checking duplicates
df.duplicated().sum()
df = df.drop_duplicates()
df.replace("No internet service", "No", inplace=True)
df.replace("No phone service", "No", inplace=True)
#checking outliers
df.describe()
import seaborn as sns
import matplotlib.pyplot as plt
sns.boxplot(x=df['MonthlyCharges'])
plt.show()
#create new column calle TenureGroup
df["TenureGroup"] = pd.cut(df["tenure"],
                           bins=[0,12,24,48,60,100],
                           labels=["0-1yr","1-2yr","2-4yr","4-5yr","5+yr"])
#Overall churn rate
df['Churn_flag'] = df['Churn'].map({'Yes': 1, 'No': 0})
# Overall churn rate
overall_churn_rate = df['Churn_flag'].mean()
print(f"Overall churn rate: {overall_churn_rate:.2%}")

# Group by contract
contract_churn = df.groupby('Contract')['Churn_flag'].mean().reset_index()

# Plot churn rate by contract type
sns.barplot(data=contract_churn, x='Contract', y='Churn_flag')
plt.ylabel('Churn Rate')
plt.title('Churn Rate by Contract Type')
plt.show()
# Scatter plot of churn by tenure
sns.histplot(data=df, x='tenure', hue='Churn', multiple='stack', bins=30)
plt.title('Churn Distribution by Tenure')
plt.xlabel('Tenure (months)')
plt.show()
#Churn rate by tenure
tenure_churn = df.groupby('tenure')['Churn_flag'].mean().reset_index()
sns.lineplot(data=tenure_churn, x='tenure', y='Churn_flag')
plt.ylabel('Churn Rate')
plt.title('Churn Rate by Tenure')
plt.show()
# line plot of churn rate by monthly charges
monthly_churn = df.groupby('MonthlyCharges')['Churn_flag'].mean().reset_index()
sns.lineplot(data=monthly_churn, x='MonthlyCharges', y='Churn_flag')
plt.ylabel('Churn Rate')
plt.title('Churn Rate by Monthly Charges')
plt.show()
#clean data
df_cleaned=df.to_csv("cleaned_telco_data.csv", index=False)
