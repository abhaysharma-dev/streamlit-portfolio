import streamlit as st

def show_projects():
    st.title("🚀 Projects")

    st.subheader("1. ML Model Data Drift & Performance Monitoring (ML Project)")

    st.write("""
    - Feature drift detection using statistical mean shift
    - Prediction drift monitoring using positive-rate change
    - Logistic Regression pipeline with ColumnTransformer
    - Streamlit dashboard with health status(STABLE / MONITOR / HIGH RISK)
    """)

    st.markdown("🔗 [GitHub Repository](https://github.com/abhaysharma-dev/ML-Model-Drift-Detection-Performance-Monitoring-System)")

    st.divider()

    st.subheader("2. Business Analytics System (NLP + ML)")

    st.write("""
    - Call Recordings transcripts sentiment analysis
    - TF-IDF + Logistic Regression (~85% accuracy)
    - Whisper ASR integration
    - Streamlit-based inference dashboard
    """)

    st.markdown("🔗 [GitHub Repository](https://github.com/abhaysharma-dev/business-analytics-system)")

    st.divider()

    st.subheader("3. Exploratory Data Analysis of Netflix Content(Data Analysis Project)")

    st.write("""
    - comprehensive EDA on a dataset of 8,000+ titles.
    - Analyzed content distribution between Movies and TV Shows.
    - Examined regional and rating-based trends to identify dominant content categories across major markets.
    - Cleaned and transformed missing and inconsistent fields using Pandas.
             """)
    
    st.markdown("🔗 [GitHub Repository](https://github.com/abhaysharma-dev/Exploratory-Data-Analysis-of-Netflix-Content)")
