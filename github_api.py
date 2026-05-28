from github import Github
g = Github()
repo = g.get_repo("OWASP/Nest")
issues = repo.get_issues(state="open")
print("Open Issues in OWASP Nest:\n")
for issue in issues[:10]:
    print(f"#{issue.number} - {issue.title}")