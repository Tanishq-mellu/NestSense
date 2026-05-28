from github import Github
g = Github()
repo = g.get_repo( "OWASP/Nest" )
issues = repo.get_issues( state="open" )
user_skills = [
    "python",
    "frontend",
    "documentation",
    "automation",
]
recommended = []
for issue in issues:
    title = issue.title.lower()
    body = issue.body.lower() if issue.body else ""
    score = 0
    reasons = []

    for skill in user_skills:
        if skill in title or skill in body:
            score += 3
            reasons.append( f"Matches skill: {skill}" )
    labels = [label.name.lower() for label in issue.labels]
    if "good first issue" in labels:
        score += 5
        reasons.append( "Good first issue" )
    if "documentation" in labels:
        score += 2
        reasons.append( "Documentation task" )
    if "frontend" in labels:
        score += 2
        reasons.append( "Frontend related" )
    if "bug" in labels:
        score += 1
        reasons.append( "Bug fixing experience" )
    if score > 0:
        recommended.append( {
            "title": issue.title,
            "url": issue.html_url,
            "score": score,
            "reasons": reasons
        } )
recommended = sorted(
    recommended,
    key=lambda x: x["score"],
    reverse=True
)
print( "\nAI-Assisted Contributor Recommendations\n" )
for item in recommended[:10]:
    print( "=" * 60 )
    print( f"Issue: {item['title']}" )
    print( f"Score: {item['score']}" )
    print( "Why Recommended:" )

    for reason in item["reasons"]:
        print( f"- {reason}" )
    print( f"URL: {item['url']}" )