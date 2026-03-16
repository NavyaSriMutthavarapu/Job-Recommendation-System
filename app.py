# app.py

import streamlit as st

from model_utils import predict_top_roles
from skill_utils import get_skill_gap, get_career_guidance
from role_data import job_roles
from resume_utils import extract_text_from_pdf


# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Job Recommendation System", layout="centered")

st.title("💼 Job Recommendation System")
st.write("Get career recommendations based on your skills or resume")

# ---------------- INPUT OPTIONS ----------------
st.subheader("📥 Provide Your Input")

user_input = st.text_area("Enter your skills (e.g., python sql communication)")

uploaded_file = st.file_uploader("OR Upload your Resume (PDF)", type=["pdf"])


# ---------------- BUTTON ----------------
if st.button("Get Recommendations"):

    # ---------------- INPUT HANDLING ----------------
    if uploaded_file is not None:
        try:
            user_input = extract_text_from_pdf(uploaded_file)
            st.success("✅ Resume uploaded and processed successfully!")
        except:
            st.error("❌ Failed to read PDF. Try another file.")
            st.stop()

    elif user_input.strip() == "":
        st.warning("⚠️ Please enter skills or upload a resume")
        st.stop()

    # ---------------- PREDICTION ----------------
    roles = predict_top_roles(user_input)

    st.subheader("🔮 Top Recommended Roles")

    # ---------------- DISPLAY RESULTS ----------------
    for role in roles:
        st.markdown("---")
        st.subheader(f"📌 {role}")

        data = job_roles.get(role, {
            "description": "No data available",
            "skills_required": []
        })

        # Description
        st.write("**📖 Description:**")
        st.write(data["description"])

        # Skill Gap
        required, missing = get_skill_gap(role, user_input)

        st.write("**🧠 Required Skills:**")
        st.write(required)

        st.write("**⚠️ Missing Skills:**")
        st.write(missing if missing else "None 🎉")

        # Guidance
        guidance = get_career_guidance(missing)

        st.write("**🚀 Career Guidance:**")
        if guidance:
            for g in guidance:
                st.write(f"👉 {g}")
        else:
            st.write("You are well-prepared for this role 🎉")