# Project Overview

When patients miss their healthcare appointments, this expense will directly result in lost revenue, inefficiently scheduled appointments or delays in patient care. The purpose of this project is to utilize machine learning and data visualization to be predictive of whether or not a patient will miss their scheduled appointment, as well as to analyse the elements that impact "no-shows".

The solution will incorporate data cleaning, predictive models and interactive dashboards that are designed to assist providers in maximizing appointment scheduling and enhancing attendance by patients.

## Objectives

-Predict patient no-shows using a machine learning model

-Identify key factors influencing appointment attendance

-Visualize no-show trends using interactive dashboards

-Provide actionable insights and optimization recommendations

## Tools & Technologies

-Python (Pandas, NumPy, Scikit-learn)

-Machine Learning – Decision Tree Classifier

-Power BI – Interactive dashboard & insights

-Jupyter Notebook

-CSV Dataset

## Project Structure

Healthcare-NoShow-Prediction/

│

├── healthcare_dataset.csv

├── healthcare_dataset_cleaned.csv

├── Healthcare_PythonDataCleaning.ipynb

├── Healthcare_PredictionModel.ipynb

├── feature_importance.csv

├── powerbi_dashboard.pbix

└── README.md

## Workflow

🔹 Step 1: Data Cleaning & Preprocessing

-Removed irrelevant columns

-Fixed date formats (European date handling)

-Handled missing values and invalid entries

-Encoded categorical variables (Gender, No-Show)

-Engineered useful features (age groups, weather impact, appointment timing)

🔹 Step 2: Prediction Model

-Selected meaningful numeric features

-Split data into training (80%) and testing (20%)

-Trained a Decision Tree Classifier

-Evaluated model using accuracy

-Extracted feature importance to understand influencing factors

*Output:

-No-show predictions (Yes/No)

-Feature importance ranking

🔹 Step 3: Visualization & Insights

-Built an interactive Power BI dashboard

*Visualized:

-Overall no-show rate

-No-shows by age group, gender, month

-Impact of weather conditions

-Feature importance from ML model

-Enabled filters for dynamic analysis

## Key Insights

-Patients who are older have an increased chance of not attending their scheduled appointment.

-No-show rates increase during periods of severe weather.

-The amount of dependence a patient has on someone else and when they schedule their appointment alters a patient's willingness to show up.

-Months of the year experience higher seasonal patterns of no-shows than other months of the year.

## Optimization Recommendations

-Send targeted SMS reminders to high-risk patients

-Provide assistance for elderly patients

-Adjust scheduling during extreme weather conditions

-Apply smart overbooking strategies for low-risk slots

## Results

-Successfully built a predictive model for healthcare appointment no-shows

-Identified major contributing factors through feature importance

-Delivered actionable insights via an interactive dashboard

## Conclusion

By converting unprocessed healthcare data into predictive insights and recommendations that are ready for business use, this project exemplifies an end-to-end data analytics and machine learning workflow.
