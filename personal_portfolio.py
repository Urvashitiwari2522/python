# personal_portfolio
import streamlit as st

# --- Portfolio Information ---
NAME = "Urvashi Tiwari"
DESCRIPTION = "BCA 4th Semester Student | Python Developer | AI & ML Enthusiast"
EMAIL = "priyatiwari0425@gmail.com"
LINKEDIN = "https://www.linkedin.com/in/urvashi-tiwari2208"
GITHUB = "https://github.com/urvashitiwari2522"

# --- Page Configuration ---
st.set_page_config(page_title="Urvashi Tiwari - Portfolio", page_icon="📌")

# --- Portfolio Header ---
st.title(NAME)
st.write(DESCRIPTION)

# Display Profile Picture
st.image("profile.jpg", width=200)

# --- Contact Info ---
st.write(f"📧 Email: {EMAIL}")
st.write(f"🔗 [LinkedIn]({LINKEDIN})")
st.write(f"🐍 [GitHub]({GITHUB})")

# --- About Me Section ---
st.header("About Me")
st.write("""
Hii I'm Urvashi _ Currently pursuing my Bachelor of Computer Applications (BCA) at University of Allahabad🎓. 
I am a second-year student and I am passionate about continuous learning, hard work, and staying updated with the latest advancements in the field.  
I am just a learner who is trying to do better every day.  
I am currently learning and working with programming languages such as SQL, HTML, JAVA, PYTHON, LINUX, and more.  
I'm excited to connect with like-minded professionals with a positive attitude to innovate and push the boundaries of what data can achieve and ready to take on new challenges, let's connect.
""")

# --- Skills Section ---
st.header("Skills")
st.write("""
- *Programming Languages:* HTML, Core Java, Python  
- *Libraries & Frameworks:* NumPy, Pandas  
- *Web Development:* Flask  
- *Operating Systems:* Linux  
- *Databases:* MySQL  
""")

# --- Projects Section ---
st.header("Projects")
projects = {
    "Hangman Game (Python)": "A classic word-guessing game built using Python.",
    "QR Code Generator (Python)": "A project that generates QR codes for various inputs.",
    "Secret Code Language (Python)": "An encryption-based project to encode and decode messages.",
    "Chatbot (Python)": "A chatbot built using Python for interactive communication."
}

for project, desc in projects.items():
    st.subheader(project)
    st.write(desc)

# --- Contact Section ---
st.header("Contact Me")
st.write(f"📧 Email: {EMAIL}")
st.write(f"🔗 [LinkedIn]({LINKEDIN})")
st.write(f"🐍 [GitHub]({GITHUB})")

# --- Footer ---
st.write("---")
st.write("© 2025 Urvashi Tiwari - Built with Streamlit")