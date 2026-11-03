import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from pathlib import Path

# Project folder ka path
PROJECT_DIR = Path.cwd()

# Raw CSV load karo
file_path = PROJECT_DIR / "data" / "raw" / "swiggy_file.csv"

df = pd.read_csv(file_path)

print("Data loaded successfully!")
print("Rows and columns:", df.shape)

df.head()

# Column names
print(df.columns.tolist())

# Data types
df.info()

# Summary statistics
df.describe(include="all").T

# Missing values analysis

missing = df.isnull().sum()

print("\nMissing Values:")
print(missing)

# Missing values percentage

missing_percentage = (df.isnull().sum() / len(df)) * 100

print("\nMissing Values Percentage:")
print(missing_percentage.round(2))

# Duplicate records analysis

duplicate_count = df.duplicated().sum()

print("\nDuplicate Records:")
print("Total Duplicates:", duplicate_count)

# Check duplicate percentage

duplicate_percentage = (duplicate_count / len(df)) * 100

print("Duplicate Percentage:", round(duplicate_percentage, 2), "%")

# Create a clean copy of original data

df_clean = df.copy()

# Remove duplicate records

df_clean = df_clean.drop_duplicates()

# Check remaining duplicates

print("\nAfter Removing Duplicates:")
print("Original Rows:", len(df))
print("Clean Rows:", len(df_clean))
print("Remaining Duplicates:", df_clean.duplicated().sum())

# Check missing values in clean dataset

print("\nMissing Values Before Cleaning:")

print(df_clean.isnull().sum())

# Check sample data of missing columns

print("\nCuisine Samples:")
print(df_clean["Cuisine"].dropna().head(10))

print("\nNumber of Ratings Samples:")
print(df_clean["Number of Ratings"].dropna().head(10))

print("\nOffer Name Samples:")
print(df_clean["Offer Name"].dropna().head(10))

print("\nArea Samples:")
print(df_clean["Area"].dropna().head(10))

# Remove rows where Cuisine is missing

df_clean = df_clean.dropna(subset=["Cuisine"])

print("\nAfter Cleaning Cuisine:")
print("Missing Cuisine:", df_clean["Cuisine"].isnull().sum())

print("Remaining Rows:", len(df_clean))

# Check Number of Ratings distribution

print("\nNumber of Ratings Value Counts:")

print(df_clean["Number of Ratings"].value_counts().head(20))

print("\nMissing Number of Ratings:")

print(df_clean["Number of Ratings"].isnull().sum())

# Fill missing Number of Ratings

df_clean["Number of Ratings"] = df_clean["Number of Ratings"].fillna("Not Available")

# Verify cleaning

print("\nAfter Cleaning Number of Ratings:")

print("Missing Values:",
      df_clean["Number of Ratings"].isnull().sum())

print("Not Available Count:",
      (df_clean["Number of Ratings"] == "Not Available").sum())

print("Remaining Rows:", len(df_clean))

# Clean Offer Name

df_clean["Offer Name"] = df_clean["Offer Name"].fillna("No Offer")

print("\nAfter Cleaning Offer Name:")

print("Missing Values:",
      df_clean["Offer Name"].isnull().sum())

print("No Offer Count:",
      (df_clean["Offer Name"] == "No Offer").sum())

print("Remaining Rows:", len(df_clean))

# Clean Area

df_clean["Area"] = df_clean["Area"].fillna("Unknown Area")

print("\nAfter Cleaning Area:")

print("Missing Area:",
      df_clean["Area"].isnull().sum())

print("Unknown Area Count:",
      (df_clean["Area"] == "Unknown Area").sum())

print("Remaining Rows:", len(df_clean))

print("\nFinal Missing Values:")
print(df_clean.isnull().sum())

print("\nFinal Dataset Shape:")
print(df_clean.shape)

# Numerical Columns

print("Numerical Columns:")
print(df_clean.select_dtypes(include="number").columns)

# Categorical Columns

