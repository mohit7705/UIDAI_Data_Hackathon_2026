import pandas as pd

# -----------------------------
# Load processed data
# -----------------------------
enrol_path = "data/processed/enrolment_bihar_clean.csv"
update_path = "data/processed/demographic_updates_bihar_clean.csv"

df_enrol = pd.read_csv(enrol_path, parse_dates=["date"])
df_update = pd.read_csv(update_path, parse_dates=["date"])

# -----------------------------
# ENROLMENT AGGREGATION
# -----------------------------

# District x Date
enrol_district_date = (
    df_enrol
    .groupby(["state", "district", "date"], as_index=False)
    .agg({
        "age_0_5": "sum",
        "age_5_17": "sum",
        "age_18_greater": "sum"
    })
)

# State x Date
enrol_state_date = (
    df_enrol
    .groupby(["state", "date"], as_index=False)
    .agg({
        "age_0_5": "sum",
        "age_5_17": "sum",
        "age_18_greater": "sum"
    })
)

# -----------------------------
# UPDATE AGGREGATION
# -----------------------------

# District x Date
update_district_date = (
    df_update
    .groupby(["state", "district", "date"], as_index=False)
    .agg({
        "demo_age_5_17": "sum",
        "demo_age_17_plus": "sum"
    })
)

# State x Date
update_state_date = (
    df_update
    .groupby(["state", "date"], as_index=False)
    .agg({
        "demo_age_5_17": "sum",
        "demo_age_17_plus": "sum"
    })
)

# -----------------------------
# Save aggregated tables
# -----------------------------
enrol_district_date.to_csv(
    "outputs/tables/enrolment_district_date.csv", index=False
)
enrol_state_date.to_csv(
    "outputs/tables/enrolment_state_date.csv", index=False
)
update_district_date.to_csv(
    "outputs/tables/update_district_date.csv", index=False
)
update_state_date.to_csv(
    "outputs/tables/update_state_date.csv", index=False
)

print("STEP 3.2 COMPLETED SUCCESSFULLY")
