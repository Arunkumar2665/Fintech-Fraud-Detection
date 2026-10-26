# P2: Fintech Transaction Fraud Scoring & Customer Segmentation

## Objective
Demonstrate fraud classification using Decision Tree and Random Forest,
and customer segmentation using K-Means.

## Dataset
The transaction and customer datasets are synthetically generated for this
educational project. They are not real financial records and do not establish
real-world fraud-detection performance.

- Transactions: 12,000
- Customer profiles: 1,500
- Fraud rate in the generated transactions: approximately 5.67%

## Methods
1. Exploratory data analysis and class-imbalance review.
2. Decision Tree classification with class weighting and depth constraints.
3. Random Forest classification with class weighting and depth constraints.
4. Precision, recall, F1-score, accuracy and ROC-AUC evaluation.
5. Validation-based threshold selection for Random Forest.
6. Customer feature transformation and standardization.
7. K-Means clustering, with K evaluated from 2 through 8 using inertia
   and silhouette scores.
8. Customer segment profiling and dashboard generation.

## Selected results
- Decision Tree ROC-AUC: 0.6498
- Random Forest ROC-AUC at default threshold: 0.7460
- Tuned Random Forest ROC-AUC: 0.7545
- Selected clustering K: 2
- Highest observed silhouette score: 0.1602

The silhouette score is relatively low, indicating that the customer
clusters may overlap. Cluster labels are descriptive groups, not fraud labels.

## Key files
- `transactions.csv`: generated transaction data
- `customer_clusters.csv`: customer data and assigned cluster labels
- `customer_cluster_profiles.csv`: cluster-level summary
- `fraud_classification_comparison.csv`: model comparison matrix
- `customer_segmentation_dashboard.png`: customer dashboard
- `customer_dashboard.py`: reusable dashboard script
- `fraud_random_forest_model.joblib`: trained fraud model
- `customer_kmeans_model.joblib`: trained K-Means model
- `customer_feature_scaler.joblib`: feature scaler
- `project_config.json`: feature names and configuration

## Re-run the dashboard
Install dependencies:

```bash
pip install pandas matplotlib
```

Then run from the project directory:

```bash
python customer_dashboard.py --input customer_clusters.csv --output customer_segmentation_dashboard.png
```

## Limitations
- Synthetic data may not reflect real fraud patterns.
- The threshold depends on business costs and should be validated on
  representative, independently collected data.
- K-Means results depend on selected features and scaling.
- Model artifacts should only be used with the feature schema documented
  in the notebook and configuration.
