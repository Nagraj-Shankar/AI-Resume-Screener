🧠 AI Resume Screener
A Streamlit-powered application that screens and ranks resumes based on a job description using keyword-based scoring, basic NLP, and PDF parsing. Designed for HR teams and recruiters who want a fast, lightweight tool.

🔥 Features
✅ Upload Multiple Resume PDFs
✅ Paste a Job Description for Matching
✅ Rule-Based Resume Scoring (NLP + Keyword Match)
✅ Downloadable CSV Report
✅ Email Automation (SMTP)
✅ Admin Dashboard with Resume Preview
✅ Streamlit UI with a Slick, Clean Design

A modern, lightweight resume screening tool

🚀 Tech Stack
Frontend: Streamlit

Backend: Python

PDF Reading: PyPDF2

Resume Ranking: Keyword & similarity-based scoring

Emailing: smtplib (local email automation)

Data Processing: Pandas


⚙️ How It Works
Input: Upload resumes (PDF format) and paste a job description.

Processing: The app extracts text from each resume, tokenizes it, and compares it with job-related keywords.

Scoring: Resumes are given a match score based on the presence of key skills, education, and role-specific terms.

Output: View top resumes, download results as a CSV, and optionally email the report.
