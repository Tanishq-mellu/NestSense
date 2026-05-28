import streamlit as st
from github import Github
st.caption(
    "Prototype for AI-assisted contributor onboarding and issue recommendation within the OWASP Nest ecosystem."
)
st.set_page_config(
    page_title="NestSense",
    page_icon="",
    layout="wide"
)
st.sidebar.title("About NestSense")
st.sidebar.info(
    """
    NestSense is an AI-assisted contributor recommendation
    and onboarding prototype for OWASP Nest.

    It helps contributors discover relevant issues
    based on skills and onboarding signals.
    """
)
st.subheader("AI-Assisted Contributor Recommendation System")
skills_input = st.text_input(
    "Enter your skills (comma separated)",
    "python,frontend,documentation"
)
user_skills = [skill.strip().lower() for skill in skills_input.split(",")]
g = Github()
repo = g.get_repo("OWASP/Nest")
issues = repo.get_issues(state="open")
recommended = []
for issue in issues:
    title = issue.title.lower()
    body = issue.body.lower() if issue.body else ""
    score = 0
    reasons = []
    for skill in user_skills:
        if skill in title or skill in body:
            score += 3
            reasons.append(f"Matches skill: {skill}")
    labels = [label.name.lower() for label in issue.labels]
    if "good first issue" in labels:
        score += 5
        reasons.append("Good first issue")
    if "documentation" in labels:
        score += 2
        reasons.append("Documentation related")
    if "frontend" in labels:
        score += 2
        reasons.append("Frontend task")
    if score > 0:
        recommended.append({
            "title": issue.title,
            "score": score,
            "reasons": reasons,
            "url": issue.html_url
        })
recommended = sorted(
    recommended,
    key=lambda x: x["score"],
    reverse=True
)
st.divider()
st.header("Recommended Issues")
if len(recommended) == 0:
    st.warning("No matching issues found.")
for item in recommended[:10]:
    with st.container():
        st.subheader(item["title"])
        st.success(f" Recommendation Score: {item['score']}")
        st.write("Why this issue is recommended:")
        for reason in item["reasons"]:
            st.write(f"- {reason}")
        st.markdown(f"[Open Issue]({item['url']})")
        st.divider()