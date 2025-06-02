🏥 Breast Cancer Mortality & Survival Prediction

Coursework Project – November 2024 University of Westminster | Data Mining & Machine Learning
📌 Project Overview
This project applied machine learning to predict breast cancer mortality outcomes and estimate survival durations using patient data from the SEER database. The objective was to support clinical decision-making by identifying high-risk patients and estimating survival time for those not expected to survive.
The work was structured around the CRISP-DM framework and focused on evaluating models not just by accuracy, but also by fairness, recall, and clinical relevance.

🧠 What I Did
Built classification models to predict mortality status (Alive vs Dead):
Logistic Regression
K-Nearest Neighbours
Naive Bayes
Built regression models to estimate patient survival duration:
Decision Tree Regressor
Pre-pruned version for interpretability
Tuned hyperparameters using GridSearchCV
Evaluated models with AUC, F1-score, MAE, and R²
Reflected on performance trade-offs and ethical implications in healthcare ML

🧰 Tools Used
Python
pandas, scikit-learn, matplotlib, seaborn
GridSearchCV, train_test_split, DecisionTreeRegressor
Jupyter Notebook

🎯 Key Insights
Logistic Regression achieved the best performance under recall-based evaluation, making it the safest model for clinical prioritisation
Pre-pruned Decision Tree models provided good balance between interpretability and performance for survival estimation
Tumour staging, hormone receptor status, and node positivity were strong predictors

🧠 Reflection
This project strengthened my skills in applying ML to real-world, high-stakes datasets. It helped me think beyond accuracy, focusing on what’s clinically meaningful when evaluating models for use in healthcare.
Later, when I joined the Research Café project on fairness in AI, I found myself reflecting on this work — and all the ways I could have applied tools like Fairlearn, SHAP, or even adjusted class weighting to reduce bias and improve transparency. It’s helped me connect technical modelling with ethical considerations more deeply, especially in sensitive domains like healthcare.