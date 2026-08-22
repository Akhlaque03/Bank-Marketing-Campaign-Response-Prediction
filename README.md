# 🏦 Bank Marketing Campaign Response Prediction

[![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python\&logoColor=white)](https://www.python.org/)
[![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Classification-orange)](https://scikit-learn.org/)
[![CatBoost](https://img.shields.io/badge/Model-CatBoost-6DB33F)](https://catboost.ai/)
[![Scikit-learn](https://img.shields.io/badge/Scikit--learn-F7931E?logo=scikit-learn\&logoColor=white)](https://scikit-learn.org/)
[![Streamlit](https://img.shields.io/badge/Deployment-Streamlit-red?logo=streamlit\&logoColor=white)](https://streamlit.io/)

> An end-to-end machine learning classification project that predicts customer response to bank marketing campaigns using multiple classification algorithms, hyperparameter tuning, and an interactive Streamlit application.

**Best Model:** CatBoost Tuned  
**ROC-AUC:** 0.9350  
**PR-AUC:** 0.6397  
**Deployment:** Streamlit Community Cloud

🚀 **Live Demo:**
https://akhlaque03-bank-marketing-campaign-response-prediction.streamlit.app/

---

## What This Project Does

This project predicts whether a customer is likely to respond positively to a targeted bank marketing campaign.

The workflow compares multiple classification algorithms, identifies strong baseline performers, applies hyperparameter tuning to selected boosting models, and deploys the final model through an interactive Streamlit application.

---

### Key Highlights

- **10 classification models** evaluated using a consistent evaluation framework
- **CatBoost, XGBoost, and LightGBM** optimized through hyperparameter tuning
- **CatBoost Tuned** selected as the final production model
- **ROC-AUC: 0.9350** and **PR-AUC: 0.6397**
- Probability-based predictions for **Yes / No** responses
- Feature importance analysis for model interpretability
- Interactive **Streamlit** prediction application
- Public cloud deployment through **Streamlit Community Cloud**

---

## Project Overview

Bank marketing campaigns involve large numbers of customer interactions, making it important to identify customers who are more likely to respond positively.

This project develops an end-to-end **binary classification system** to predict customer response to targeted bank marketing campaigns.

### Machine Learning Workflow

**Data → Preprocessing → EDA → Encoding → Model Training → Baseline Comparison → Hyperparameter Tuning → Model Evaluation → Feature Importance → Deployment**

The project covers:

- Data preprocessing and quality checks
- Exploratory Data Analysis (EDA)
- Categorical feature encoding
- Training and evaluation of multiple classification models
- Baseline model comparison using ROC-AUC
- Hyperparameter tuning of CatBoost, XGBoost, and LightGBM
- Original vs. tuned model comparison
- Feature importance analysis
- Final model selection
- Interactive customer response prediction
- Streamlit deployment

### Prediction Output

The deployed application provides:

- **Predicted Response:** `Yes` / `No`
- **No Response Probability**
- **Yes Response Probability**
- **Final Model:** CatBoost Tuned

---

## Business Value

The goal of this project is to support **data-driven customer targeting** by estimating which customers are more likely to respond positively to a marketing campaign.

Instead of treating every customer equally, the model can help marketing teams prioritize customers based on their predicted response probability.

### Potential Business Applications

- **Customer Prioritization** — focus outreach on customers with higher predicted response probability
- **Campaign Optimization** — support more targeted marketing strategies
- **Resource Allocation** — reduce unnecessary outreach and improve use of marketing resources
- **Customer Insights** — identify patterns associated with campaign response
- **Probability-Based Decision Making** — use model confidence to support campaign-level decisions

> **Important:** The model provides predictive insights rather than causal conclusions. Real-world deployment should consider campaign costs, business rules, customer consent, and operational constraints.

---

## Project Objectives

The project was designed to build, evaluate, and deploy a reliable machine learning solution for predicting customer responses to bank marketing campaigns.

### Key Objectives

- Develop a binary classification model for customer response prediction.
- Perform data quality checks, preprocessing, and exploratory analysis.
- Prepare categorical and numerical features for model training.
- Evaluate multiple classification algorithms using consistent metrics.
- Identify the strongest baseline model using ROC-AUC.
- Optimize selected boosting models through hyperparameter tuning.
- Compare original and tuned model performance across multiple metrics.
- Analyze feature importance to understand the model's predictive signals.
- Select and serialize the final production model.
- Build an interactive Streamlit prediction application.
- Provide probability-based predictions for better decision support.
- Deploy the application through Streamlit Community Cloud.

---

## Dataset Information

The project uses the **Bank Marketing dataset**, which contains customer demographic information, financial attributes, campaign interaction details, and previous campaign outcomes.

The dataset is used to identify patterns associated with customer responses and train a binary classification model.

### Input Feature Categories

| Category | Features |
|---|---|
| **Customer Profile** | Age, Job, Marital Status, Education |
| **Financial Information** | Balance, Default, Housing Loan, Personal Loan |
| **Campaign Information** | Day, Month, Contact, Campaign, Duration |
| **Previous Campaign History** | Previous Campaign Outcome |

### Features Used by the Model

**Numerical Features**
- `age`
- `balance`
- `day`
- `duration`
- `campaign`

**Categorical Features**
- `job`
- `marital`
- `education`
- `default`
- `housing`
- `loan`
- `contact`
- `month`
- `poutcome`

### Target Variable

**Customer Response**

- `Yes` → Customer responded positively
- `No` → Customer did not respond

The target variable represents a **binary classification problem**.

---

## Feature Availability Consideration

The feature `duration` was identified as the strongest predictive feature in the final model.

However, `duration` represents the length of the customer interaction and is only known during or after the contact. Therefore, it would not be available when deciding **which customers to contact before a campaign begins**.

This creates an important distinction between:

- **Post-contact prediction** — uses interaction information such as `duration`.
- **Pre-campaign targeting** — should exclude variables that are only available after or during the customer interaction.

For a production-ready **pre-campaign targeting system**, the model should be retrained without post-contact variables such as `duration`.

> **Key takeaway:** The current model demonstrates strong predictive performance, but its feature availability should be considered carefully before applying it to real-world pre-campaign customer targeting.
---

## Data Preprocessing & Feature Engineering

The dataset was prepared through a structured preprocessing workflow to ensure consistent and reliable model training.

### Preprocessing Workflow

**Data Quality → Feature Analysis → Encoding → Feature Alignment → Model-Ready Data**

### Data Quality & Preparation

- Checked for missing values and inconsistent entries.
- Reviewed duplicate records and overall data quality.
- Analyzed numerical and categorical variables.
- Examined feature distributions and relationships with the target.
- Prepared the dataset for classification model training.

### Categorical Encoding

Categorical variables were converted into numerical representations using **One-Hot Encoding**.

Examples of generated features include:

- `job_blue-collar`
- `job_management`
- `marital_married`
- `education_tertiary`
- `housing_yes`
- `contact_unknown`
- `month_may`
- `poutcome_success`

### Feature Alignment

The deployed application uses the same feature structure expected by the trained model.

A saved feature-column configuration ensures that transformed user inputs remain aligned with the feature structure used during training.

This maintains consistency across the complete inference workflow:

**Training → Preprocessing → Feature Alignment → Production Inference**

---

## Exploratory Data Analysis

Exploratory Data Analysis (EDA) was performed to understand customer characteristics, campaign behavior, feature distributions, and patterns associated with customer response.

### Analysis Performed

- **Univariate Analysis** — examined distributions of numerical and categorical variables.
- **Bivariate Analysis** — analyzed relationships between individual features and customer response.
- **Multivariate Analysis** — investigated interactions among multiple variables.
- **Categorical Analysis** — examined response patterns across job, education, contact, housing, loan, month, and previous campaign outcome.
- **Numerical Analysis** — analyzed age, balance, duration, day, and campaign-related variables.
- **Correlation Analysis** — evaluated relationships among numerical features.
- **Feature Importance Analysis** — examined the strongest predictive signals captured by the final model.

### Key EDA Insights

The analysis highlighted several variables with strong predictive signals, including:

- `duration`
- `contact_unknown`
- `day`
- `poutcome_success`
- `month_may`

These patterns were further evaluated during model training and feature importance analysis.

> **Important:** Feature importance reflects how strongly a variable contributes to model predictions. It does not establish a causal relationship with customer response.

---

## Machine Learning Models Evaluated

Multiple classification algorithms were trained and evaluated using a consistent evaluation framework to establish baseline performance and identify suitable candidates for optimization.

### Baseline Models

| Model | Type |
|---|---|
| Logistic Regression | Linear Classifier |
| K-Nearest Neighbors (KNN) | Distance-Based Classifier |
| Support Vector Classifier (SVC) | Margin-Based Classifier |
| Gaussian Naive Bayes (GNB) | Probabilistic Classifier |
| Decision Tree Classifier | Tree-Based Classifier |
| Random Forest Classifier | Ensemble Tree Model |
| Gradient Boosting Classifier | Boosting Model |
| XGBoost Classifier | Gradient Boosting |
| LightGBM Classifier | Gradient Boosting |
| CatBoost Classifier | Gradient Boosting |

The baseline comparison was used to identify the strongest-performing models for further hyperparameter optimization.

---

## Evaluation Metrics

The classification models were evaluated using multiple complementary metrics to assess both prediction quality and probability performance.

| Metric | Purpose |
|---|---|
| **Accuracy** | Measures the overall proportion of correct predictions |
| **Precision** | Measures how many predicted positive responses were actually positive |
| **Recall** | Measures how many actual positive responses were correctly identified |
| **F1-Score** | Balances precision and recall using their harmonic mean |
| **Log Loss** | Evaluates the quality and confidence of predicted probabilities |
| **ROC-AUC** | Measures the model's ability to distinguish between positive and negative classes across thresholds |
| **PR-AUC** | Evaluates precision-recall performance, particularly for the positive class |

### Primary Model Selection Metric

**ROC-AUC** was selected as the primary ranking metric because the project focuses on distinguishing customers who are likely to respond positively from those who are not across different classification thresholds.

Other metrics were considered alongside ROC-AUC to provide a broader view of model performance, including precision, recall, F1-score, probability quality, and positive-class performance.

---

## Baseline Model Comparison

All baseline classification models were evaluated using the same dataset split and evaluation framework to ensure a consistent comparison.

**ROC-AUC** was selected as the primary model-selection metric because it measures how effectively a classifier separates positive and negative responses across different decision thresholds.

### Baseline Performance

| Model | Accuracy | Precision | Recall | F1-Score | Log Loss | ROC-AUC | PR-AUC |
|---|---:|---:|---:|---:|---:|---:|---:|
| **CatBoost** | 0.9067 | 0.8977 | 0.9067 | 0.9003 | 0.2009 | **0.9341** | 0.6336 |
| LightGBM | 0.9057 | 0.8970 | 0.9057 | 0.8997 | 0.2019 | 0.9317 | 0.6335 |
| XGBoost | 0.9045 | 0.8962 | 0.9045 | 0.8990 | 0.2120 | 0.9268 | 0.6123 |
| Random Forest | 0.9018 | 0.8890 | 0.9018 | 0.8909 | 0.2464 | 0.9212 | 0.6090 |
| Gradient Boosting | 0.9007 | 0.8874 | 0.9007 | 0.8894 | 0.2187 | 0.9212 | 0.5999 |
| Logistic Regression | 0.8972 | 0.8816 | 0.8972 | 0.8831 | 0.2361 | 0.9048 | 0.5645 |
| SVC | 0.9026 | 0.8892 | 0.9026 | 0.8889 | 0.2493 | 0.9005 | 0.5997 |
| KNN | 0.8911 | 0.8739 | 0.8911 | 0.8775 | 0.9804 | 0.8396 | 0.4425 |
| GNB | 0.8639 | 0.8618 | 0.8639 | 0.8628 | 1.6535 | 0.8167 | 0.3922 |
| Decision Tree | 0.8737 | 0.8746 | 0.8737 | 0.8742 | 4.5518 | 0.7060 | 0.2934 |

### Baseline Result

**CatBoost achieved the highest baseline ROC-AUC of 0.9341**, followed by LightGBM at 0.9317 and XGBoost at 0.9268.

Based on the primary ranking metric, CatBoost was the strongest baseline model.

The baseline results were then used to identify **CatBoost, XGBoost, and LightGBM** as candidates for hyperparameter optimization.

---

## Hyperparameter Tuning

After baseline evaluation, hyperparameter tuning was performed on the strongest boosting candidates to determine whether optimized configurations could improve model performance.

### Models Tuned

- **CatBoost Classifier**
- **XGBoost Classifier**
- **LightGBM Classifier**

### Tuning Objective

The selected models were optimized and then compared with their corresponding original versions using the same evaluation framework.

The comparison included:

- Accuracy
- Precision
- Recall
- F1-Score
- Log Loss
- ROC-AUC
- PR-AUC

**ROC-AUC remained the primary ranking metric** throughout the tuning and model-selection process.

### Model Selection Approach

The tuned models were not selected based on a single metric in isolation. Their performance was evaluated across multiple metrics to understand the trade-offs between classification performance and probability quality.

The final production model was selected based on the project's primary ranking criterion, **ROC-AUC**, together with its overall performance profile.

---

## Original vs. Tuned Model Comparison

Hyperparameter tuning was evaluated by comparing each optimized model with its corresponding original version.

This comparison helps determine whether tuning improved the primary model-selection metric while also showing the impact on other classification and probability-based metrics.

### Comparison Results

| Model | Accuracy | Precision | Recall | F1-Score | Log Loss | ROC-AUC | PR-AUC |
|---|---:|---:|---:|---:|---:|---:|---:|
| **CatBoost Tuned** | 0.8610 | **0.9188** | 0.8610 | 0.8782 | 0.3173 | **0.9350** | **0.6397** |
| CatBoost Original | 0.9067 | 0.8977 | 0.9067 | **0.9003** | **0.2009** | 0.9341 | 0.6336 |
| XGBoost Tuned | 0.8660 | 0.9174 | 0.8660 | 0.8817 | 0.2984 | 0.9338 | 0.6385 |
| LightGBM Tuned | 0.8527 | 0.9167 | 0.8527 | 0.8717 | 0.3259 | 0.9322 | 0.6306 |
| LightGBM Original | 0.9057 | 0.8970 | 0.9057 | 0.8997 | 0.2019 | 0.9317 | 0.6335 |
| XGBoost Original | 0.9045 | 0.8962 | 0.9045 | 0.8990 | 0.2120 | 0.9268 | 0.6123 |

### Key Finding

**CatBoost Tuned achieved the highest ROC-AUC of 0.9350 and PR-AUC of 0.6397** among the compared models.

However, tuning introduced trade-offs compared with CatBoost Original:

| Metric | CatBoost Original | CatBoost Tuned | Change |
|---|---:|---:|---:|
| Accuracy | 0.9067 | 0.8610 | Decreased |
| Precision | 0.8977 | **0.9188** | Increased |
| Recall | 0.9067 | 0.8610 | Decreased |
| F1-Score | **0.9003** | 0.8782 | Decreased |
| Log Loss | **0.2009** | 0.3173 | Increased |
| ROC-AUC | 0.9341 | **0.9350** | Increased |
| PR-AUC | 0.6336 | **0.6397** | Increased |

The tuned CatBoost model therefore provided a small improvement in **ROC-AUC and PR-AUC**, while sacrificing some threshold-dependent classification metrics and probability quality.

Based on the project's primary selection criterion, **CatBoost Tuned was selected as the final production model**.

---

## Final Model Selection

Based on the comparative evaluation, **CatBoost Tuned** was selected as the final production model.

### Final Model Performance

| Metric | Score |
|---|---:|
| Accuracy | 0.8610 |
| Precision | **0.9188** |
| Recall | 0.8610 |
| F1-Score | 0.8782 |
| Log Loss | 0.3173 |
| ROC-AUC | **0.9350** |
| PR-AUC | **0.6397** |

### Why CatBoost Tuned?

CatBoost Tuned was selected primarily because it achieved the project's strongest ranking performance:

- **Highest ROC-AUC:** 0.9350
- **Highest PR-AUC:** 0.6397
- **Highest Precision:** 0.9188

The model achieved a small improvement in ROC-AUC over CatBoost Original:

**0.9341 → 0.9350**

Although some threshold-dependent metrics decreased after tuning, the tuned model remained the strongest according to the project's primary selection criterion, **ROC-AUC**.

The final trained model was serialized and integrated into the Streamlit application for production inference.

---

## Feature Importance Analysis

Feature importance analysis was performed using the final **CatBoost Tuned** model to identify the variables that contributed most strongly to its predictions.

### Top 10 Important Features

| Rank | Feature | Importance |
|---:|---|---:|
| 1 | `duration` | 30.014453 |
| 2 | `contact_unknown` | 9.764939 |
| 3 | `day` | 8.833413 |
| 4 | `poutcome_success` | 5.591781 |
| 5 | `month_may` | 4.304850 |
| 6 | `housing_yes` | 4.004956 |
| 7 | `age` | 3.964837 |
| 8 | `balance` | 3.754881 |
| 9 | `poutcome_unknown` | 3.398896 |
| 10 | `month_jul` | 3.186803 |

### Key Insight

The feature importance analysis shows that **`duration`** was the strongest predictive feature, with substantially higher importance than the other features.

Other influential signals included:

- Contact type
- Day of contact
- Previous campaign outcome
- Campaign month
- Housing status
- Age
- Account balance

These results help explain which variables the model relied on most strongly when generating predictions.

> **Important:** Feature importance measures a feature's contribution to model predictions. It does not establish a causal relationship between the feature and customer response.

---

## 💻 Streamlit Web Application

The final **CatBoost Tuned** model was integrated into an interactive Streamlit application, allowing users to generate customer response predictions without writing code.

### Customer & Campaign Inputs

The application accepts the following customer and campaign information:

- Age
- Account Balance
- Day
- Call Duration
- Campaign Contacts
- Job
- Marital Status
- Education
- Default Status
- Housing Loan
- Personal Loan
- Contact Type
- Campaign Month
- Previous Campaign Outcome

### Prediction Output

For each customer, the application provides:

- **Customer Response:** `Yes` / `No`
- **No Response Probability**
- **Yes Response Probability**
- **Model Used:** CatBoost Tuned

The probability output provides additional insight into the model's estimated likelihood for each response class, rather than relying only on the final binary prediction.

### Deployment

The application is deployed through **Streamlit Community Cloud** and is publicly accessible through the live demo linked at the top of this README.

---

## 📸 Application Screenshots

The following screenshots demonstrate the deployed application's interface, prediction workflow, model evaluation, and feature importance analysis.

### Application Home & Prediction Interface

The main application provides an interactive interface where users can enter customer and campaign information and generate a response prediction.

![Application Home](screenshots/01_home.png)

---

### Positive Response Prediction

Example of a customer predicted to respond positively to the marketing campaign, along with the corresponding response probabilities.

![Positive Response Prediction](screenshots/02_prediction_yes.png)

---

### Negative Response Prediction

Example of a customer predicted not to respond to the marketing campaign, along with the corresponding response probabilities.

![Negative Response Prediction](screenshots/03_prediction_no.png)

---

### Baseline Model Performance

Comparison of the evaluated baseline classification models across multiple performance metrics.

![Baseline Model Comparison](screenshots/04_baseline_model_comparison.png)

#### Baseline ROC-AUC Comparison

Visual ranking of the baseline models based on ROC-AUC, the primary metric used for model selection.

![Baseline ROC-AUC Comparison](screenshots/05_baseline_model_graph.png)

---

### Original vs. Tuned Model Performance

Comparison of the original and hyperparameter-tuned boosting models across multiple classification metrics.

![Original vs Tuned Model Comparison](screenshots/06_original_vs_tuned_table.png)

#### Original vs. Tuned ROC-AUC Comparison

Visual comparison of original and tuned models based on ROC-AUC.

![Original vs Tuned Model ROC-AUC Comparison](screenshots/07_original_vs_tuned_graph.png)

---

### Feature Importance Analysis

Top 10 features contributing to predictions from the final CatBoost Tuned model.

![Feature Importance Analysis](screenshots/08_feature_importance_graph.png)




---

## 📁 Project Structure

```text
Bank-Marketing-Campaign-Response-Prediction/
│
├── app.py
├── requirements.txt
├── final_model_cb_tuned.pkl
├── Feature_columns.pkl
├── README.md
│
└── screenshots/
    ├── 01_home.png
    ├── 02_prediction_yes.png
    ├── 03_prediction_no.png
    ├── 04_baseline_model_comparison.png
    ├── 05_baseline_model_graph.png
    ├── 06_original_vs_tuned_table.png
    ├── 07_original_vs_tuned_graph.png
    └── 08_feature_importance_graph.png

```

| File / Folder | Description |
|---|---|
| `app.py` | Streamlit application for customer response prediction and probability output |
| `final_model_cb_tuned.pkl` | Serialized hyperparameter-tuned CatBoost classification model used for inference |
| `Feature_columns.pkl` | Saved feature-column configuration used to align production inputs with the training feature structure |
| `requirements.txt` | Python dependencies required to run the application |
| `screenshots/` | Screenshots of the application, model evaluation, and feature importance analysis |
| `README.md` | Project documentation, methodology, results, setup, and deployment details |

---

## Technologies Used

| Category | Technologies |
|---|---|
| **Programming** | Python |
| **Data Processing** | Pandas, NumPy |
| **Data Visualization** | Matplotlib |
| **Machine Learning** | Scikit-learn, CatBoost, XGBoost, LightGBM |
| **Model Evaluation** | Accuracy, Precision, Recall, F1-Score, Log Loss, ROC-AUC, PR-AUC |
| **Deployment & Development** | Streamlit, Joblib, Jupyter Notebook, GitHub, Streamlit Community Cloud |

---

## 🚀 Installation & Local Setup

Follow the steps below to run the application locally.

### 1. Clone the Repository

```bash
git clone https://github.com/Akhlaque03/Bank-Marketing-Campaign-Response-Prediction.git
```

### 2. Navigate to the Project Directory

```bash
cd Bank-Marketing-Campaign-Response-Prediction
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

**Windows:**

```bash
venv\Scripts\activate
```

**macOS / Linux:**

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the Streamlit Application

```bash
streamlit run app.py
```

The application will be available at the local Streamlit URL shown in the terminal, typically:

http://localhost:8501

---

## 🚀 Deployment

The final CatBoost Tuned model is deployed through **Streamlit Community Cloud** as an interactive web application for real-time customer response prediction.

The application loads the serialized model and saved feature configuration, accepts customer and campaign inputs, and returns the predicted response along with class probabilities.

### Deployment Workflow

```text
Model Training
      ↓
CatBoost Tuned Model
      ↓
Model Serialization
      ↓
GitHub Repository
      ↓
Streamlit Community Cloud
      ↓
Live Prediction Application
```

### 🌐 Live Application

**Try the deployed application:**

https://akhlaque03-bank-marketing-campaign-response-prediction.streamlit.app/

The deployed application loads the saved model and feature configuration, accepts customer information through the Streamlit interface, and generates the predicted response along with response probabilities.

---
## 🔮 Future Enhancements

Potential future enhancements include:

* **Pre-Campaign Model Version** — develop a separate model excluding post-contact variables such as `duration` for realistic pre-call targeting.
* **Interactive Analytics Dashboard** — add campaign-level analytics and customer response trends.
* **Customer Segmentation** — group customers based on behavioral and financial characteristics.
* **Explainable Predictions** — integrate SHAP-based explanations to show why individual predictions are generated.
* **Model Monitoring** — track prediction performance and detect model/data drift after deployment.
* **Automated Model Retraining** — periodically retrain the model using newly collected campaign data.
* **Production API Layer** — expose the prediction model through a dedicated REST API.
* **CI/CD Pipeline** — automate testing, deployment, and application updates.

---

## 👨‍💻 Author

### Akhlaque Alam

**Aspiring Data Scientist | Python | SQL | Machine Learning | Data Analysis**

I build practical machine learning solutions focused on real-world prediction problems, model evaluation, and deployable data-driven applications.

### Core Skills

* Python
* SQL
* Machine Learning
* Data Analysis & EDA
* Data Visualization
* Streamlit Deployment

### 🔗 Connect With Me

* **GitHub:** [Akhlaque03](https://github.com/Akhlaque03)
* **LinkedIn:** [Akhlaque Alam](https://www.linkedin.com/in/akhlaque-alam-788a53410/)



---

⭐ If you found this project useful, consider giving the repository a **Star**.
