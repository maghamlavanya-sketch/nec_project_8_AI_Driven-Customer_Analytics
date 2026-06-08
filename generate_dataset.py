import pandas as pd
import random
from faker import Faker

fake = Faker("en_IN")

cities = [
    "Bangalore",
    "Hyderabad",
    "Chennai",
    "Mumbai",
    "Pune",
    "Delhi"
]

categories = [
    "Electronics",
    "Fashion",
    "Groceries",
    "Home",
    "Sports"
]

rows = []

for i in range(1, 201):

    age = random.randint(18, 65)

    income = random.randint(25000, 200000)

    tenure = random.randint(1, 120)

    purchase_frequency = random.randint(1, 20)

    website_visits = random.randint(1, 50)

    last_purchase_days = random.randint(1, 90)

    discount_usage = random.randint(0, 1)

    total_spent = purchase_frequency * random.randint(500, 5000)

    purchase_next_month = (
        1 if purchase_frequency > 8
        and last_purchase_days < 30
        else 0
    )

    churn = (
        1 if last_purchase_days > 60
        else 0
    )

    rows.append([
        f"C{i:03}",
        fake.name(),
        age,
        random.choice(["Male", "Female"]),
        random.choice(cities),
        income,
        tenure,
        purchase_frequency,
        total_spent,
        website_visits,
        last_purchase_days,
        discount_usage,
        random.choice(categories),
        churn,
        purchase_next_month
    ])

columns = [
    "customer_id",
    "name",
    "age",
    "gender",
    "city",
    "income",
    "tenure",
    "purchase_frequency",
    "total_spent",
    "website_visits",
    "last_purchase_days",
    "discount_usage",
    "product_category",
    "churn",
    "purchase_next_month"
]

df = pd.DataFrame(rows, columns=columns)

df.to_csv(
    "dataset/customer_dataset.csv",
    index=False
)

print("Dataset Generated")