print("\nCategorical Columns:")
print(df_clean.select_dtypes(include="object").columns)

# Numerical Columns

print("Numerical Columns:")
print(df_clean.select_dtypes(include="number").columns.tolist())

# Categorical Columns

print("\nCategorical Columns:")
print(df_clean.select_dtypes(include=["object", "str"]).columns.tolist())

# Check data types

print("\nColumn Data Types:")
print(df_clean.dtypes)

# Check numerical data samples

print("\nRating Samples:")
print(df_clean["Rating"].head(10))

print("\nAverage Price Samples:")
print(df_clean["Average Price"].head(10))

print("\nNumber of Offers Samples:")
print(df_clean["Number of Offers"].head(10))

# Check unique values

print("\nRating Unique Values:")
print(df_clean["Rating"].value_counts().head(20))

print("\nAverage Price Unique Values:")
print(df_clean["Average Price"].value_counts().head(20))

print("\nNumber of Ratings Unique Values:")
print(df_clean["Number of Ratings"].value_counts().head(20))

# Convert Rating into Numeric

df_clean["Rating"] = pd.to_numeric(
    df_clean["Rating"],
    errors="coerce"
)

# Clean Average Price

df_clean["Average Price"] = (
    df_clean["Average Price"]
    .str.replace("₹", "", regex=False)
    .str.replace(" for two", "", regex=False)
)

df_clean["Average Price"] = pd.to_numeric(
    df_clean["Average Price"],
    errors="coerce"
)

# Check Data Types

print("Updated Data Types:")
print(df_clean.dtypes)

print("\nUpdated Dataset:")
print(df_clean.head())

print("Number of Ratings Before Cleaning:")

print(df_clean["Number of Ratings"].value_counts())

# Extract Rating Count

rating_count = (
    df_clean["Number of Ratings"]
    .str.extract(r"(\d+(?:\.\d+)?)\s*(K)?")
)

df_clean["Rating Count Minimum"] = (
    pd.to_numeric(rating_count[0], errors="coerce")
    * rating_count[1].map({"K": 1000}).fillna(1)
)

# Check Results

print("Rating Count Samples:")
print(df_clean[["Number of Ratings",
                "Rating Count Minimum"]].head(20))

print("\nNew Column Data Type:")
print(df_clean["Rating Count Minimum"].dtype)

# Check missing values after cleaning

print("Missing Values After Cleaning:")
print(df_clean.isnull().sum())

# Check updated data types

print("\nUpdated Data Types:")
print(df_clean.dtypes)

# Check final dataset shape

print("\nFinal Dataset Shape:")
print(df_clean.shape)

# Check missing rating values

print("Missing Rating Analysis:")

print(df_clean[df_clean["Rating"].isnull()]
      ["Rating"].isnull().sum())

# Check rating distribution

print("\nRating Distribution:")

print(df_clean["Rating"].value_counts(dropna=False).head(15))

# Check missing rating percentage

print("\nMissing Rating Percentage:")

print(df_clean["Rating"].isnull().mean() * 100)

# Duplicate Values Analysis

print("\nDuplicate Rows Analysis:")

# Total duplicate rows

print("Total Duplicate Rows:")
print(df_clean.duplicated().sum())

# Check duplicate restaurant names

print("\nDuplicate Restaurant Names:")
print(df_clean["Restaurant Name"].duplicated().sum())

# Display duplicate records

print("\nDuplicate Records:")
print(df_clean[df_clean.duplicated()].head(10))

# Data Validation

print("\nRating Range:")
print("Minimum Rating:", df_clean["Rating"].min())
print("Maximum Rating:", df_clean["Rating"].max())

print("\nAverage Price Range:")
print("Minimum Price:", df_clean["Average Price"].min())
print("Maximum Price:", df_clean["Average Price"].max())

print("\nNumber of Offers Range:")
print("Minimum Offers:", df_clean["Number of Offers"].min())
print("Maximum Offers:", df_clean["Number of Offers"].max())

