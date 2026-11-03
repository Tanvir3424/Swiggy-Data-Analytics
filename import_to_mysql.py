import csv
import mysql.connector
import re
import os
from dotenv import load_dotenv

load_dotenv()
# CSV file location
csv_path = r"C:\Swiggy_Data_Analytics\data\cleaned\swiggy_cleaned.csv"

# MySQL connection
conn = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)

cursor = conn.cursor()

def clean_number(value):
    if not value or not value.strip():
        return None
    match = re.search(r"\d+\.?\d*", value.replace(",", ""))
    return float(match.group()) if match else None

insert_query = """
INSERT INTO swiggy_restaurants
(
    restaurant_name, cuisine, rating, number_of_ratings,
    average_price, number_of_offers, offer_name, area,
    pure_veg, location, rating_count_minimum
)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

rows = []

with open(csv_path, "r", encoding="utf-8-sig", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        rating = clean_number(row["Rating"])
        price = clean_number(row["Average Price"])
        offers = clean_number(row["Number of Offers"])

        rows.append((
            row["Restaurant Name"],
            row["Cuisine"],
            rating,
            row["Number of Ratings"],
            price,
            int(offers) if offers is not None else None,
            row["Offer Name"],
            row["Area"],
            row["Pure Veg"],
            row["Location"],
            row["Rating Count Minimum"]
        ))

cursor.executemany(insert_query, rows)
conn.commit()

print("Total rows imported:", cursor.rowcount)

cursor.close()
conn.close()