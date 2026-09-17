import streamlit as st

from resume_parser import extract_resume_text
from ats_analyzer import calculate_match_score


st.set_page_config(
    page_title="AI Resume Scanner",
    page_icon="📄",
    layout="wide"
)


st.title("📄 AI Resume Scanner")
st.write("Upload your resume and compare it with a Job Description.")


st.header("1. Upload Resume")

resume_file = st.file_uploader(
    "Upload your Resume",
    type=["pdf", "docx"]
)


st.header("2. Enter Job Description")

job_description = st.text_area(
    "Paste the Job Description here",
    height=200
)


if st.button("🔍 Analyze Resume"):

    if resume_file is None:
        st.warning("Please upload your resume.")

    elif not job_description.strip():
        st.warning("Please enter the Job Description.")

    else:

        with st.spinner("Analyzing your resume..."):

            resume_text = extract_resume_text(resume_file)

            score, matching_skills, missing_skills = calculate_match_score(
                resume_text,
                job_description
            )

        st.success("Resume analysis completed!")

        st.subheader("📊 ATS Match Score")

        st.metric(
            label="Resume Match",
            value=f"{score}%"
        )

        st.subheader("✅ Matching Skills")

        if matching_skills:
            st.write(", ".join(matching_skills))
        else:
            st.write("No matching skills found.")

        st.subheader("❌ Missing Skills")

        if missing_skills:
            st.write(", ".join(missing_skills))
        else:
            st.write("No important skills are missing.")

        st.subheader("💡 Resume Suggestion")

        if score >= 80:
            st.success(
                "Your resume has a strong match with this job description."
            )

        elif score >= 50:
            st.info(
                "Your resume has a moderate match. Consider adding missing skills."
            )

        else:
            st.warning(
                "Your resume has a low match. Try improving your skills and keywords."
            )