print("\nPure Veg Unique Values:")
print(df_clean["Pure Veg"].value_counts())

print("\nLocation Unique Values:")
print(df_clean["Location"].nunique())

# Average Price Outlier Analysis

print("\nAverage Price Statistics:")

print(df_clean["Average Price"].describe())

print("\nTop 20 Highest Prices:")

print(
    df_clean["Average Price"]
    .sort_values(ascending=False)
    .head(20)
)

print("\nBottom 20 Lowest Prices:")

print(
    df_clean["Average Price"]
    .sort_values()
    .head(20)
)

# IQR Method for Outlier Detection

Q1 = df_clean["Average Price"].quantile(0.25)

Q3 = df_clean["Average Price"].quantile(0.75)

IQR = Q3 - Q1

Lower_Limit = Q1 - 1.5 * IQR

Upper_Limit = Q3 + 1.5 * IQR

print("\nIQR Analysis:")

print("Q1:", Q1)
print("Q3:", Q3)
print("IQR:", IQR)

print("Lower Limit:", Lower_Limit)
print("Upper Limit:", Upper_Limit)

# Identify Outliers

outliers = df_clean[
    (df_clean["Average Price"] < Lower_Limit) |
    (df_clean["Average Price"] > Upper_Limit)
]

print("\nTotal Outliers:")
print(len(outliers))

print("\nOutlier Percentage:")
print((len(outliers) / len(df_clean)) * 100)

print("\nHighest Price Outliers:")

print(
    outliers[
        ["Restaurant Name", "Average Price", "Location"]
    ].sort_values(
        by="Average Price",
        ascending=False
    ).head(20)
)

# Investigate Extreme Price Values

print("\nRestaurants Above 1000:")

print(
    df_clean[
        df_clean["Average Price"] > 1000
    ][
        ["Restaurant Name", "Average Price", "Location"]
    ].sort_values(
        by="Average Price",
        ascending=False
    ).head(30)
)

print("\nPrice Distribution:")

print(
    df_clean["Average Price"]
    .value_counts()
    .head(20)
)

print("Highest 10 Average Prices:")
print(
    df_clean.nlargest(10, "Average Price")[
        ["Restaurant Name", "Average Price", "Location"]
    ]
)

# top_10 = df_clean.nlargest(10, "Average Price")

# plt.figure(figsize=(12, 6))

# sns.barplot(
#     data=top_10,
#     x="Average Price",
#     y="Restaurant Name",
#     hue="Restaurant Name",
#     palette="viridis",
#     legend=False
# )

# plt.title("Top 10 Restaurants by Average Price", fontsize=16)
# plt.xlabel("Average Price (₹)", fontsize=12)
# plt.ylabel("Restaurant Name", fontsize=12)

# plt.tight_layout()
# plt.savefig("top_10_restaurants.png", dpi=300)
# plt.show()

print("The Food Town Records:")

print(
    df_clean[
        df_clean["Restaurant Name"] == "The Food Town"
    ][["Restaurant Name", "Average Price", "Location"]]
)

print("Highest 20 Average Prices:")

print(
    df_clean.nlargest(20, "Average Price")[
        ["Restaurant Name", "Average Price", "Location"]
    ].to_string(index=False)
)

print("Original Data Record:")

print(
    df[
        (df["Restaurant Name"] == "The Food Town") &
        (df["Location"] == "Lalitpur")
    ].to_string(index=False)
)

row = df[
    (df["Restaurant Name"] == "The Food Town") &
    (df["Location"] == "Lalitpur")
]

print("Original Average Price:")
print(repr(row["Average Price"].iloc[0]))

print("Cleaned Average Price:")
print(df_clean.loc[row.index, "Average Price"].values)

df_clean.loc[
    df_clean["Average Price"] > Upper_Limit,
    "Average Price"
] = np.nan

df_clean["Average Price"] = df_clean["Average Price"].fillna(
    df_clean["Average Price"].median()
)

