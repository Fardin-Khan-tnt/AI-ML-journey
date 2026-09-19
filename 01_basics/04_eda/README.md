# Exploratory Data Analysis (EDA)

A practical walkthrough of the EDA process using a real-world roller coaster dataset.

EDA is the process of examining and visualizing a dataset to understand its structure, patterns, and relationships before building models or drawing conclusions.

---

## Notebook

📓 **[01_learn_eda.ipynb](01_learn_eda.ipynb)**

## Topics Covered

1. **Data Understanding** — `shape`, `head`, `tail`, `dtypes`, `describe`
2. **Data Preparation** — dropping columns, handling duplicates, renaming, type conversion
3. **Feature Understanding (Univariate)** — histograms, KDE, value counts
4. **Feature Relationships (Bivariate)** — scatter plots, correlation heatmaps, pair plots
5. **Asking Questions** — using groupby + aggregation + visualization to answer data questions

Ends with a **Cheat Sheet** for quick reference.

---

## Key Imports

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
```

---

## Files

| File | Description |
|---|---|
| `01_learn_eda.ipynb` | Main EDA tutorial notebook |
| `coaster_db.csv` | Roller coaster database (source dataset) |

---

## EDA Workflow

```
1. Load and inspect the data
2. Clean and prepare (drop, rename, fix types, deduplicate)
3. Explore individual features (distributions)
4. Explore relationships between features (scatter, correlation)
5. Ask and answer questions with groupby + plots
```

---

## Video Resources

- 📺 [Exploratory Data Analysis (EDA) Tutorial](https://youtu.be/xi0vhXFPegw?si=wkkcv7Zt3zpLIpBd)

<!-- Original tutorial from Medallion Data Science YouTube channel -->
