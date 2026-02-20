import streamlit as st

def show_skills():
    st.title("🛠️ Skills")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("1. Programming Languages")
        st.write("- Python\n- SQL\n- C++")

        st.subheader("3. ML & NLP")
        st.write("- Logistic Regression\n- TF-IDF\n- Text Preprocessing \n- Feature Engineering \n - Model Evaluation (Accuracy, Precision, Recall)\n - Hyperparameter Tuning ")

    with col2:
        st.subheader("2. Libraries")
        st.write("- Pandas\n- NumPy\n- Scikit-learn\n- FastAPI\n- Matplotlib\n- Evidently AI")

        st.subheader("4. Tools")
        st.write("- Power BI \n- Streamlit\n- Docker\n- AWS EC2\n- MySQL\n- Jupyter Notebook")
