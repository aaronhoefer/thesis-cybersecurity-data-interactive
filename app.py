import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load your cleaned data
df = pd.read_excel("data_cts_corruption_and_economic_crime.xlsx")  # or whatever file you save

# Rename columns based on the second row (index 1)
df.columns = df.iloc[1]
df = df[2:].reset_index(drop=True)

# Rename columns for easier reference
df.columns = ["Iso3_code", "Country", "Region", "Subregion", "Indicator",
              "Dimension", "Category", "Sex", "Age", "Year",
              "Unit", "Value", "Source"]

# Convert Year and Value columns to numeric types
df["Year"] = pd.to_numeric(df["Year"], errors="coerce")
df["Value"] = pd.to_numeric(df["Value"], errors="coerce")

# App title
st.title("Cybercrime Trends by Country")

# Country selector
country = st.selectbox("Select a country:", sorted(df["Country"].unique()))

# Filter by selected country
filtered = df[df["Country"] == country]

# Plot
fig, ax = plt.subplots()
filtered.groupby("Year")["Value"].sum().plot(ax=ax, marker="o")
ax.set_title(f"Cybercrime Trend in {country}")
ax.set_ylabel("Reported Cases")
ax.grid(True)
st.pyplot(fig)