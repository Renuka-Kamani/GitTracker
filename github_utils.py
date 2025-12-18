from github import Github
from datetime import timezone
from config import GITHUB_TOKEN

if not GITHUB_TOKEN:
    raise SystemExit("❌ Please set your GITHUB_TOKEN environment variable first.")

g = Github(GITHUB_TOKEN)

def get_github_details(username):
    """Fetch repository count, total commits, and last commit date for a user."""
    try:
        user = g.get_user(username)
        repos = list(user.get_repos())
        total_repos = len(repos)
        total_commits = 0
        last_commit = None

        for repo in repos:
            commits = repo.get_commits()
            count = commits.totalCount
            total_commits += count

            # get latest commit date
            if count > 0:
                commit_date = commits[0].commit.author.date
                if last_commit is None or commit_date > last_commit:
                    last_commit = commit_date

        return {
            "username": username,
            "total_repos": total_repos,
            "total_commits": total_commits,
            "last_commit": last_commit.isoformat() if last_commit else "No commits"
        }

    except Exception as e:
        return {"error": str(e)}
