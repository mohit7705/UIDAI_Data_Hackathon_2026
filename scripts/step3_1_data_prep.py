import pandas as pd

# -----------------------------
# File paths (Linux-safe)
# -----------------------------
ENROLMENT_PATH = "data/raw/enrolment/BIHAR.csv"
UPDATE_PATH = "data/raw/demographic_updates/BIHAR.csv"

# -----------------------------
# Load datasets
# -----------------------------
df_enrol = pd.read_csv(ENROLMENT_PATH)
df_update = pd.read_csv(UPDATE_PATH)

# -----------------------------
# Basic structure check
# -----------------------------
print("ENROLMENT DATA")
print(df_enrol.head())
print(df_enrol.info())

print("\nUPDATE DATA")
print(df_update.head())
print(df_update.info())

# -----------------------------
# Date parsing
# -----------------------------
df_enrol["date"] = pd.to_datetime(df_enrol["date"], dayfirst=True)
df_update["date"] = pd.to_datetime(df_update["date"], dayfirst=True)

# -----------------------------
# Rename unclear column safely
# -----------------------------
if "demo_age_17_" in df_update.columns:
    df_update.rename(
        columns={"demo_age_17_": "demo_age_17_plus"},
        inplace=True
    )

# -----------------------------
# Save processed data
# -----------------------------
df_enrol.to_csv(
    "data/processed/enrolment_bihar_clean.csv", index=False
)
df_update.to_csv(
    "data/processed/demographic_updates_bihar_clean.csv", index=False
)

print("\nSTEP 3.1 COMPLETED SUCCESSFULLY")
