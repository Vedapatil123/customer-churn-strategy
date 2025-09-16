# Customer Churn Prediction & Risk Dashboard

## 1. Project Overview

This project provides an interactive dashboard built with Streamlit to analyze and visualize customer churn risk. It uses a dataset of customer transactions to calculate churn probability and identifies key segments of at-risk customers. The primary goal is to equip a business with the tools to proactively engage customers who are likely to churn.

This project was created to demonstrate my skills in:
- **Data Analysis** with Pandas
- **Data Visualization** with Plotly
- **Web Application Development** with Streamlit
- **Business Acumen** in applying data insights to solve a real-world problem (customer retention).

---

## 2. Features

- **Dynamic Key Metrics**: Displays real-time counts of total customers, at-risk customers, and the average churn probability.
- **Interactive Visualizations**: Includes a histogram of risk scores and a scatter plot comparing customer recency and monetary value, color-coded by churn risk.
- **Actionable Customer List**: Provides a data table of the top 20 customers with the highest churn risk scores, enabling targeted marketing or support efforts.

---

## 3. Tech Stack

- **Python**: The core programming language used for data manipulation and application logic.
- **Pandas**: For data loading and transformation.
- **Streamlit**: To build and serve the interactive web dashboard.
- **Plotly**: For creating interactive charts and graphs.

---

## 4. How to Run This Project

Follow these steps to get the application running on your local machine.

**Prerequisites:**
- Python 3.8 or higher installed.
- `pip` (Python package installer).

**Installation & Setup:**

1.  **Clone the repository:**
    ```
    git clone https://github.com/YOUR_USERNAME/your-repo-name.git
    ```

2.  **Navigate to the project directory:**
    ```
    cd your-repo-name
    ```

3.  **Install the required libraries:**
    ```
    pip install -r requirements.txt
    ```

4.  **Run the application:**
    ```
    streamlit run app/streamlit_app.py
    ```

After running the command, your web browser should open to `http://localhost:8501` with the dashboard.

---

## 5. Project Structure

```
├── app/
│   └── streamlit_app.py   # The main application script
├── data/
│   └── processed/
│       └── churn_scores.csv # The dataset used
├── README.md              # Project documentation
└── requirements.txt       # Python dependencies
```

---

## 6. Future Improvements

- Integrate a machine learning model to generate more accurate `churn_probability` scores.
- Add more filtering options to the dashboard (e.g., filter by customer segment).
- Deploy the application to a cloud service like Streamlit Community Cloud or Heroku.
```
