# 03. Classification Metrics

Go beyond accuracy — understand how well your classifier really performs.

This is the **third step** — learn to properly evaluate classification models.

---

## Overview

Accuracy alone can be misleading, especially on imbalanced datasets. This section introduces the full toolkit for evaluating classifiers: the confusion matrix, precision, recall, F1, ROC-AUC, and the `average=` parameter for multiclass problems. You'll learn when each metric matters and how to choose the right one for your specific problem.

---

## What You'll Learn

- **Binary Classification**: Confusion matrix (TP, TN, FP, FN), precision, recall, F1-score, why accuracy is misleading
- **Multiclass Classification**: N×N confusion matrix, per-class metrics, and averaging strategies (macro, weighted, micro)
- **Threshold Tuning**: ROC curve and AUC — how metrics change as you adjust decision thresholds
- **Practical Skills**: Using `classification_report()` and choosing metrics based on problem constraints

---

## Notebooks

| Notebook | Topic | Time | Difficulty |
|----------|-------|------|------------|
| [01_binary_classification_metrics.ipynb](01_binary_classification_metrics.ipynb) | TP/TN/FP/FN, accuracy, precision, recall, F1, ROC/AUC | 1.5 hrs | Medium |
| [02_multiclass_classification_metrics.ipynb](02_multiclass_classification_metrics.ipynb) | N×N confusion matrix, averaging strategies (macro/weighted/micro) | 1 hr | Medium |

**Total:** ~2.5 hours

---

## Prerequisites

- [02_Logistic-Regression](../02_logistic-regression/)

---

## Why Separate from Algorithms?

These metrics apply to **all classifiers**: Logistic Regression, KNN, Decision Trees, Random Forest, SVM, Naive Bayes. By learning them here, you can evaluate any classifier you build later — they're general tools, not algorithm-specific.

**Applies To:**
- ✅ Logistic Regression
- ✅ KNN Classification
- ✅ Decision Tree Classification
- ✅ Random Forest Classification
- ✅ SVM Classification
- ✅ Naive Bayes

---

## Key Takeaways

| Concept | When It Matters |
|---------|-----------------|
| **Accuracy** | Balanced datasets only. Fails on imbalanced data. |
| **Precision** | When false positives are costly (e.g., spam detection — flag too much and users hate you) |
| **Recall** | When false negatives are costly (e.g., disease screening — missing a case is dangerous) |
| **F1** | When you care equally about both false positives and false negatives |
| **ROC-AUC** | When you want to evaluate a model across all thresholds, not just one |
| **Macro Average** | When all classes are equally important, regardless of sample count |
| **Weighted Average** | When you want metrics to reflect class imbalance in your test set |

---

## Next Steps

👉 After completing this, move to **[04_knn](../04_knn/)**

---

## Video Resources

- [StatQuest: Classification Metrics](https://youtu.be/c09drtuCS3c?si=YtJor8orMgow7_6o) — Comprehensive walkthrough of precision, recall, and F1
- [Confusion Matrix Explained](https://youtu.be/iK-kdhJ-7yI?si=vn5XKiMDADCVXhi3) — Visual breakdown of TP/TN/FP/FN
- [ROC Curve and AUC](https://youtu.be/pGPiRRfNsr0?si=xhIPV4DeyLXn4Tkw) — Understanding threshold trade-offs
