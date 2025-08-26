from __future__ import annotations
import streamlit as st
import base64
import json
from datetime import date
from pathlib import Path
from typing import Annotated
from urllib.parse import quote_plus
import streamlit as st
from PIL import Image
from pydantic import BaseModel, EmailStr, Field, ValidationError, field_validator
from streamlit_option_menu import option_menu
    

# ========================= Page config & global CSS ========================= #
st.set_page_config(
    page_title="Prateek Sarna — Portfolio",
    page_icon="👨‍💻",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Lock sidebar open & hide default footer; circular avatar utility
st.markdown(
    """
    <style>
      [data-testid="collapsedControl"] { display: none; }
      footer { visibility: hidden; }
      .profile-pic { width: 220px; height: 220px; border-radius: 50%; object-fit: cover; border: 3px solid rgba(0,0,0,0.08); }
      .center { text-align: center; }
    </style>
    """,
    unsafe_allow_html=True,
)

# ================================ Assets =================================== #
# Embed avatar as base64 so the circular mask is perfect and consistent
AVATAR_PATHS = ["prateek.jpg", "avatar.png"]
avatar_b64 = None
for p in AVATAR_PATHS:
    if Path(p).exists():
        with open(p, "rb") as f:
            avatar_b64 = base64.b64encode(f.read()).decode()
        break

# Resume bytes (read if present)
RESUME_PATH = Path("PRATEEK_SARNA_RESUME_2025.pdf")
resume_pdf_bytes = RESUME_PATH.read_bytes() if RESUME_PATH.exists() else None

# ============================== Sidebar Nav ================================ #
with st.sidebar:
    st.markdown(
        """
        <div class='center'>
            <h2 style='margin-bottom:0'>Prateek Sarna</h2>
            <p style='margin-top:4px; opacity:0.8'>Developer • ML & Data • System Design</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if avatar_b64:
        # st.markdown(
        #     f"""
        #     <div class='center'>
        #         <img src='data:image/png;base64,{avatar_b64}' class='profile-pic' alt='Prateek Sarna'>
        #     </div>
        #     """,
        #     unsafe_allow_html=True,
        # )

        pass
    
    else:
        st.markdown("<div class='center' style='font-size:48px'>🧠</div>", unsafe_allow_html=True)

    selected = option_menu(
        menu_title="Navigate",
        options=[
            "Home",
            "AI Portfolio Chatbot",
            "Skills",
            "Projects",
            "Experience",
            "Contact",
            "Resume",
        ],
        icons=["house", "robot" ,"graph-up", "kanban", "briefcase", "envelope", "file-earmark-person"],
        default_index=0,
        orientation="vertical",
    )

# ================================= Home ==================================== #
if selected == "Home":
    left, right = st.columns([1, 2], vertical_alignment="center")

    with left:
        if avatar_b64:
            st.markdown(
                f"""
                <div class='center'>
                    <img src='data:image/png;base64,{avatar_b64}' class='profile-pic' alt='Prateek Sarna'>
                </div>
                """,
                unsafe_allow_html=True,
            )
            pass
        st.metric("CGPA", "8.16")
        st.metric("Projects", "15+")
        st.metric("DSA", "700+")

    with right:
        st.title("Building things that learn — and last.")
        st.write(
            """
            I'm **Prateek Sarna**, a software developer focused on **DSA**, **ML/DL**, and **system design**. I build
            **end‑to‑end platforms**: frontend (Streamlit/HTML), backend (**FastAPI**), reliable **REST APIs**, and
            containerized deployments with **Docker**. I also orchestrate AI pipelines with **LangChain** where useful.

            **Engineering Stack**
            - **Languages**: C++, Python, Java, SQL, HTML/CSS/JS
            - **AI/ML**: scikit‑learn, TensorFlow/Keras, CNN/RNN/Transformers, multimodal fusion, LangChain
            - **Backend**: FastAPI, auth, rate‑limiting, logging, telemetry
            - **System Design**: microservices, caching, pagination, idempotency, retries, observability
            - **DevOps**: Docker, Git, CI/CD, Unix; reproducible builds & envs
            - **Data**: Pandas/NumPy, SQL, data validation, ETL
            """
        )
        st.info(
            "Currently exploring: Full end‑to‑end development with **LangChain**, **FastAPI**, and **Docker** — building robust APIs, orchestration, and deployable AI services."
        )

# ================================ Skills =================================== #
elif selected == "Skills":
    st.title("Skills & Depth")
    st.caption("From idea → architecture → implementation → deploy → observe.")

    cols = st.columns(3)
    with cols[0]:
        st.subheader("Programming")
        st.write("C++, Python, Java, SQL, HTML/CSS/JS")
        st.subheader("AI/ML/DL")
        st.write("scikit‑learn, TensorFlow/Keras, CNN, RNN, Transformers, LangChain, vector DBs")
    with cols[1]:
        st.subheader("Backend & APIs")
        st.write("FastAPI, REST design, auth, rate‑limits, pagination, versioning, OpenAPI")
        st.subheader("Data")
        st.write("Pandas, NumPy, SQL, ETL, validation")
    with cols[2]:
        st.subheader("Systems & DevOps")
        st.write("System design, Docker, Git, CI/CD, Unix, logging, monitoring")

# ================================ Projects ================================= #
elif selected == "Projects":

    def tech_badge(name, color="#4CAF50"):
        return f"<span style='background-color:{color}; color:white; padding:4px 10px; border-radius:12px; font-size:0.85em; margin-right:5px;'>{name}</span>"

    st.title("🚀 Projects")

    projects = [
        {
            "title": "Medical Summarizer (LangChain + FastAPI + Docker)",
            "desc": "End-to-end AI app for summarizing patient records with LangChain, deployed in Docker with FastAPI backend.",
            "tech": [
                ("LangChain", "#FF9800"),
                ("FastAPI", "#009688"),
                ("Docker", "#0db7ed"),
                ("Python", "#3572A5")
            ],
            "link": "https://github.com/yourrepo"
        },
        {
            "title": "Neural Machine Translation",
            "desc": "French-to-English translation using encoder-decoder architecture with attention mechanism.",
            "tech": [
                ("Python", "#3572A5"),
                ("TensorFlow", "#FF6F00"),
                ("Keras", "#D00000")
            ],
            "link": "https://github.com/yourrepo"
        },
        {
            "title": "InstaBot Automation",
            "desc": "Instagram automation tool using Selenium for scraping and automating user actions.",
            "tech": [
                ("Python", "#3572A5"),
                ("Selenium", "#43A047"),
                ("API Integration", "#795548")
            ],
            "link": "https://github.com/yourrepo"
        },
        {
            "title": "Pneumonia Detection",
            "desc": "Deep learning model to detect pneumonia from X-ray images.",
            "tech": [
                ("Python", "#3572A5"),
                ("TensorFlow", "#FF6F00"),
                ("CNN", "#9C27B0")
            ],
            "link": "https://github.com/yourrepo"
        }
    ]

    # LangChain projects first
    projects.sort(key=lambda p: "LangChain" not in [t[0] for t in p["tech"]])

    for proj in projects:
        st.subheader(proj["title"])
        st.write(proj["desc"])
        badges_html = "".join([tech_badge(name, color) for name, color in proj["tech"]])
        st.markdown(badges_html, unsafe_allow_html=True)
        if proj["link"]:
            st.markdown(f"[🔗 View Project]({proj['link']})")
        st.markdown("---")

# =============================== Experience ================================ #
elif selected == "Experience":
    st.title("Experience & Leadership")
    st.markdown(
        """
        - **Team Lead** — Led ML-focused teams; reviews, sprints, delivery.
        - **Hackathon** — Live video+audio analysis; pivoted to PyTorch under time pressure.
        - **MLOps** — From notebooks to reproducible deployments with Streamlit & Docker.
        """
    )
    st.markdown("---")
    st.subheader("Academic")
    st.write("CSE Graduate • CGPA **8.16** • NPTEL: Top 1% (Discrete Math), Top 2% (P&S)")

# ================================ Contact ================================== #
elif selected == "Contact":
    from typing import Optional
    import urllib.parse

    # ------------------ Pydantic Model ------------------
    class ContactForm(BaseModel):
        name: str = Field(..., min_length=2, max_length=50)
        email: EmailStr
        message: str = Field(..., min_length=2, max_length=500)

    # ------------------ Streamlit UI ------------------
    st.set_page_config(page_title="Contact - Prateek Sarna", layout="centered")
    st.title("📬 Contact Me")

    st.write("Fill in your details below, and when you click **Send**, "
            "WhatsApp will open with your message ready to send to me.")

    with st.form("contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Your Message")
        submitted = st.form_submit_button("Send via WhatsApp")

    if submitted:
        try:
            # Validate input
            form = ContactForm(name=name, email=email, message=message)

            # Prepare WhatsApp URL
            phone_number = "+919911400546"
            encoded_msg = urllib.parse.quote(
                f"Hello, my name is {form.name} ({form.email}).\n\n{form.message}"
            )
            whatsapp_url = f"https://wa.me/{phone_number}?text={encoded_msg}"

            st.success("Validation successful! Opening WhatsApp...")
            st.markdown(f"[Click here if WhatsApp doesn't open automatically]({whatsapp_url})", unsafe_allow_html=True)
            st.markdown(f"<meta http-equiv='refresh' content='0; url={whatsapp_url}'>", unsafe_allow_html=True)

        except ValidationError as e:
            st.error("Please correct the errors below:")
            for err in e.errors():
                st.write(f"**{err['loc'][0]}**: {err['msg']}")


# ================================= Resume ================================== #
elif selected == "Resume":
    st.title("Resume & Downloads")
    st.write("Grab my latest resume/CV or request a tailored version for a specific role.")

    st.download_button(
        label="Download Resume (PDF)",
        data=resume_pdf_bytes,
        file_name="Prateek_Sarna_Resume.pdf",
        mime="application/pdf",
    )
    st.caption("Resume")

    st.markdown("---")
    st.subheader("Quick Snapshot")
    st.write(
        """
        - **Roles of interest**: Application Engineering, Software Development (SDE), ML Engineering.  
        - **Keywords**: Python, DSA, ML/DL, Unix, Docker, Git, Streamlit, SQL, APIs, Data Pipelines.  
        - **Open to**: Internships, part-time roles, and research collaborations.
        """
    )

# ================================== AI Portfolio Chatbot ====================
    
elif selected == "AI Portfolio Chatbot":

    st.title("🤖 AI Portfolio Chatbot")
    st.markdown("Ask me anything about **Prateek Sarna's** skills, projects, and experience!")

    # User input
    user_input = st.text_input("Type your message...")

    import json

    if st.button("Send") and user_input.strip():
        try:
            import requests
            api_url = "http://127.0.0.1:8000/invoke"
            payload = {"user_query": user_input}
            
            response = requests.post(api_url, json=payload)

            # Convert byte content to dict
            data = json.loads(response.content.decode("utf-8"))

            ai_response = data.get("response", "No response from AI")
        
        except Exception as e:
            ai_response = f"API call failed: No more tokens left :("

        st.markdown(f"**AI:** {ai_response}")



# ================================= Footer ================================== #
st.markdown(
    f"""
    <hr style='margin-top:3rem;margin-bottom:0.5rem' />
    <div style='display:flex;justify-content:space-between;align-items:center;opacity:0.8'>
      <div>© {date.today().year} Prateek Sarna</div>
      <div></div>
    </div>
    """,
    unsafe_allow_html=True,
)
