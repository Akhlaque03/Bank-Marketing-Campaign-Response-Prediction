import pandas as pd
import streamlit as st
import joblib


# Load model
final_model = joblib.load("final_model_cb_tuned.pkl")
feature_columns = joblib.load("Feature_columns.pkl")


# Page configuration
st.set_page_config(
    page_title="Bank Marketing Campaign Response Prediction",
    page_icon="💬",
    layout="wide"
)


# Side bar inputs
st.sidebar.header("Bank Marketing Campaign Response Prediction")

age = st.sidebar.slider(
    "Age",
    min_value=18.0,
    max_value=70.5,
    value=40.8,
    step=0.1
)

balance = st.sidebar.number_input(
    "Balance",
    min_value=-1962,
    max_value=3462,
    value=933,
    step=1
)

day = st.sidebar.slider(
    "Day",
    min_value=1,
    max_value=31,
    value=12,
    step=1
)

duration = st.sidebar.number_input(
    "Duration",
    min_value=0,
    max_value=643,
    value=235,
    step=1
)

campaign = st.sidebar.slider(
    "Campaign",
    min_value=1,
    max_value=6,
    value=3,
    step=1
)

job = st.sidebar.selectbox(
    "Job",
    options=['admin.', 'blue-collar', 'entrepreneur', 'housemaid', 'management', 'retired', 'self-employed',
             'services', 'student', 'technician', 'unemployed', 'unknown']    
)

marital = st.sidebar.selectbox(
    "Marital",
    options=['married', 'single']
)

education = st.sidebar.selectbox(
    "Education",
    options=['secondary', 'tertiary', 'unknown']
)


default = st.sidebar.radio(
    "Default",
    options=["no", "yes"]
)

housing = st.sidebar.radio(
    "Housing",
    options=["no", "yes"]
)

loan = st.sidebar.radio(
    "Loan",
    options=["no", "yes"]
)

contact = st.sidebar.selectbox(
    "Contact",
    options=['telephone', 'unknown']
)

month = st.sidebar.selectbox(
    "Month",
    options=['aug', 'dec', 'feb', 'jan', 'jul', 'jun',
             'mar', 'may', 'nov', 'oct', 'sep']
)

poutcome = st.sidebar.selectbox(
    "PoutCome",
    options=['other', 'success', 'unknown']
)

# Default value
prediction = None

# Prediction Button
predict_button = st.sidebar.button("Predict Response")

if predict_button:

    # Create input Data
    iinput_data = {
        "age":age,
        "balance":balance,
        "day":day,
        "duration":duration,
        "campaign":campaign,

        "job_blue-collar": 1 if job == 'blue-collar' else 0,
        "job_entrepreneur": 1 if job == 'entrepreneur' else 0,
        "job_housemaid": 1 if job == 'housemaid' else 0,
        "job_management": 1 if job == 'management' else 0,
        "job_retired": 1 if job == 'retired' else 0,
        "job_self-employed": 1 if job == 'self-employed' else 0,
        "job_services": 1 if job == 'services' else 0,
        "job_student": 1 if job == 'student' else 0,
        "job_technician": 1 if job == 'technician' else 0,
        "job_unemployed": 1 if job == 'unemployed' else 0,
        "job_unknown": 1 if job == "unknown" else 0,

        "marital_married": 1 if marital == "married" else 0,
        "marital_single": 1 if marital == "single" else 0,

        "education_secondary": 1 if education == 'secondary' else 0,
        "education_tertiary": 1 if education == 'tertiary' else 0,
        "education_unknown": 1 if education == 'unknown' else 0,

        "default_yes": 1 if default == "yes" else 0,
        "housing_yes": 1 if housing == "yes" else 0,
        "loan_yes": 1 if loan == "yes" else 0,

        "contact_telephone": 1 if contact == 'telephone' else 0,
        "contact_unknown": 1 if contact == 'unknown' else 0,

        "month_aug": 1 if month == "aug" else 0,
        "month_dec": 1 if month == 'dec' else 0,
        "month_feb": 1 if month == 'feb' else 0,
        "month_jan": 1 if month == 'jan' else 0,
        "month_jul": 1 if month == 'jul' else 0,
        "month_jun": 1 if month == 'jun' else 0,
        "month_mar": 1 if month == 'mar' else 0,
        "month_may": 1 if month == 'may' else 0,
        "month_nov": 1 if month == 'nov' else 0,
        "month_oct": 1 if month == 'oct' else 0,
        "month_sep": 1 if month == 'sep' else 0,

        "poutcome_other": 1 if poutcome == 'other' else 0,
        "poutcome_success": 1 if poutcome == 'success' else 0,
        "poutcome_unknown": 1 if poutcome == 'unknown' else 0
    }

    input_df = pd.DataFrame([iinput_data])

    # MODEL PREDICTION & PROBABILITY
    prediction = final_model.predict(input_df)
    probability = final_model.predict_proba(input_df)

    # Convert Prediction to Label
    prediction_label = "Yes" if prediction[0] == 1 else "No"

    # Probability Calculation
    no_response_probability = probability[0][0] * 100
    yes_response_probability = probability[0][1] * 100


