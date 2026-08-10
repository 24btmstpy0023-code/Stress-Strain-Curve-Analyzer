import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import simpson
st.title("Stress-Strain Analyzer - by Priyaranjan")
# Young's Modulus Input
E = st.number_input(
    "Enter Young's Modulus (MPa)",
    value=200000.0
)
offset = 0.002
# Upload CSV
file = st.file_uploader(
    "Upload CSV File",
    type=["csv"]
)

if file:
    df = pd.read_csv(file,header=None,names=["strain","stress"])
    strain = df["strain"]
    stress = df["stress"]
   # offset_stress = E*(strain - offset)
    st.write("### Uploaded Data")
    st.dataframe(df)
    # Plot Graph
    fig, ax = plt.subplots()
    ax.plot(strain, stress)
   # ax.plot(strain,offset_stress,linestyle = "dashed",color ="k",label="offset_line")
    ax.axhline(max(stress),linestyle="dashed",color = "red",label="UTS")
    ax.axvline(max(strain),linestyle="dashed",color = "green",label ="Max strain")
    ax.set_xlabel("Strain")
    ax.set_ylabel("Stress (MPa)")
    ax.set_title("Stress-Strain Curve")
    ax.grid(True)
    ax.legend()
    st.pyplot(fig)
    # Maximum Stress (UTS)
    max_stress = stress.max()
    # Maximum Strain
    max_strain = strain.max()
    # Resilience
    resilience = (max_stress**2) / (2 * E)
    # Toughness
    toughness = simpson(stress, x=strain)
    st.write("## Results")
    st.success(f"Maximum Stress (UTS): {max_stress:.2f} MPa")
    st.success(f"Maximum Strain: {max_strain:.6f}")
    st.success(f"Resilience: {resilience:.4f}")
    st.success(f"Toughness: {toughness:.4f}")
else:
    st.info("Upload a CSV file containing Strain and Stress columns.")
