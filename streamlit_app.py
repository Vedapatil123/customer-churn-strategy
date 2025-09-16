import streamlit as st
import pandas as pd
import plotly.express as px

# Load the data with churn scores
# Ensure 'data/processed/churn_scores.csv' is in the correct path
try:
    df = pd.read_csv('data/processed/churn_scores.csv')
except FileNotFoundError:
    st.error("Error: The data file 'data/processed/churn_scores.csv' was not found. Please ensure the file path is correct.")
    st.stop()

st.set_page_config(layout="wide")
st.title("Customer Churn Risk Dashboard")

# --- Create the 'churn_flag' column ---
# This was the cause of the error. We define 'at risk' customers as those with Recency > 90 days.
if 'Recency' in df.columns:
    df['churn_flag'] = (df['Recency'] > 90).astype(int)
else:
    st.error("Error: The 'Recency' column required to create 'churn_flag' is missing from the dataset.")
    st.stop()

# --- Key Metrics ---
# Check if required columns exist before using them
required_columns = ['churn_probability', 'churn_flag', 'Recency', 'Monetary', 'CustomerID']
if not all(col in df.columns for col in required_columns):
    st.error(f"Error: The dataset must contain the following columns: {', '.join(required_columns)}")
    st.stop()

avg_churn_prob = df['churn_probability'].mean()
churned_customers = df[df['churn_flag'] == 1].shape[0]
total_customers = df.shape[0]

col1, col2, col3 = st.columns(3)
col1.metric("Total Customers", f"{total_customers:,}")
col2.metric("Identified as 'At Risk' (Recency > 90 days)", f"{churned_customers}")
col3.metric("Average Churn Probability", f"{avg_churn_prob:.2%}")

st.markdown("---")

# --- Charts ---
col1, col2 = st.columns(2)

with col1:
    st.subheader("Distribution of Churn Risk Scores")
    fig_hist = px.histogram(df, x='churn_probability', nbins=20, title="Customer Risk Score Distribution")
    st.plotly_chart(fig_hist, use_container_width=True)

with col2:
    st.subheader("Recency vs. Monetary Value by Churn Risk")
    fig_scatter = px.scatter(df, x='Recency', y='Monetary', color='churn_probability',
                             hover_data=['CustomerID'], title="Recency vs. Monetary by Churn Risk",
                             color_continuous_scale='reds')
    st.plotly_chart(fig_scatter, use_container_width=True)

# --- Data Table of High-Risk Customers ---
st.subheader("Top 20 High-Risk Customers")
st.dataframe(df.sort_values('churn_probability', ascending=False).head(20))

