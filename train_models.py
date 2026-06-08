import pandas as pd
import joblib

from sklearn.cluster import KMeans
from sklearn.ensemble import RandomForestClassifier

df = pd.read_csv(
    "dataset/customer_dataset.csv"
)

# Segmentation

segment_features = df[
    [
        "income",
        "purchase_frequency",
        "total_spent"
    ]
]

kmeans = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10
)

kmeans.fit(segment_features)

joblib.dump(
    kmeans,
    "models/segmentation_model.pkl"
)

# Purchase Prediction

X_purchase = df[
    [
        "age",
        "income",
        "tenure",
        "purchase_frequency",
        "total_spent",
        "website_visits",
        "last_purchase_days"
    ]
]

y_purchase = df["purchase_next_month"]

purchase_model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

purchase_model.fit(
    X_purchase,
    y_purchase
)

joblib.dump(
    purchase_model,
    "models/purchase_model.pkl"
)

# Churn Prediction

y_churn = df["churn"]

churn_model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

churn_model.fit(
    X_purchase,
    y_churn
)

joblib.dump(
    churn_model,
    "models/churn_model.pkl"
)

print("All Models Saved")