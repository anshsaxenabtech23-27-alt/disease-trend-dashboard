import pandas as pd
import matplotlib.pyplot as plt

# Load COVID dataset
df = pd.read_csv(
    r"C:\Users\anshs\OneDrive\Documents\Desktop\disease trend dashboard\covid_data.csv\Latest Covid-19 India Status.csv"
)

# -----------------------------
# 1. Basic Data Information
# -----------------------------
print("Dataset Shape:", df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nFirst 5 Rows:")
print(df.head())

# -----------------------------
# 2. Missing Values
# -----------------------------
print("\nMissing Values:")
print(df.isnull().sum())

# -----------------------------
# 3. Top 10 States by Cases
# -----------------------------
top_cases = df.nlargest(10, "Total Cases")

print("\nTop 10 States by Total Cases:")
print(top_cases[["State/UTs", "Total Cases"]])

# -----------------------------
# 4. Top 10 States by Deaths
# -----------------------------
top_deaths = df.nlargest(10, "Deaths")

print("\nTop 10 States by Deaths:")
print(top_deaths[["State/UTs", "Deaths"]])

# -----------------------------
# 5. Visualization
# -----------------------------
plt.figure(figsize=(10, 6))

plt.bar(
    top_cases["State/UTs"],
    top_cases["Total Cases"]
)

plt.xticks(rotation=90)
plt.xlabel("State/UTs")
plt.ylabel("Total Cases")
plt.title("Top 10 States by COVID-19 Cases")

plt.tight_layout()
plt.show()