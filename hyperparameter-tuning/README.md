# Hyperparameter Tuning

Find the best model settings automatically instead of guessing.

> 🚧 **Coming soon** — notebook will be added as I learn this topic.

---

## What You'll Learn

- What hyperparameters are (vs learned parameters)
- `GridSearchCV` — exhaustive search over a parameter grid
- `RandomizedSearchCV` — faster random sampling
- Defining parameter grids
- Reading `best_params_` and `best_estimator_`

---

## Quick Preview

```python
from sklearn.model_selection import GridSearchCV

param_grid = {'n_estimators': [50, 100, 200], 'max_depth': [None, 5, 10]}
grid = GridSearchCV(model, param_grid, cv=3)
grid.fit(X_train, y_train)

grid.best_params_
grid.best_estimator_.score(X_test, y_test)
```

---

## Prerequisites

- [Scikit-learn basics](../basics/scikit-learn/)
- [Cross Validation](../cross-validation/)

---

## Video Resources

> *Links to recommended video tutorials will be added here.*
