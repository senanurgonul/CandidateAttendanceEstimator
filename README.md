# Candidate Attendance Estimator  
**AI Model for Predicting Interview Attendance Based on Historical Participation Patterns**

---

## Project Overview  
**Candidate Attendance Estimator** is an AI-powered forecasting tool developed to predict daily candidate attendance for scheduled interviews based on behavioral data from previous assessments.

It takes into account historical no-show patterns and allows HR teams to estimate how many candidates may not attend on specific dates—even before the actual interview day arrives.

The system is fully interactive: users select a date range and input how many candidates they plan to invite each day. The model then predicts how many of those are likely to not show up, enabling smarter daily planning.

---

## Project Context — Developed During My Turkish Airlines Internship  
This project was developed during my **Software Engineering Internship at Turkish Airlines**, specifically for the **Cabin Recruitment Planning Department**.

Its main objective was to support **daily interview capacity planning** by providing a predictive tool that:

- Uses historical attendance data  
- Accepts user-defined planned interview quotas  
- Outputs expected daily no-shows  
- Improves scheduling accuracy for each interview day  

With this project, I transformed raw interview planning data into a machine learning–powered decision-support system that now helps the Cabin HR operations team:

🔹 Minimize over/underbooking risk  
🔹 Reduce uncertainty caused by no-shows  
🔹 Plan daily quotas more efficiently

---

## Machine Learning Approach  
The model is built on **Random Forest Regression**, a non-linear ensemble learning technique that performs exceptionally well in forecasting problems with temporal and behavioral variance.

### Model Input Features:
- Year  
- Month  
- Day of Month  
- Planned Attendance (user input)

### Model Output:
- **Predicted No-Show Count** (for each selected date)

Even if the target date does not exist in the training data, the model makes accurate predictions by generalizing from similar temporal patterns.

---

## Interactive Planning Interface  
The tool includes a lightweight Flask web interface for real-time interaction:

**Step 1**: Select a custom date range  
**Step 2**: Enter expected planned candidates for each day  
**Step 3**: Instantly receive predicted no-show counts per day + total for the period

This makes the tool fully accessible to HR personnel without requiring coding or technical expertise.

---

## Analytics & Reporting  
- Daily line charts showing attendance risk  
- Excel export of all predicted days  
- Monthly attendance forecast summary  
- HR dashboard integration with filters (department, day type, etc.)

---

## Tech Stack

### 🔹 Core AI / Data Science
- Scikit-learn – Model building (Random Forest)  
- Pandas – Feature extraction & date handling  
- NumPy – Math operations

### 🔹 Backend
- Flask – Lightweight API & server  
- Jinja2 – HTML templating  
- HTML + CSS – Web UI

---

## Potential Enhancements (AI-Focused Roadmap)
- Gradient Boosting Regressors (e.g. XGBoost / LightGBM)  
- SHAP Explainability for transparency  
- Anomaly detection for rare high no-show days
