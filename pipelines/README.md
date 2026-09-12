# Pipelines

Chain preprocessing steps and a model into one object to keep your workflow clean and avoid data leakage.

> 🚧 **Coming soon** — notebook will be added as I learn this topic.

---

## What You'll Learn

- Why pipelines prevent data leakage
- `Pipeline` — sequential chain of transformers + estimator
- `ColumnTransformer` — apply different preprocessing to different columns
- Combining pipelines with `GridSearchCV`
- `make_pipeline` shorthand

---

## Quick Preview

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier

pipe = Pipeline([
    ('scale',  StandardScaler()),
    ('forest', RandomForestClassifier()),
])

pipe.fit(X_train, y_train)
pipe.score(X_test, y_test)
```

---

## Prerequisites

- [Scikit-learn basics](../basics/scikit-learn/)

---

## Video Resources

> *Links to recommended video tutorials will be added here.*
