# 01. Regression

Predict continuous numerical values using linear regression models. This is the **first step** in supervised learning.

---

## Notebooks

Follow this order:

| # | Topic | Notebook | Focus |
|---|---|---|---|
| 1 | [Simple Linear Regression](01_simple_linear_regression.ipynb) | `01_simple_linear_regression.ipynb` | Single feature, fitting a line, interpreting slope/intercept |
| 2 | [Multiple Linear Regression](02_multiple_linear_regression.ipynb) | `02_multiple_linear_regression.ipynb` | Multiple features, planes in higher dimensions, coefficients |
| 3 | [Regression from Scratch](03_regression_from_scratch.ipynb) | `03_regression_from_scratch.ipynb` | Implement OLS & Normal Equation from NumPy — understand the math |
| 4 | [Regression Metrics](04_regression_metrics.ipynb) | `04_regression_metrics.ipynb` | **Evaluation:** MAE, RMSE, R², adjusted R², residual plots |

---

## Why 4 Notebooks (No Duplication)?

Each notebook has a **specific focus** with minimal overlap:

- **01 & 02:** Building & fitting models (no metrics)
- **03:** Understanding the underlying math (from-scratch implementation)
- **04:** Comprehensive evaluation guide used by all models

This keeps each notebook focused and learnable in ~10-15 minutes, rather than one bloated notebook.

---

## Key Concepts

| Concept | Introduced In |
|---|---|
| Line fitting (y = mx + b) | Notebook 1 |
| Multiple features & planes | Notebook 2 |
| Normal Equation & OLS derivation | Notebook 3 |
| MAE, RMSE, R², Adjusted R² | Notebook 4 |
| Residual analysis & diagnostics | Notebook 4 |

---

## Data Files

| File | Used In | Description |
|---|---|---|
| `placement.csv` | Notebooks 1, 2 | CGPA → package prediction (real data) |
| (none) | Notebook 3 | Uses `load_diabetes` + synthetic data (built-in) |
| (none) | Notebook 4 | Uses `load_diabetes` (built-in) |

---

## Quick Start

```python
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# 1. Prepare data
X = df[['feature1', 'feature2']]
y = df['target']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 2. Fit model
lr = LinearRegression()
lr.fit(X_train, y_train)

# 3. Predict
y_pred = lr.predict(X_test)

# 4. Evaluate (see Notebook 04)
from sklearn.metrics import mean_absolute_error, r2_score
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
```

---

## Next Steps

👉 After completing this folder, move to **[02_logistic-regression](../02_logistic-regression/)**

---

## Video Resources

> *Links to recommended video tutorials will be added here.*
