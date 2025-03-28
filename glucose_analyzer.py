import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Load glucose data from CSV
def load_data(filename):
    df = pd.read_csv(filename)
    df['Time'] = pd.to_datetime(df['Time'])
    df = df.sort_values('Time')
    return df

# Analyze glucose trends
def analyze_trends(df):
    print("Basic Glucose Stats:")
    print(df['Glucose'].describe())
    print("\nHighest reading:", df['Glucose'].max())
    print("Lowest reading:", df['Glucose'].min())
    print("Standard deviation:", df['Glucose'].std())

# Plot glucose levels over time
def plot_glucose(df):
    plt.figure(figsize=(10,5))
    plt.plot(df['Time'], df['Glucose'], color='red', linewidth=2)
    plt.title("Glucose Levels Over Time")
    plt.xlabel("Time")
    plt.ylabel("Glucose (mmol/L)")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# Main execution
if __name__ == "__main__":
    file = "glucose_data.csv"  # Replace with your actual data file
    data = load_data(file)
    analyze_trends(data)
    plot_glucose(data)
