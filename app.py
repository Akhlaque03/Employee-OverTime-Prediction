import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import joblib


# PAGE CONFIG
st.set_page_config (
    page_title="Employee OverTime Prediction",
    page_icon="⏰",
    layout="wide"
)


# LOAD MODEL
model = joblib.load("gnb_final_model.pkl")
feature_columns = joblib.load("feature_columns.pkl")


# SIDEBAR INPUTS
st.sidebar.header("Employee Information")

age = st.sidebar.slider(
    "Age",
    22,
    60,
    37
)

job_level = st.sidebar.slider(
    "Job Level",
    1,
    5,
    2
)

years_at_company = st.sidebar.slider(
    "Years At Company",
    0,
    27,
    6
)

monthly_income = st.sidebar.number_input(
    "Monthly Income",
    min_value=3000.0,
    max_value=19644.75,
    value=8670.0
)

job_satisfaction = st.sidebar.selectbox(
    "Job Satisfaction",
    [1.5, 2., 3., 4., 5.]
)

work_life_balance = st.sidebar.selectbox(
    "Work Life Balance",
    [1, 2, 3, 4]
)

distance_from_home = st.sidebar.number_input(
    "Distance From Home",
    min_value=1.0,
    max_value=26.45,
    value=8.3
)

department = st.sidebar.selectbox(
    "Department",
    ["Finance", "HR", "IT", "Marketing", "Sales", "Operations"]
)


# PREDICT BUTTON
predict_button = st.sidebar.button("Predict OverTime")


# HEADER
st.title("⏰ Employee OverTime Prediction")
st.caption(
    "Predict employee overtime using employee information."
)


# Model Comprasion
comprasion_df = pd.DataFrame({
    "Model": [
        "Gaussian NB",
        "Gradient Boosting",
        "AdaBoost",
        "Random Forest",
        "CatBoost"
    ],
    "Accuracy": [
        0.7260,
        0.7255,
        0.7255,
        0.7255,
        0.7255
    ],
    "Precision": [
        0.7098,
        0.5264,
        0.5264,
        0.5264,
        0.5264
    ],
    "Recall": [
        0.7260,
        0.7255,
        0.7255,
        0.7255,
        0.7255
    ],
    "F1-Score": [
        0.6122,
        0.6101,
        0.6101,
        0.6101,
        0.6101
    ],
    "ROC-AUC": [
        0.6068,
        0.6010,
        0.5944,
        0.5934,
        0.5920
    ]
})




# DEFAULT VALUES
prediction_label = None
no_overtime_probability = None
yes_overtime_probability = None



# # TOP SECTION
# left, right = st.columns([1.2, 1])

# with left:

#     st.subheader("Prediction")



# PREDICTION
if predict_button:

    input_data = {
        "Age":age,
        "JobLevel":job_level,
        "YearsAtCompany":years_at_company,
        "MonthlyIncome": monthly_income,
        "JobSatisfaction":job_satisfaction,
        "WorkLifeBalance":work_life_balance,
        "DistanceFromHome":distance_from_home,

        "Department_Finance": 1 if department == "Finance" else 0,
        "Department_HR": 1 if department == "HR" else 0,
        "Department_IT": 1 if department == "IT" else 0,
        "Department_Marketing": 1 if department == "Marketing" else 0,
        "Department_Operations": 1 if department == "Operations" else 0,
        "Department_Sales": 1 if department == "Sales" else 0
    }

    input_df = pd.DataFrame([input_data])
    

    # MODEL PREDICTION & PROBABILITY
    prediction = model.predict(input_df)
    probability = model.predict_proba(input_df)

    # Convert Prediction to Label
    prediction_label = "Yes OverTime" if prediction[0] == 1 else "No OverTime"

    # Probability Calculation
    no_overtime_probability = probability[0][0] * 100
    yes_overtime_probability = probability[0][1] * 100



  # =========================
# TOP SECTION
# =========================

left, right = st.columns([1.2, 1])

with left:

    st.subheader("Prediction")

    if prediction_label is not None:

        st.success(
            prediction_label
        )

        st.subheader("Prediction Probability")

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "No OverTime",
                f"{no_overtime_probability:.2f}%"
            )

        with col2:
            st.metric(
                "Yes OverTime",
                f"{yes_overtime_probability:.2f}%"
            )

    else:

        st.info(
            "Fill employee details from sidebar and click Predict OverTime."
        )

with right:

    st.subheader("Deployed Model")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Best Model",
            "GNB"
        )

    with col2:
        st.metric(
            "Accuracy",
            "72.60%"
        )

    with col3:
        st.metric(
            "Precision",
            "70.98%"
        )


    col4, col5, col6 = st.columns(3)

    with col4:
        st.metric(
            "Recall",
            "72.60%"
        )
    with col5:
        st.metric(
            "F1-Score",
            "61.22%"
        )

    with col6:
        st.metric(
            "ROC-AUC",
            "60.68%"
        )

st.divider()



# Model Comprasion Table
st.subheader("Model Comprasion")

st.dataframe(
    comprasion_df.sort_values(
        by='ROC-AUC',
        ascending=False
    ),
    use_container_width=True
)


# SELECTED EMPLOYEE SCENARIO
scenario_df = pd.DataFrame({
    "Feature": [
        "Age",
        "Job Level",
        "Years At Company",
        "Monthly Income",
        "Job Satisfaction",
        "Work Life Balance",
        "Distance From Home",
        "Department"
    ],
 "Value": [
    str(age),
    str(job_level),
    str(years_at_company),
    str(monthly_income),
    str(job_satisfaction),
    str(work_life_balance),
    str(distance_from_home),
    department
]
})

st.dataframe(
    scenario_df,
    use_container_width=True
)
