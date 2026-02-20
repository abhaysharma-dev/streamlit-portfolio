import streamlit as st

def show_Profile():
    st.title("👋 Hi, I'm Abhay Sharma")

    st.subheader("Machine Learning Engineer | ML Deployment | FastAPI | Docker | AWS EC2 | NLP")

    col1,col2 = st.columns([1,2.5])
    with col1:
        st.image("assets/profile.jpg",width=600)
    with col2:  
        st.markdown("""
        #### I am a Computer Science undergraduate with hands-on experience building and deploying end-to-end Machine Learning systems. 
         - Machine Learning model development and deployment  
         - REST API development using FastAPI
         - Docker containerization
         - Cloud deployment on AWS EC2  
         - Data Analytics           
         - Streamlit
        """)

        st.markdown("📍 **Open to internships and entry-level roles**")

    st.download_button(
        label="📄 Download My Resume",
        file_name="Abhay_Sharma_ML_Data_Analyst.pdf",
        data=open("assets/Abhay_Sharma_ML_Data_Analyst.pdf", "rb"),
        mime="application/pdf",
        width= 400
    )
