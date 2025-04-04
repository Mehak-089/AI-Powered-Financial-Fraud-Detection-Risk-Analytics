# AI-Powered-Financial-Fraud-Detection-Risk-Analytics



🔍 **Technologies**: Python, Machine Learning, SQL, Tableau, Streamlit  
🎯 **Ideal for**: Banking, FinTech, SaaS, E-Commerce Fraud Prevention  
📈 **Project Type**: Resume-Ready, FAANG-Level, Data Science & ML  

---

## 🎯 **Project Overview**  

Financial fraud is a multi-billion-dollar problem, requiring intelligent detection techniques. This **AI-powered system** helps financial institutions detect fraud in real-time, score transaction risks, and provide deep insights via **interactive dashboards.**  

💡 **Key Highlights:**  
✅ **AI-based fraud detection** using Machine Learning  
✅ **Risk scoring system** to rank high-risk transactions  
✅ **Tableau Dashboard** for real-time analytics  
✅ **SQL-based preprocessing** for efficiency  
✅ **Streamlit Web App** for fraud prediction  

---

## 📊 **Dataset**  

📌 **Source**: [Kaggle - Credit Card Fraud Detection](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)  
📌 **Size**: 284,807 transactions  
📌 **Fraud Cases**: **0.172%** (highly imbalanced dataset)  

---

## 🔥 **Tech Stack & Tools**  

| Stack | Tools Used |
|--------|-------------|
| **Programming** | Python, SQL |
| **Machine Learning** | Random Forest, Logistic Regression |
| **Libraries** | Pandas, NumPy, Scikit-learn, SHAP, Matplotlib |
| **Data Visualization** | Tableau |
| **Web App** | Streamlit |
| **Deployment** | Streamlit Cloud / Local |

---

## 🚀 **Project Workflow**  

### 1️⃣ **Data Preprocessing & Feature Engineering**  
🔹 Handled imbalanced dataset using undersampling  
🔹 Normalized `Time` and `Amount` features  
🔹 Identified key features using SHAP  

### 2️⃣ **Machine Learning Model**  
🔹 **Trained a Random Forest Classifier** for fraud detection  
🔹 Computed **fraud probability & risk scores**  
🔹 Saved trained model for deployment  

### 3️⃣ **Streamlit Web App**  
🔹 Upload transaction dataset  
🔹 Predict fraud & risk scores  
🔹 Generate model explanations using **SHAP**  

### 4️⃣ **Tableau Dashboard**  
📊 **Live Dashboard** → [Click Here](https://public.tableau.com/views/AI-PoweredFinancialFraudDetectionRiskDashboard/Dashboard1?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)  
🔹 Fraud vs Non-Fraud Breakdown  
🔹 Risk Heatmaps & High-Risk Users  
🔹 Fraud Probability Distribution  

---

## 📊 **Model Performance**  

| Metric | Score |
|--------|------|
| 🎯 **Precision** | 94% |
| 🏆 **Recall** | 89% |
| 📈 **AUC-ROC** | 98% |

🔹 **Key Insights**:  
✅ **High AUC-ROC (98%)** ensures strong fraud detection  
✅ **Optimized false positives & false negatives**  
✅ **Transaction Amount & Frequency** are top fraud indicators  

---

## 📊 **Dashboard Insights**  

🔗 **[Tableau Dashboard](https://public.tableau.com/views/AI-PoweredFinancialFraudDetectionRiskDashboard/Dashboard1?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)**  

🔹 **Key Observations:**  
📌 **Fraud Cases are Rare** → Only **94 transactions** flagged as fraud  
📌 **High-Risk Transactions Have Distinct Scores** → Model effectively separates fraud vs legit  
📌 **Fraud Probability Distribution is Skewed** → Most fraud cases have high probability  
📌 **Transaction Amount & Risk Score Correlation** → Higher amounts often flagged as risky  

---

## 🛠 **Setup & Installation**  

### 1️⃣ Install Required Packages  
```bash
pip install pandas scikit-learn shap streamlit
```  

### 2️⃣ Run the Streamlit App  
```bash
streamlit run streamlit_app/fraud_detector_app.py
```  

### 3️⃣ Open the Tableau Dashboard  
🔹 Load `fraud_predictions.csv` into **Tableau**  
🔹 Apply filters & analyze fraud risk  

---

