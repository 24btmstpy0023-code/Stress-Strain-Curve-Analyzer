# Stress-Strain Analyzer

A simple Streamlit-based application for analyzing tensile test data and calculating key mechanical properties of materials.

## Features

- Upload stress-strain data from a CSV file
- Plot the stress-strain curve
- Calculate Maximum Stress (UTS)
- Calculate Maximum Strain
- Calculate Resilience
- Calculate Toughness
- Display results in an interactive dashboard

## Libraries Used

- Streamlit
- Pandas
- NumPy
- Matplotlib
- SciPy

## Input Format

The uploaded CSV file must contain two columns:

```csv
Strain,Stress
0.0000,0
0.0005,100
0.0010,200
0.0015,300
0.0020,400
```

## Installation

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Applications

- Materials Science
- Mechanical Engineering
- Tensile Test Analysis
- Academic Projects
- Research and Development

## Author

Priyaranjan S
