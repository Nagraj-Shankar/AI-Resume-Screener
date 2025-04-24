import streamlit as st
import pandas as pd
from read_resume import extract_text_from_pdf
from ranker import rank_resumes

# Set page config and add a logo
st.set_page_config(page_title="AI Resume Screener", layout="centered", page_icon="📄")
st.image("assets/logo.jpeg", width=100)
st.markdown("# 🤖 AI Resume Screener")
st.markdown("Upload resumes and a job description to instantly find the best-fit candidates!")

# Expandable section for Job Description
with st.expander("📋 Paste Job Description"):
    job_desc = st.text_area("", height=250, placeholder="Paste job description here...")

# File uploader (only PDF files)
uploaded_files = st.file_uploader("📄 Upload Resume PDFs", type=["pdf"], accept_multiple_files=True)

# Input for email automation (to send report)
recipient_email = st.text_input("Enter your email address to receive the report:", placeholder="example@domain.com")

if st.button("🚀 Rank Resumes"):
    if not uploaded_files or not job_desc:
        st.warning("🚨 Please upload at least one resume and paste a job description.")
    else:
        with st.spinner("🧠 Analyzing resumes..."):
            resumes = [extract_text_from_pdf(file) for file in uploaded_files]
            ranked = rank_resumes(job_desc, resumes)
        st.success("✅ Ranking complete!")
        
        # Create a DataFrame for the report
        report_data = [
            {"Resume Number": idx + 1, "Score": score, "Justification": justification}
            for idx, (score, justification) in enumerate(ranked)
        ]
        df_report = pd.DataFrame(report_data)
        
        # Use tabs for Results and Admin Dashboard
        tab1, tab2 = st.tabs(["Results", "Admin Dashboard"])
        
        with tab1:
            st.markdown("### 📊 Ranked Resumes:")
            for idx, (score, justification) in enumerate(ranked):
                st.write(f"**Resume {idx + 1}** — Score: **{score:.2f}**")
                st.write(f"*Justification:* {justification}")
            
            # Downloadable CSV Report button
            csv = df_report.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="📥 Download Report as CSV",
                data=csv,
                file_name="resume_report.csv",
                mime="text/csv",
            )
        
        with tab2:
            st.markdown("### 🖥️ Admin Dashboard / Resume Previewer")
            for i, text in enumerate(resumes):
                with st.expander(f"Resume {i + 1} Preview"):
                    st.text_area("Resume Text", text, height=200)
        
        # Email automation: send the report when button is clicked
        if st.button("📧 Send Report via Email"):
            if recipient_email:
                from email_automation import send_email_report
                if send_email_report(recipient_email, df_report):
                    st.success("Email sent successfully!")
                else:
                    st.error("Failed to send email. Please check logs.")
            else:
                st.warning("Please enter a valid email address to send the report.")