print("Cleaned Average Price:")
print(df_clean["Average Price"].describe())

# Handle both lower and upper outliers
df_clean.loc[
    (df_clean["Average Price"] < Lower_Limit) |
    (df_clean["Average Price"] > Upper_Limit),
    "Average Price"
] = np.nan

# Fill missing values with median
df_clean["Average Price"] = df_clean["Average Price"].fillna(
    df_clean["Average Price"].median()
)

# Verify cleaned data
print(df_clean["Average Price"].describe())

# Save cleaned dataset
output_path = PROJECT_DIR / "data" / "cleaned" / "swiggy_cleaned.csv"

output_path.parent.mkdir(parents=True, exist_ok=True)

df_clean.to_csv(output_path, index=False)

print("Cleaned dataset saved successfully!")

# Top 10 locations by restaurant count

# top_locations = (
#     df_clean["Location"]
#     .value_counts()
#     .head(10)
#     .reset_index()
# )

# top_locations.columns = ["Location", "Restaurant Count"]

# plt.figure(figsize=(12, 6))

# sns.barplot(
#     data=top_locations,
#     x="Restaurant Count",
#     y="Location",
#     hue="Location",
#     palette="magma",
#     legend=False
# )

# plt.title("Top 10 Locations by Restaurant Count", fontsize=16)
# plt.xlabel("Number of Restaurants")
# plt.ylabel("Location")

# plt.tight_layout()
# plt.savefig("top_10_locations.png", dpi=300)
# plt.show()

# Top 10 cuisines

# top_cuisines = (
#     df_clean["Cuisine"]
#     .value_counts()
#     .head(10)
#     .reset_index()
# )

# top_cuisines.columns = ["Cuisine", "Restaurant Count"]

# plt.figure(figsize=(12, 6))

# sns.barplot(
#     data=top_cuisines,
#     x="Restaurant Count",
#     y="Cuisine",
#     hue="Cuisine",
#     palette="viridis",
#     legend=False
# )

# plt.title("Top 10 Cuisines by Restaurant Count", fontsize=16)
# plt.xlabel("Number of Restaurants")
# plt.ylabel("Cuisine")

# plt.tight_layout()
# plt.savefig("top_10_cuisines.png", dpi=300)
# plt.show()

# Average price by location

# location_price = (
#     df_clean.groupby("Location")["Average Price"]
#     .mean()
#     .sort_values(ascending=False)
#     .head(10)
#     .reset_index()
# )

# plt.figure(figsize=(12, 6))

# sns.barplot(
#     data=location_price,
#     x="Average Price",
#     y="Location",
#     hue="Location",
#     palette="coolwarm",
#     legend=False
# )

# plt.title("Top 10 Locations by Average Restaurant Price", fontsize=16)
# plt.xlabel("Average Price (₹)")
# plt.ylabel("Location")

# plt.tight_layout()
# plt.savefig("average_price_by_location.png", dpi=300)
# plt.show()

# Business Insights

print("\n========== BUSINESS INSIGHTS ==========")

print("\n1. Total Restaurants:")
print(df_clean["Restaurant Name"].nunique())

print("\n2. Total Locations:")
print(df_clean["Location"].nunique())

print("\n3. Average Restaurant Price:")
print(round(df_clean["Average Price"].mean(), 2))

print("\n4. Most Common Location:")
print(df_clean["Location"].value_counts().idxmax())

print("\n5. Most Common Cuisine:")
print(df_clean["Cuisine"].value_counts().idxmax())

print("\n6. Most Expensive Restaurant:")
print(
    df_clean.loc[
        df_clean["Average Price"].idxmax(),
        ["Restaurant Name", "Average Price", "Location"]
    ]
)

from pathlib import Path

cleaned_folder = Path("data/cleaned")
cleaned_folder.mkdir(parents=True, exist_ok=True)

df_clean.to_csv(
    cleaned_folder / "swiggy_cleaned.csv",
    index=False
)

print("Cleaned dataset saved successfully!")