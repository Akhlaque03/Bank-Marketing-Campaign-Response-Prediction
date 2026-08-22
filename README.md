# 🏦 Bank Marketing Campaign Response Prediction

![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python\&logoColor=white)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Classification-orange)
![CatBoost](https://img.shields.io/badge/Model-CatBoost-6DB33F)
![Streamlit](https://img.shields.io/badge/Deployment-Streamlit-red?logo=streamlit\&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/Library-Scikit--Learn-F7931E?logo=scikit-learn\&logoColor=white)

> An end-to-end machine learning classification application that predicts whether a customer will respond positively to a targeted bank marketing campaign.

🚀 **Live Demo:** https://akhlaque03-bank-marketing-campaign-response-prediction.streamlit.app/

### 🎯 What This Project Does

This application uses customer demographic, financial, campaign, and previous-contact information to predict **customer response (`Yes` / `No`)** and provides the **response probability for both outcomes** using a tuned CatBoost classification model.

**Key highlights:**

*  CatBoost-based customer response prediction
*  Probability scores for both **Yes Response** and **No Response**
*  ROC-AUC and PR-AUC based model evaluation
*  Original vs. hyperparameter-tuned model comparison
*  Feature importance analysis
*  Interactive Streamlit deployment



## 📌 Project Overview

Bank marketing campaigns generate large volumes of customer interactions, but not every customer is equally likely to respond positively. Identifying customers with a higher probability of responding can help marketing teams make campaigns more targeted and efficient.

This project develops an **end-to-end binary classification solution** to predict whether a customer will respond positively to a bank marketing campaign.

The complete machine learning workflow covers:

* Data preprocessing and preparation
* Exploratory Data Analysis (EDA)
* Feature engineering and categorical encoding
* Training and evaluation of multiple classification algorithms
* Baseline model comparison
* Hyperparameter tuning
* Original vs. tuned model evaluation
* Feature importance analysis
* Final model selection
* Interactive prediction with response probabilities
* Streamlit deployment

The final application allows users to enter customer and campaign information and receive:

* **Predicted customer response — Yes / No**
* **Probability of No Response**
* **Probability of Yes Response**
* **Final model used for prediction**

The selected **CatBoost Tuned** model is deployed as an interactive Streamlit application for real-time predictions.
