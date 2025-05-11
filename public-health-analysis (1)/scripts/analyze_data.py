# Triggering GitHub Actions test

import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("data/sample_data.csv")

# Basic summary
print("Summary of ART Regimen Line:")
print(df["CurrentRegimenLine"].value_counts())

# Visualization
plt.figure(figsize=(8, 5))
df["CurrentRegimenLine"].value_counts().plot(kind="bar")
plt.title("Current Regimen Line Distribution")
plt.ylabel("Count")
plt.xlabel("Regimen Line")
plt.tight_layout()
plt.savefig("data/regimen_distribution.png")
plt.show()
