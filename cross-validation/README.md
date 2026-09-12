# Cross Validation

Evaluate model performance more reliably by averaging scores across multiple train/test splits.

> 🚧 **Coming soon** — notebook will be added as I learn this topic.

---

## What You'll Learn

- Why a single train/test split is not enough
- K-Fold Cross Validation
- Stratified K-Fold (for imbalanced classes)
- `cross_val_score` and `cross_validate`
- Choosing the right number of folds

---

## Quick Preview

```python
from sklearn.model_selection import cross_val_score

scores = cross_val_score(model, X, y, cv=5)
scores.mean()
```

---

## Prerequisites

- [Scikit-learn basics](../basics/scikit-learn/)

---

## Video Resources

> *Links to recommended video tutorials will be added here.*
