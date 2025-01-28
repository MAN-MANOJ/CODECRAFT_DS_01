import matplotlib.pyplot as plt
import pandas as pd

# Load the full dataset from the file
file_path = 'age_data.csv'
data = pd.read_csv(file_path)

# Rename columns for clarity
data.columns = [
    "Country",
    "Indicator",
    "Age_0_14",
    "Age_15_64",
    "Age_65_plus",
    "Young_Percentage",
    "Old_Percentage",
    "Dependency_Ratio",
    "Crude_Death_Rate",
    "Crude_Birth_Rate",
    "Other"
]

# Select relevant columns
age_data = data[["Country", "Age_0_14", "Age_15_64", "Age_65_plus"]].dropna()

# Convert age columns to numeric for visualization
age_data["Age_0_14"] = pd.to_numeric(age_data["Age_0_14"], errors="coerce")
age_data["Age_15_64"] = pd.to_numeric(age_data["Age_15_64"], errors="coerce")
age_data["Age_65_plus"] = pd.to_numeric(age_data["Age_65_plus"], errors="coerce")

# Drop rows with NaN values after conversion
age_data_cleaned = age_data.dropna()

# Create a bar chart for age group distributions
age_groups = ["Age_0_14", "Age_15_64", "Age_65_plus"]
average_ages = age_data_cleaned[age_groups].mean()

plt.figure(figsize=(10, 6))
average_ages.plot(kind="bar", color=['skyblue', 'orange', 'lightgreen'])
plt.title("Average Age Group Distribution", fontsize=16)
plt.xlabel("Age Groups", fontsize=14)
plt.ylabel("Average Percentage", fontsize=14)
plt.xticks(rotation=0)
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.show()

# Create histograms for all age groups
for age_group in age_groups:
    plt.figure(figsize=(10, 6))
    plt.hist(age_data_cleaned[age_group], bins=10, color="lightblue", edgecolor="black")
    plt.title(f"Histogram of {age_group} Distribution", fontsize=16)
    plt.xlabel(f"{age_group} Percentage", fontsize=14)
    plt.ylabel("Frequency", fontsize=14)
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.show()