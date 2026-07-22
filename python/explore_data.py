from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parent.parent
RAW_DATA_DIR = PROJECT_ROOT / "data" / "raw"

incident_file = RAW_DATA_DIR / "Incident_Management_CSV.csv"
support_file = RAW_DATA_DIR / "synthetic_it_support_tickets.csv"

incident_df = pd.read_csv(incident_file, sep=';')
support_df = pd.read_csv(support_file)

print("\nINCIDENT MANAGEMENT DATA")
print("-" * 50)
print("Rows and columns:", incident_df.shape)
print("\nColumn names:")
print(incident_df.columns.tolist())
print("\nFirst five rows:")
print(incident_df.head())
print("\nData types:")
print(incident_df.dtypes)
print("\nMissing values:")
print(incident_df.isna().sum().sort_values(ascending=False).head(20))

print("\n\nIT SUPPORT TICKET DATA")
print("-" * 50)
print("Rows and columns:", support_df.shape)
print("\nColumn names:")
print(support_df.columns.tolist())
print("\nFirst five rows:")
print(support_df.head())
print("\nData types:")
print(support_df.dtypes)
print("\nMissing values:")
print(support_df.isna().sum().sort_values(ascending=False).head(20))