from github_utils import get_github_details
from pdf_report import generate_pdf

def main():
    print("=== GitHub Tracker ===")
    username = input("Enter GitHub username: ").strip()

    print(f"\nFetching data for {username} ...")
    data = get_github_details(username)

    if "error" in data:
        print("❌ Error:", data["error"])
    else:
        print(f"\nGitHub Username: {data['username']}")
        print(f"Total Repositories: {data['total_repos']}")
        print(f"Total Commits: {data['total_commits']}")
        print(f"Last Commit Date: {data['last_commit']}")
        generate_pdf(data)

if __name__ == "__main__":
    main()
