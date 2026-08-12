import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import simpson
from scipy.stats import linregress
st.title("Stress-Strain Analyzer - by Priyaranjan")
# Young's Modulus Input
#E = st.number_input(
    #"Enter Young's Modulus (MPa)")

offset = 0.002
# Upload CSV
file = st.file_uploader(
    "Upload CSV File",
    type=["csv"])


if file:
    df = pd.read_csv(file)
    strain = df["Strain"]
    stress = df["Stress"]
    best_r2 = 0
    best_E = 0
    best_points = 0

    for n in range(5, len(strain) + 1):

        result = linregress(strain[:n], stress[:n])

        r2 = result.rvalue**2

        if r2 > best_r2:
            best_r2 = r2
            best_E = result.slope
            best_points = n

        if r2 >= 0.999:
            break
    offset_stress = best_E * (strain - offset)
    offset_strain = strain - offset
    st.subheader("Results")

    st.write(f"**Young's Modulus:** {best_E:.2f} MPa")
    st.write(f"**Young's Modulus:** {best_E/1000:.2f} GPa")
    st.write(f"**UTS:** {uts:.2f} MPa")
    st.write(f"**Maximum Strain:** {max_strain:.4f}")
    st.write(f"**Resilience:** {resilience:.4f}")
    st.write(f"**Toughness:** {toughness:.4f}")
    st.write(f"**R²:** {best_r2:.6f}")
    st.write("### Uploaded Data")
    st.dataframe(df)
    # Plot Graph
    fig, ax = plt.subplots()
    ax.plot(strain, stress)
    ax.plot(offset_strain,offset_stress,linestyle = "dashed",color ="k",label="offset_line")
    ax.axhline(max(stress),linestyle="dashed",color = "red",label="UTS")
    ax.axvline(max(strain),linestyle="dashed",color = "green",label ="Max strain")
    ax.set_xlabel("Strain")
    ax.set_ylabel("Stress (MPa)")
    ax.set_title("Stress-Strain Curve")
    ax.grid(True)
    ax.legend()
    ax.set_ylim(0,max(stress)+10)
    st.pyplot(fig)
    from io import BytesIO
    img = BytesIO()
    fig.savefig(img, format="png")

    st.download_button(
    "Download PNG",
    img.getvalue(),
    "stress_strain_curve.png",
    "image/png")


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