# Header
st.title("💬 Bank Marketing Campaign Response Prediction")

st.caption("An end-to-end machine learning application for predicting customer response to targeted bank marketing campaigns.")


# Top Section
left, right = st.columns([1.2, 1])

with left:
    st.subheader("Prediction")

    if prediction is not None:

        if prediction_label == "Yes":
            st.success("🟢 YES — Customer Will Respond")
        else:
            st.error("🔴 NO — Customer Will Not Respond")

        st.warning("Model Used: CatBoost Tuned")

        st.subheader("Prediction Probability")

        col1, col2 = st.columns(2)

        with col1:
            st.warning(
                f"**No Response**  \n"
                f"### {no_response_probability:.2f}%"
            )

        with col2:
            st.info(
                f"**Yes Response**  \n"
                f"### {yes_response_probability:.2f}%"
            )

    else:
        st.info(
            "Fill customer details from the sidebar and click Predict Response."
        )

with right:

    st.subheader("Deployed Model")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Best Model",
            "CatBoost Tuned"
        )

    with col2:
        st.metric(
            "Accuracy",
            "86.10%"
        )

    with col3:
        st.metric(
            "Precision",
            "91.88%"
        )

    col4, col5, col6 = st.columns(3)

    with col4:
        st.metric(
            "Recall",
            "86.10%"
        )

    with col5:
        st.metric(
            "F1-Score",
            "87.82%"
        )

    with col6:
        st.metric(
            "ROC-AUC",
            "93.50%"
        )
st.divider()

# Selected Customer Response Scenario
st.subheader("Selected Customer Response Scenario")

scenario_df = pd.DataFrame({
    "Features": [
        "Age",
        "Balance",
        "Day",
        "Duration",
        "Campaign",
        "Job",
        "Marital",
        "Education",
        "Default",
        "Housing",
        "Loan",
        "Contact",
        "Month",
        "Poutcome"
    ],
    "Value": [
        age,
        balance,
        day,
        duration,
        campaign,
        job,
        marital,
        education,
        default,
        housing,
        loan,
        contact,
        month,
        poutcome
    ]
})

st.dataframe(
    scenario_df,
    use_container_width=True
)



# Baseline Model Comparison
comparison_df = pd.DataFrame({
    "Model": [
        "CatBoost",
        "LightGBM",
        "XGBoost",
        "Random Forest",
        "Gradient Boosting",
        "Logistic Regression",
        "SVC",
        "KNN",
        "GNB",
        "Decision Tree"
    ],
    "Accuracy": [
        0.9067,
        0.9057,
        0.9045,
        0.9018,
        0.9007,
        0.8972,
        0.9026,
        0.8911,
        0.8639,
        0.8737
    ],
    "Precision": [
        0.8977,
        0.8970,
        0.8962,
        0.8890,
        0.8874,
        0.8816,
        0.8892,
        0.8739,
        0.8618,
        0.8746
    ],
    "Recall": [
        0.9067,
        0.9057,
        0.9045,
        0.9018,
        0.9007,
        0.8972,
        0.9026,
        0.8911,
        0.8639,
        0.8737
    ],
    "F1-Score": [
        0.9003,
        0.8997,
        0.8990,
        0.8909,
        0.8894,
        0.8831,
        0.8889,
        0.8775,
        0.8628,
        0.8742
    ],
    "Log Loss": [
        0.2009,
        0.2019,
        0.2120,
        0.2464,
        0.2187,
        0.2361,
        0.2493,
        0.9804,
        1.6535,
        4.5518
    ],
    "ROC-AUC": [
        0.9341,
        0.9317,
        0.9268,
        0.9212,
        0.9212,
        0.9048,
        0.9005,
        0.8396,
        0.8167,
        0.7060
    ],
    "PR-AUC": [
        0.6336,
        0.6335,
        0.6123,
        0.6090,
        0.5999,
        0.5645,
        0.5997,
        0.4425,
        0.3922,
        0.2934
    ]
})

