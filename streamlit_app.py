import streamlit as st

st.set_page_config(
    page_title="SkillSwap",
    page_icon="✨"
)

st.title("✨ SkillSwap")
st.subheader("Learn One Skill, Teach One Skill")

st.sidebar.header("My Profile")
name = st.sidebar.text_input("Your Name")

my_skills = st.text_input(
    "Skills I can teach",
    "Python, Graphic Design"
)

learning_skills = st.text_input(
    "Skills I want to learn",
    "English, Python"
)

teach_list = [s.strip() for s in my_skills.split(",") if s.strip()]
learn_list = [s.strip() for s in learning_skills.split(",") if s.strip()]

available_skills = set(teach_list)

st.write("### 👤 Welcome", name or "Student")

col1, col2 = st.columns(2)

with col1:
    st.write("### 🧠 I Can Teach")
    for skill in teach_list:
        st.write("✅", skill)

with col2:
    st.write("### 🌱 I Want to Learn")
    for skill in learn_list:
        st.write("📚", skill)

st.write("### 🤝 Skill Matching")

for skill in learn_list:
    if skill in available_skills:
        st.success(f"You already know: {skill}")
    else:
        st.info(f"Find a partner to learn: {skill}")

st.write("### 📝 My Learning Goal")
goal = st.text_input("Add your learning goal")

if st.button("Save Goal"):
    st.success("Goal added: " + goal)