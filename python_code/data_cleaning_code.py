import pandas as pd

# Use raw string (r"") to avoid issues with backslashes
file_path = r"C:\Users\admin\Downloads\campaign_data_with_metrics.csv"

# Load CSV
df = pd.read_csv(file_path)

# Preview first rows
df.head()

# Calculate Click-Through Rate (CTR), Cost Per Click (CPC), and ROI
df["CTR"] = (df["clicks"] / df["impressions"]) * 100
df["CPC"] = df["spent"] / df["clicks"]
df["ROI"] = ((df["approved_conversion"] * 100) / df["spent"]).replace([float("inf"), -float("inf")], 0)

# Handle division by zero
df = df.fillna(0)

df.head()

output_file = r"C:\Users\admin\Downloads\campaign_data_with_metrics_updated.csv"
df.to_csv(output_file, index=False)

print(f"Updated file saved at: {output_file}")
