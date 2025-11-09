🚗 WEEK 2 SUMMARY REPORT — EV Range Prediction Project
🧩 Objective

The main goal of Week 2 was to develop a Machine Learning model capable of predicting the range of electric vehicles (EVs) based on their technical parameters such as battery capacity, weight, motor power, and other performance-related features.

This week focused on converting the preprocessed data from Week 1 into a functional and optimized predictive model.

⚙️ Tasks Completed

Data Loading and Preprocessing

Imported the cleaned dataset generated during Week 1 (ev_cleaned_data.csv).

Split the dataset into training and testing sets to ensure fair model evaluation.

Applied feature scaling using StandardScaler for better model convergence.

Model Training

Implemented and trained an XGBoost Regressor, chosen for its efficiency and ability to handle complex data relationships.

Tuned model parameters such as learning rate, max depth, and number of estimators for improved accuracy.

Saved the trained model as xgboost_model.pkl for reuse and deployment.

Model Evaluation

Evaluated the model using metrics such as:

Mean Squared Error (MSE) to measure prediction error.

R² Score to determine model accuracy and fit.

Achieved a strong predictive performance, validating the success of the training pipeline.

Chatbot Integration

Developed a basic rule-based EV chatbot to interact with users and answer queries related to electric vehicles and range prediction.

The chatbot responds to keywords like battery, range, model, and performance, creating an interactive interface for demonstration.

🌱 Improvements Over Week 1
Area	Week 1	Week 2 Improvement
Focus	Data cleaning, preprocessing, and visualization	Model building and interaction
Outcome	Cleaned and structured EV dataset	Trained XGBoost model + EV chatbot
Files	ev_analysis.ipynb, ev_cleaned_data.csv	Week2_EV_Model.ipynb, xgboost_model.pkl
Functionality	Static analysis	Predictive and interactive system
User Interaction	Data exploration only	Chatbot-based conversational interface
🧠 Key Learnings

Gained hands-on experience with XGBoost regression for predictive modeling.

Understood the role of feature scaling and train-test splitting.

Integrated basic AI conversation logic through chatbot interaction.

Learned how to save and reuse trained ML models for deployment.

🧾 Outcome

At the end of Week 2, a complete EV Range Prediction system was built — capable of taking vehicle parameters as input and predicting the estimated driving range accurately.
Additionally, the EV Chatbot adds an interactive and user-friendly layer to the project, enhancing its presentation and usability.

📁 Generated Files

Week2_EV_Model.ipynb — Main notebook for Week 2

xgboost_model.pkl — Trained ML model

ev_cleaned_data.csv — Clean dataset from Week 1
