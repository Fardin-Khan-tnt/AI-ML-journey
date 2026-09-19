# Pandas

**Panel Data** — the essential library for data manipulation and analysis in Python.

Pandas provides two main data structures: **Series** (1D) and **DataFrame** (2D). It handles CSV, Excel, SQL, JSON, and many other formats, making it the go-to tool for data cleaning, exploration, and transformation.

---

## Notebook

📓 **[01_learn_pandas.ipynb](01_learn_pandas.ipynb)**

## Topics Covered

1. **Series** — creating, accessing, filtering 1D labeled arrays
2. **DataFrame Basics** — creating from dicts, basic attributes, `describe()`
3. **Selecting Data** — column selection, `loc` vs `iloc`, `head`/`tail`
4. **Modifying DataFrames** — adding/updating columns, adding rows, dropping
5. **Reading Files** — `read_csv`, `read_excel`, `read_json`, `read_sql`
6. **Filtering Data** — conditions, `&`/`|` operators, `isin()`, `query()`
7. **Aggregation and Grouping** — `mean`, `sum`, `value_counts`, `groupby`
8. **Sorting** — `sort_values`, `sort_index`, multi-column sorting
9. **Data Cleaning** — missing values, duplicates, type casting, standardizing text
10. **String Operations** — `.str` accessor for vectorized string methods
11. **Merging and Joining** — `merge` (inner/left/outer), `concat`
12. **Apply and Map** — custom functions with `apply`, `map`, lambda
13. **Dates and Time Series** — `date_range`, `resample`, extracting components
14. **Pivot Tables** — reshaping and summarizing with `pivot_table`, `crosstab`
15. **Exporting Data** — `to_csv`, `to_excel`, `to_json`, `to_html`

Ends with a **Cheat Sheet** for quick reference.

---

## Key Imports

```python
import pandas as pd
import numpy as np
```

---

## Files

| File | Description |
|---|---|
| `01_learn_pandas.ipynb` | Main tutorial notebook |
| `data.csv` | Sample data file |

---

## Video Resources

- 📺 [Pandas Full Tutorial](https://youtu.be/VXtjG_GzO7Q?si=AXJ3qQ8aAxX4Rj0N)
- 📺 [Pandas Advanced Tutorial](https://youtu.be/gtjxAH8uaP0?si=MD3ndFks-iSYUsTx)
