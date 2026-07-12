# ⏰ Employee OverTime Prediction

##  Project Overview

This project predicts whether an employee is likely to work **OverTime** based on employee-related information such as age, job level, monthly income, work-life balance, job satisfaction, department, and years at the company.

The project follows a complete end-to-end Machine Learning workflow, including data preprocessing, exploratory data analysis, feature engineering, model comparison, hyperparameter tuning, model selection, and deployment using Streamlit.

---

##  Problem Statement

Employee overtime has a significant impact on productivity, employee well-being, and organizational performance. This project aims to build a machine learning model that predicts whether an employee is likely to work overtime based on historical employee data.

---

##  Dataset

* Employee OverTime Dataset
* Target Variable: **OverTime**

  * **0 → No OverTime**
  * **1 → Yes OverTime**

---

##  Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Scikit-learn
* Joblib
* Streamlit

---

## 📊 Machine Learning Workflow

* Data Cleaning
* Exploratory Data Analysis (EDA)
* Feature Engineering
* Train-Test Split
* Model Building
* Model Evaluation
* Hyperparameter Tuning
* Model Comparison
* Final Model Selection
* Streamlit Deployment

---

##  Models Evaluated

* Logistic Regression
* Decision Tree
* Random Forest
* Gradient Boosting
* XGBoost
* LightGBM
* CatBoost
* K-Nearest Neighbors (KNN)
* Support Vector Machine (SVM)
* Gaussian Naive Bayes (GNB)
* AdaBoost
* Extra Trees

---

## 🏆 Final Model

**Gaussian Naive Bayes (GNB)**

The final model was selected after comparing multiple machine learning algorithms using weighted evaluation metrics and ROC-AUC score.

---

##  Evaluation Metrics

The models were evaluated using:

* Accuracy
* Precision (Weighted)
* Recall (Weighted)
* F1-Score (Weighted)
* ROC-AUC Score

---

##  Streamlit Application Features

* Employee information input through sidebar
* Real-time OverTime prediction
* Prediction probability display
* Best model performance summary
* Model comparison table
* Selected employee scenario visualization

---

##  Project Structure

```text
Employee_OverTime_Prediction/
│
├── app.py
├── Employee_OverTime_Prediction.ipynb
├── employee_dataset.csv
├── gnb_final_model.pkl
├── feature_columns.pkl
├── requirements.txt
├── README.md
└── screenshots/
```



---

##  Application Preview

Add screenshots of the Streamlit application inside the **screenshots** folder and include them here.

---

##  Future Improvements

* Improve minority class prediction.
* Experiment with advanced ensemble techniques.
* Apply feature selection techniques.
* Improve model calibration.
* Deploy using Streamlit Community Cloud.

---

## 👨‍💻 Author

**Akhlaque Alam**

* Data Science Enthusiast
* Python | SQL | Machine Learning | Streamlit
* Open to Data Science and Machine Learning opportunities.
