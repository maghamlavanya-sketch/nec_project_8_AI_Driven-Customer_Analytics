# AI-Driven Customer Behavior Analytics Platform

## Live Demo

### Render Deployment URL

https://lavy-project-8.onrender.com/

---

# Project Overview

AI-Driven Customer Behavior Analytics Platform is an end-to-end Machine Learning application built using Python, Streamlit, Scikit-Learn, Pandas, NumPy, Plotly, and Joblib.

The system helps businesses understand customer behavior patterns, identify customer segments, predict purchasing behavior, detect churn risk, and generate personalized recommendations through advanced analytics and machine learning.

Users can:

* Upload their own customer dataset
* Use the built-in sample dataset
* Analyze customer behavior
* Predict purchase probability
* Detect churn risk
* Generate personalized recommendations
* Visualize insights through interactive dashboards

The application automatically processes customer data, trains machine learning models, performs segmentation, generates predictions, and provides actionable business insights.

---

# Key Features

## Dataset Management

* Upload customer dataset
* Use default customer dataset
* Live dataset preview
* Dataset statistics
* Customer profile exploration

---

## Data Preprocessing

* Missing value analysis
* Duplicate record detection
* Outlier identification
* Feature engineering
* Data cleaning pipeline
* Processed dataset export

---

## Customer Dashboard

Business KPIs:

* Total Customers
* Average Income
* Average Spending
* Average Purchase Frequency
* Churn Rate
* High Value Customers

Interactive Analytics:

* Age Distribution
* Income Distribution
* Gender Distribution
* Spending Analysis
* Purchase Frequency Analysis
* Customer Location Analysis

---

## Customer Segmentation

Automatic Customer Grouping using K-Means Clustering

Segments:

* High Value Customers
* Loyal Customers
* Potential Customers
* At-Risk Customers

Outputs:

* Cluster Visualization
* Segment Distribution
* Customer Segment Statistics
* Segment Summary Table

---

## Purchase Prediction

Predict customer purchasing behavior based on:

* Age
* Salary
* Tenure
* Purchase Frequency
* Previous Spending

Outputs:

* Purchase Probability
* Prediction Result
* Feature Impact Visualization
* Prediction Graph
* Customer Prediction Table

---

## Churn Prediction

Predict customer churn probability

Inputs:

* Age
* Salary
* Tenure
* Spending
* Purchase Frequency

Outputs:

* Churn Risk Percentage
* Risk Category
* Churn Visualization
* Customer Risk Table
* Probability Gauge Chart

---

## Recommendation Engine

Generate personalized recommendations based on:

* Spending Pattern
* Purchase Frequency
* Customer Segment
* Salary Group

Outputs:

* Recommended Marketing Action
* Customer Value Category
* Retention Suggestions
* Upselling Opportunities
* Recommendation Dashboard

---

## Reports

Download reports as:

* CSV
* Excel
* PDF

Generated Reports:

* Customer Summary Report
* Segmentation Report
* Prediction Report
* Churn Report

---

# Machine Learning Models

## Customer Segmentation

Algorithm:

K-Means Clustering

Features:

* Age
* Salary
* Spending
* Purchase Frequency
* Tenure

---

## Purchase Prediction

Algorithm:

Random Forest Classifier

Target:

Purchase Probability

Evaluation Metrics:

* Accuracy
* Precision
* Recall
* F1 Score

---

## Churn Prediction

Algorithm:

Random Forest Classifier

Target:

Churn Status

Evaluation Metrics:

* Accuracy
* Precision
* Recall
* ROC-AUC Score

---

# Technology Stack

## Frontend

* Streamlit

## Data Processing

* Pandas
* NumPy

## Visualization

* Plotly

## Machine Learning

* Scikit-Learn

## Model Storage

* Joblib

---

# Project Structure

AI_Driven_Customer_Analytics/

│

├── app.py

├── requirements.txt

├── runtime.txt

├── README.md

├── train_models.py

├── generate_dataset.py

│

├── dataset/

│   └── customer_dataset.csv

│

├── models/

│   ├── segmentation_model.pkl

│   ├── purchase_model.pkl

│   └── churn_model.pkl

│

├── pages/

│   ├── Dashboard.py

│   ├── Segmentation.py

│   ├── Prediction.py

│   ├── Churn.py

│   └── Recommendation.py

│

├── analytics/

│   ├── customer_stats.py

│   ├── churn_analysis.py

│   ├── recommendation_engine.py

│   └── segmentation_analysis.py

│

├── utils/

│   ├── data_loader.py

│   ├── charts.py

│   ├── model_loader.py

│   └── helpers.py

│

└── reports/

```
├── customer_report.py

└── export_utils.py
```

---

# Dataset Features

Customer Dataset Fields:

* customer_id
* name
* age
* gender
* city
* salary
* tenure
* purchase_frequency
* spent
* churn

---

# Installation

## Clone Repository

git clone https://github.com/your-username/AI_Driven_Customer_Analytics.git

## Navigate

cd AI_Driven_Customer_Analytics

## Install Requirements

pip install -r requirements.txt

## Train Models

python train_models.py

## Run Application

streamlit run app.py

---

# Analytical Process

Customer Dataset

↓

Data Cleaning

↓

Feature Engineering

↓

Exploratory Data Analysis

↓

Customer Segmentation

↓

Purchase Prediction

↓

Churn Prediction

↓

Recommendation Generation

↓

Interactive Dashboard

↓

Business Insights

---

# Future Enhancements

* XGBoost Customer Prediction
* Deep Learning Recommendation Engine
* Real-Time Customer Monitoring
* Customer Lifetime Value Prediction
* Marketing Campaign Analytics
* Cloud Database Integration
* GenAI Customer Insights
* Automated Business Reports

---

# Author

Lavanya Magham

AI / Machine Learning Project
