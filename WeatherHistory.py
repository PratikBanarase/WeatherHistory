import pandas as pd
import matplotlib.pyplot as plt

# Load your dataset
df = pd.read_csv("/content/weatherHistory.csv.csv")

# Show first 5 rows
print("Weather Data Preview:\n", df.head())

# Summary statistics
print("\nSummary Statistics:")
print(df.describe())

# Check column names for clarity
print("\nColumns in dataset:", df.columns)

# Plot temperature trends (adjust column names if different in your file)
if "MaxTemp" in df.columns and "MinTemp" in df.columns:
    plt.figure(figsize=(10, 5))
    plt.plot(df["Date"], df["MaxTemp"], label="Max Temp", color="red")
    plt.plot(df["Date"], df["MinTemp"], label="Min Temp", color="blue")
    plt.xlabel("Date")
    plt.ylabel("Temperature (°C)")
    plt.title("Daily Temperature Trends")
    plt.legend()
    plt.show()

# Plot precipitation if available
if "Precipitation" in df.columns:
    plt.figure(figsize=(8, 4))
    plt.bar(df["Date"], df["Precipitation"], color="skyblue")
    plt.xlabel("Date")
    plt.ylabel("Precipitation (mm)")
    plt.title("Daily Precipitation")
    plt.show()
