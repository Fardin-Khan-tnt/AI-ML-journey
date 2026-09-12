# Scikit-learn

The most widely used machine learning library in Python.

Scikit-learn provides simple, efficient tools for data preprocessing, model training, evaluation, and tuning — all through a consistent `fit()` / `predict()` / `transform()` API.

> **Note:** These notes are a work in progress. More topics will be added over time.

---

## Notebook

📓 **[learn_scikit-learn.ipynb](learn_scikit-learn.ipynb)**

## Topics Covered

1. **Datasets** — built-in (`load_iris`, `load_breast_cancer`), downloadable (`fetch_california_housing`, `fetch_openml`), synthetic (`make_blobs`, `make_moons`)
2. **Train / Test Split** — `train_test_split`, `StratifiedShuffleSplit`
3. **Preprocessing: Scaling** — `StandardScaler`, `MinMaxScaler`
4. **Preprocessing: Encoding** — `OrdinalEncoder`, `OneHotEncoder`
5. **Classification** — KNN, Logistic Regression, Decision Tree, SVM, Random Forest, Naive Bayes
6. **Regression** — Linear, Ridge, Lasso, ElasticNet, KNN, Decision Tree, SVR, Random Forest
7. **Clustering** — KMeans, DBSCAN
8. **Dimensionality Reduction** — PCA on MNIST
9. **Metrics** — accuracy, precision, recall, F1, R², MAE, RMSE
10. **Cross Validation** — `cross_val_score`
11. **Hyperparameter Tuning** — `GridSearchCV`
12. **Pipeline** — chaining preprocessing and models

Ends with a **Cheat Sheet** for quick reference.

---

## Key Imports

```python
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
import numpy as np
import pandas as pd
```

---

## Core Concepts

| Concept | Description |
|---|---|
| **Features (`X`)** | Input data — 2D array (samples × features) |
| **Target (`y`)** | Labels/values to predict — 1D array |
| **Estimator** | Any object that learns from data |
| `fit()` | Train a model on data |
| `predict()` | Make predictions from a trained model |
| `transform()` | Apply a preprocessing step |
| `fit_transform()` | Fit + transform in one step (training data only) |
| `score()` | Accuracy (classifiers) or R² (regressors) |

---

## ML Workflow

```
1. Load data
2. Split into train / test
3. Preprocess (scale, encode)
4. Train a model (fit)
5. Evaluate (score, metrics)
6. Tune hyperparameters (GridSearchCV)
7. Use a Pipeline to avoid data leakage
```

---

## Video Resources

> *Links to recommended video tutorials will be added here.*
