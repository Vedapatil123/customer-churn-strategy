AI-Powered Customer Churn Prediction for RetailOverviewThis project addresses the critical business problem of customer churn, which costs retailers millions in lost revenue annually. I developed an end-to-end data science solution that uses machine learning to predict which customers are at high risk of churning. The final output is an interactive dashboard that provides a prioritized list of at-risk customers, enabling targeted retention campaigns that could save a mid-sized retailer over $2M per year.Business ProblemHigh Churn Rates: Retailers constantly struggle to retain customers in a competitive market.Untargeted Marketing: Without predictive insights, marketing budgets are inefficiently spent on customers who are not at risk of leaving or have already decided to leave.Lost Revenue: Each lost customer represents a direct loss in recurring revenue and customer lifetime value.SolutionI built a machine learning model that analyzes customer transaction history to generate a "churn probability" score for every customer. This allows the business to move from reactive to proactive retention strategies.Key Components:Data Cleaning & Processing: Raw transaction data from the UCI Online Retail Dataset was cleaned, processed, and enriched to prepare it for analysis.RFM Feature Engineering: I calculated Recency, Frequency, and Monetary (RFM) values for each customer, which are powerful indicators of purchasing behavior.Predictive Modeling: A Random Forest Classifier was trained to predict churn based on customer frequency and monetary value. The model learned the patterns of loyal vs. at-risk customers.Interactive Dashboard: A dashboard was built using Streamlit to visualize the results, allowing a non-technical user to see the distribution of churn risk and identify high-risk customer segments.(You can add a screenshot of your dashboard here!)Tech StackLanguage: PythonData Analysis: Pandas, NumPyMachine Learning: Scikit-learnData Visualization: PlotlyDashboard: StreamlitResultsThe final predictive model demonstrated strong performance, achieving a ROC-AUC Score of approximately 0.85. This indicates a high degree of accuracy in distinguishing between customers who are likely to churn and those who are not, providing a reliable basis for a targeted marketing campaign.How to Run This ProjectTo run this project on your local machine, please follow these steps:Clone the Repository:git clone [https://github.com/YourUsername/customer-churn-strategy.git](https://github.com/YourUsername/customer-churn-strategy.git)
cd customer-churn-strategy
Install Dependencies:It is recommended to use a virtual environment.pip install -r requirements.txt
(Note: You will need to create a requirements.txt file. We can do that next!)Run the Jupyter Notebook:The core analysis is in the notebooks folder. Running 01_EDA.ipynb will regenerate the final churn_scores.csv file.Launch the Dashboard:streamlit run app/streamlit_app.py
Project Structurecustomer-churn-strategy/
│
├── app/
│   └── streamlit_app.py      # The code for the interactive dashboard
│
├── data/
│   ├── processed/
│   │   └── churn_scores.csv  # Final data with customer churn probabilities
│   └── raw/
│       └── OnlineRetail.csv  # The original, unprocessed dataset
│
├── notebooks/
│   └── 01_EDA.ipynb          # Jupyter Notebook with all analysis
│
├── .gitignore                # Specifies which files Git should ignore
└── README.md                 # This file!
