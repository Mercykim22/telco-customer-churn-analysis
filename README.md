# telco-customer-churn-analysis
# EXECUTIVE SUMMARY
This project analyzes customer churn behavior in a telecommunications company using Excel, Python, and Power BI. The objective was to identify the key drivers of customer attrition and provide actionable business recommendations to improve retention.Through data cleaning, exploratory data analysis, and dashboard development, the analysis revealed that customers on month-to-month contracts, those with higher monthly charges, and customers with shorter tenure exhibit significantly higher churn rates. Additionally, certain service types and payment methods were associated with increased churn risk.A comprehensive Power BI dashboard was developed to visualize churn patterns and customer segments, enabling stakeholders to monitor high-risk groups effectively. Based on the findings, strategic recommendations such as promoting long-term contracts, enhancing early-stage customer engagement, and implementing targeted retention campaigns were proposed.This project demonstrates strong analytical, visualization, and business interpretation skills by transforming raw data into meaningful insights that support data-driven decision-making.
![image alt](https://github.com/Mercykim22/telco-customer-churn-analysis/blob/2d2e04c0e2da22d3b67adbc5645a9e7b14bea6e7/A%20dashboard%201.PNG)

# BUSINESS PROBLEM
The telecom company is experiencing a significant rate of customer churn, which directly impacts revenue, profitability, and long-term business sustainability. Customer acquisition costs in the telecommunications industry are typically high due to marketing, promotions, and onboarding expenses. As a result, losing existing customers not only reduces recurring revenue but also increases the overall cost of growth.Churn is often influenced by multiple factors such as pricing, contract type, service quality, customer tenure, billing methods, and competition. Without a clear understanding of why customers leave, the company risks continuing revenue leakage and ineffective retention strategies.The primary objective of this analysis is to identify the key drivers of customer churn using historical customer data. By examining demographic characteristics, service subscriptions, billing information, and contract details, this project aims to:
- Determine which customer segments are most likely to churn
- Identify behavioral and service-related patterns associated with churn
- Quantify the impact of different factors on customer attrition
- Provide actionable, data-driven recommendations to reduce churn
The ultimate goal is to support strategic decision-making by enabling the company to implement targeted retention initiatives, improve customer satisfaction, and enhance overall customer lifetime value
# DATASET DESCRIPTION
The Telco Customer Churn Dataset contains information about telecom customers and whether they have discontinued their service. The dataset includes several categories of variables such as customer information (gender, senior citizen status, partner, and dependents), account information (tenure, contract type, payment method, monthly charges, and total charges), and services subscribed by customers (phone service, internet service, online security, tech support, and streaming TV or movies). The target variable in the dataset is Churn, which indicates whether a customer has left the company or continues using the service (Yes/No).
# TOOLS USED
- Excel – pivot analysis,visualization
- Python – Data cleaning,Data analysis (Pandas, Matplotlib, Seaborn),
- Power BI – Interactive dashboard
# Data Cleaning Process
Handled missing values
Converted data types
# Exploratory Data Analysis (EDA)
- Churn rate percentage
The analysis shows that the overall churn rate is approximately 27%, indicating that more than one-quarter of the customers have discontinued the service. This relatively high churn rate suggests the need for improved customer retention strategies
- Contract type vs churn
![image alt](https://github.com/Mercykim22/telco-customer-churn-analysis/blob/b87a3d73ef79ee8df57164177109400161e233e7/images/Churn%20vs%20contract%20type.PNG)
- Monthly charges vs churn
- Tenure vs churn
  ![image alt](https://github.com/Mercykim22/telco-customer-churn-analysis/blob/5c3c0dd7d414bc42c10d967b7f634ae1d8a0ef09/images/churn%20rate%20by%20tenure%20line%20graph.PNG)
 As tenure increases, the line drops sharply, meaning customers who stay longer are less likely to leave.
- Internet service impact
  ![image alt](https://github.com/Mercykim22/telco-customer-churn-analysis/blob/c63b101d4633de8fabeccd0939b903027778f3d0/images/Churn%20vs%20internet%20service.PNG)

The bar graph shows that customers using Fiber Optic internet exhibit the highest churn rate compared to DSL and customers without internet service. This suggests that internet service type, particularly Fiber Optic, may be associated with higher customer dissatisfaction or higher service costs.
# KEY INSIGHTS
- Customers on month-to-month contracts churn more
- High monthly charges increase churn risk
- Customers with short tenure are more likely to churn
- Fiber optic users show higher churn rates
# Business Recommendations
- Offer discounts for long-term contracts
- Create loyalty programs for high-risk customers
- Provide targeted retention campaigns for fiber optic users
- Improve onboarding experience for new customers
- Offer bundled services at reduced prices