comparison_df = comparison_df.sort_values(
    by="ROC-AUC",
    ascending=False
).reset_index(drop=True)

st.subheader("Baseline Model Performance Comparison")

st.dataframe(
    comparison_df,
    use_container_width=True,
    hide_index=True
)


# Baseline Model Performance Visualization
import matplotlib.pyplot as plt

plot_df = comparison_df.copy()

# Convert ROC-AUC to numeric only for visualization
plot_df["ROC-AUC"] = plot_df["ROC-AUC"].astype(float)

# Sort: Highest → Lowest
plot_df = plot_df.sort_values(
    by="ROC-AUC",
    ascending=False
).reset_index(drop=True)

fig, ax = plt.subplots(figsize=(13, 7))

colors = ['#4338CA'] * len(plot_df)
colors[0] = '#0F766E'

bars = ax.bar(
    plot_df["Model"],
    plot_df["ROC-AUC"],
    color=colors,
    edgecolor='#111827',
    linewidth=1.2,
    width=0.72
)

ax.set_title(
    "Classification Model Performance Comparison (ROC-AUC)",
    fontsize=18,
    fontweight='bold',
    color='#111827',
    pad=20
)

ax.text(
    0.5, 1.02,
    "Higher ROC-AUC indicates better predictive performance",
    transform=ax.transAxes,
    ha='center',
    fontsize=12,
    color='#64748B',
    style='italic'
)

ax.set_xlabel(
    "Machine Learning Model",
    fontsize=12,
    fontweight='bold'
)

ax.set_ylabel(
    "ROC-AUC",
    fontsize=12,
    fontweight='bold'
)

ax.grid(
    axis='y',
    linestyle='--',
    linewidth=0.8,
    alpha=0.25
)

ax.set_axisbelow(True)

ax.tick_params(
    axis='x',
    rotation=30,
    labelsize=10
)

ax.tick_params(
    axis='y',
    labelsize=10
)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

for bar in bars:
    height = bar.get_height()

    ax.text(
        bar.get_x() + bar.get_width() / 2,
        height + 0.003,
        f"{height:.3f}",
        ha='center',
        fontsize=10,
        fontweight='bold',
        color='#475569'
    )

fig.tight_layout()

st.pyplot(fig)

plt.close(fig)



# Final Model Comparison After Hyperparameter Tuning
comparison_tuned_df = pd.DataFrame({
    "Model": [
        "CatBoost Tuned",
        "CatBoost Original",
        "XGBoost Tuned",
        "LightGBM Tuned",
        "LightGBM Original",
        "XGBoost Original"
    ],
    "Accuracy": [
        0.8610,
        0.9067,
        0.8660,
        0.8527,
        0.9057,
        0.9045
    ],
    "Precision": [
        0.9188,
        0.8977,
        0.9174,
        0.9167,
        0.8970,
        0.8962
    ],
    "Recall": [
        0.8610,
        0.9067,
        0.8660,
        0.8527,
        0.9057,
        0.9045
    ],
    "F1-Score": [
        0.8782,
        0.9003,
        0.8817,
        0.8717,
        0.8997,
        0.8990
    ],
    "Log Loss": [
        0.3173,
        0.2009,
        0.2984,
        0.3259,
        0.2019,
        0.2120
    ],
    "ROC-AUC": [
        0.9350,
        0.9341,
        0.9338,
        0.9322,
        0.9317,
        0.9268
    ],
    "PR-AUC": [
        0.6397,
        0.6336,
        0.6385,
        0.6306,
        0.6335,
        0.6123
    ]
})

comparison_tuned_df = comparison_tuned_df.sort_values(
    by="ROC-AUC",
    ascending=False
).reset_index(drop=True)

st.subheader("Original vs Tuned Model Performance Comparison")

st.dataframe(
    comparison_tuned_df,
    use_container_width=True,
    hide_index=True
)



# Final Model Performance Visualization
import matplotlib.pyplot as plt

plot_df = comparison_tuned_df.copy()

# Ensure ROC-AUC is numeric
plot_df["ROC-AUC"] = plot_df["ROC-AUC"].astype(float)

# Sort: Highest → Lowest
plot_df = plot_df.sort_values(
    by="ROC-AUC",
    ascending=False
).reset_index(drop=True)

fig, ax = plt.subplots(figsize=(13, 7))

# Colors
colors = ['#4338CA'] * len(plot_df)
colors[0] = '#0F766E'  # Best model

