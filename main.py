import os
import subprocess
from datetime import datetime, timedelta

# Initialize variables
start_date = datetime(2023, 1, 1)
file_name = "commit_file.txt"
num_commits = 365

# Ensure the file exists
if not os.path.exists(file_name):
    with open(file_name, "w") as f:
        f.write("Initial commit\n")

# Loop to create commits
for i in range(num_commits):
    # Calculate the commit date
    commit_date = start_date + timedelta(days=i)
    formatted_date = commit_date.strftime("%Y-%m-%d %H:%M:%S")
    
    # Modify the file
    with open(file_name, "a") as f:
        f.write(f"Commit {i + 1} on {formatted_date}\n")
    
    # Stage the changes
    subprocess.run(["git", "add", "."], check=True)
    
    # Make the commit with a custom date
    subprocess.run(
        [
            "git", "commit", "-m", f"Commit {i + 1}",
            "--date", formatted_date
        ],
        check=True
    )
    
    # Print status
    print(f"Created commit {i + 1} with date {formatted_date}")

print("All commits created successfully!")
