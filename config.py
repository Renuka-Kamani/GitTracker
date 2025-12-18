import os
from pathlib import Path

# GitHub Personal Access Token (you must set it as an environment variable)
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

# Directory for PDF reports
REPORT_DIR = Path("reports")
REPORT_DIR.mkdir(exist_ok=True)
