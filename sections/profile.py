import streamlit as st

def show_Profile():
    st.title("👋 Hi, I'm Abhay Sharma")

    st.subheader("Data Analyst | Machine Learning & NLP")

    col1,col2 = st.columns([1,2.5])
    with col1:
        st.image("assets/profile.jpg",width=600)
    with col2:  
        st.markdown("""
        ### I am a Computer Science undergraduate with hands-on experience working on end-to-end Data Analytics and Machine Learning projects, including: ###
         - Machine Learning
         - Data Analytics
         - NLP
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
