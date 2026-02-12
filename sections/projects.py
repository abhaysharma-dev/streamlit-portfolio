import streamlit as st

def show_projects():
    st.title("🚀 Projects")

    st.subheader("1. Business Analytics System (NLP + ML)")

    st.write("""
    - End-to-end ML pipeline: Audio → Whisper transcription → sentiment prediction → MySQL storage
    - Built FastAPI REST API for real-time inference and model serving
    - Containerized full system using Docker and Docker Compose (frontend, backend, database)
    - Deployed on AWS EC2 with production-ready architecture
    - TF-IDF + Logistic Regression (~85% accuracy)
    - Whisper ASR integration
    - Streamlit-based inference dashboard
    """)

    st.markdown("🔗 [GitHub Repository](https://github.com/abhaysharma-dev/business-analytics-system)")

    st.divider()

    st.subheader("2. ML Model Data Drift & Performance Monitoring (ML Project)")

    st.write("""
    - Feature drift detection using statistical mean shift
    - Prediction drift monitoring using positive-rate change
    - Logistic Regression pipeline with ColumnTransformer
    - Streamlit dashboard with health status(STABLE / MONITOR / HIGH RISK)
    """)

    st.markdown("🔗 [GitHub Repository](https://github.com/abhaysharma-dev/ML-Model-Drift-Detection-Performance-Monitoring-System)")

    st.divider()

    st.subheader("3. Data Professional Survey Analysis(Power BI Project)")

    st.write("""
    - Built an interactive Power BI dashboard analyzing survey data of 600+ data professionals
    - highlighting salary trends, job roles, programming languages, and geographic distribution.
    - Performed data cleaning using Power Query and created DAX measures to deliver actionable insights
    """)

    st.markdown("🔗 [GitHub Repository](https://github.com/abhaysharma-dev/Powerbi-Data-Professional-Survey)")

    st.divider()

    st.subheader("4. Exploratory Data Analysis of Netflix Content(Data Analysis Project)")

    st.write("""
    - comprehensive EDA on a dataset of 8,000+ titles.
    - Analyzed content distribution between Movies and TV Shows.
    - Examined regional and rating-based trends to identify dominant content categories across major markets.
    - Cleaned and transformed missing and inconsistent fields using Pandas.
             """)
    
    st.markdown("🔗 [GitHub Repository](https://github.com/abhaysharma-dev/Exploratory-Data-Analysis-of-Netflix-Content)")
