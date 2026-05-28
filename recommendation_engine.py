from github import Github
g = Github()
repo = g.get_repo("OWASP/Nest")
issues = repo.get_issues(state="open")
beginner_keywords = [
    "good first issue",
    "documentation",
    "frontend",
    "bug",
    "help wanted"
]
recommended = []
for issue in issues:
    labels = [label.name.lower() for label in issue.labels]
    score = 0
    for keyword in beginner_keywords:
        if keyword in labels:
            score += 1
    if score > 0:
        recommended.append((issue.title, score, issue.html_url))
recommended.sort(key=lambda x: x[1], reverse=True)
print("\nRecommended Issues:\n")
for issue in recommended[:10]:
    print(f"Score: {issue[1]}")
    print(issue[0])
    print(issue[2])
    print("-" * 50)