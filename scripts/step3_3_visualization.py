import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# Load aggregated tables
# -----------------------------
enrol_state = pd.read_csv(
    "outputs/tables/enrolment_state_date.csv",
    parse_dates=["date"]
)

update_state = pd.read_csv(
    "outputs/tables/update_state_date.csv",
    parse_dates=["date"]
)

# -----------------------------
# Plot 1: Enrolment over time
# -----------------------------
plt.figure(figsize=(10, 5))
plt.plot(enrol_state["date"], enrol_state["age_0_5"], label="Age 0–5")
plt.plot(enrol_state["date"], enrol_state["age_5_17"], label="Age 5–17")
plt.plot(enrol_state["date"], enrol_state["age_18_greater"], label="Age 18+")

plt.title("Aadhaar Enrolments Over Time (Bihar)")
plt.xlabel("Date")
plt.ylabel("Count")
plt.legend()
plt.tight_layout()

plt.savefig("outputs/figures/enrolment_state_time.png")
plt.close()

# -----------------------------
# Plot 2: Demographic updates
# -----------------------------
plt.figure(figsize=(10, 5))
plt.plot(update_state["date"], update_state["demo_age_5_17"], label="Age 5–17")
plt.plot(update_state["date"], update_state["demo_age_17_plus"], label="Age 17+")

plt.title("Aadhaar Demographic Updates Over Time (Bihar)")
plt.xlabel("Date")
plt.ylabel("Count")
plt.legend()
plt.tight_layout()

plt.savefig("outputs/figures/update_state_time.png")
plt.close()

print("STEP 3.3 COMPLETED SUCCESSFULLY")