bars = ax.bar(
    plot_df["Model"],
    plot_df["ROC-AUC"],
    color=colors,
    edgecolor='#111827',
    linewidth=1.2,
    width=0.72
)

# Title
ax.set_title(
    "Final Model Performance Comparison (ROC-AUC)",
    fontsize=18,
    fontweight='bold',
    color='#111827',
    pad=20
)

# Subtitle
ax.text(
    0.5,
    1.02,
    "Higher ROC-AUC indicates stronger classification performance",
    transform=ax.transAxes,
    ha='center',
    fontsize=11,
    color='#64748B',
    style='italic'
)

# Axis Labels
ax.set_xlabel(
    "Machine Learning Model",
    fontsize=12,
    fontweight='bold',
    color='#374151',
    labelpad=10
)

ax.set_ylabel(
    "ROC-AUC Score",
    fontsize=12,
    fontweight='bold',
    color='#374151',
    labelpad=10
)

# X-axis
ax.set_xticks(range(len(plot_df)))

ax.set_xticklabels(
    plot_df["Model"],
    rotation=30,
    ha='right',
    fontsize=10.5,
    fontweight='bold'
)

# Y-axis
ax.tick_params(
    axis='y',
    labelsize=10
)

# Grid
ax.grid(
    axis='y',
    linestyle='--',
    alpha=0.22,
    linewidth=0.7
)

ax.set_axisbelow(True)

# Remove unnecessary borders
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

ax.spines['left'].set_linewidth(1.1)
ax.spines['bottom'].set_linewidth(1.1)

# Value labels
for bar in bars:
    height = bar.get_height()

    ax.text(
        bar.get_x() + bar.get_width() / 2,
        height + 0.003,
        f"{height:.3f}",
        ha='center',
        va='bottom',
        fontsize=10,
        fontweight='bold',
        color='#475569'
    )

fig.tight_layout()

st.pyplot(fig)

plt.close(fig)




# Feature Importance Table
feature_importance_df = pd.DataFrame({
    "Feature": [
        "duration",
        "contact_unknown",
        "day",
        "poutcome_success",
        "month_may",
        "housing_yes",
        "age",
        "balance",
        "poutcome_unknown",
        "month_jul"
    ],
    "Importance": [
        30.014453,
        9.764939,
        8.833413,
        5.591781,
        4.304850,
        4.004956,
        3.964837,
        3.754881,
        3.398896,
        3.186803
    ]
})

st.subheader("Top 10 Feature Importance")

st.dataframe(
    feature_importance_df,
    use_container_width=True,
    hide_index=True
)



# Top 10 Feature Importance Visualization
import matplotlib.pyplot as plt

top_10 = (
    feature_importance_df
    .sort_values(
        by="Importance",
        ascending=True
    )
)

fig, ax = plt.subplots(figsize=(13, 7))

bars = ax.barh(
    top_10["Feature"],
    top_10["Importance"],
    color="#0891B2",
    edgecolor="#164E63",
    linewidth=1.2,
    height=0.68
)

# Title
ax.set_title(
    "Top 10 Feature Importance Analysis",
    fontsize=18,
    fontweight="bold",
    color="#111827",
    pad=20
)

# Subtitle
ax.text(
    0.5,
    1.02,
    "Higher importance indicates greater contribution to model predictions",
    transform=ax.transAxes,
    ha="center",
    fontsize=11,
    color="#64748B",
    style="italic"
)

# Axis Labels
ax.set_xlabel(
    "Importance",
    fontsize=12,
    fontweight="bold",
    color="#374151"
)

ax.set_ylabel(
    "Feature",
    fontsize=12,
    fontweight="bold",
    color="#374151"
)

# Grid
ax.grid(
    axis="x",
    linestyle="--",
    linewidth=0.7,
    alpha=0.22
)

ax.set_axisbelow(True)

# Tick Labels
ax.tick_params(
    axis="x",
    labelsize=10
)

ax.tick_params(
    axis="y",
    labelsize=10.5
)

# Remove unnecessary borders
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

ax.spines["left"].set_linewidth(1.1)
ax.spines["bottom"].set_linewidth(1.1)

# Value Labels
for bar in bars:

    width = bar.get_width()

    ax.text(
        width + 0.3,
        bar.get_y() + bar.get_height() / 2,
        f"{width:.3f}",
        ha="left",
        va="center",
        fontsize=10,
        fontweight="bold",
        color="#334155"
    )

fig.tight_layout()

st.pyplot(fig)

plt.close(fig)