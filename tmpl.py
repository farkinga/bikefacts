import os
from datetime import datetime

# Define the directory where your posts are stored
posts_dir = "_posts"

# Check if the directory exists, create it if not
if not os.path.exists(posts_dir):
os.makedirs(posts_dir)

# Get a list of existing post files in the directory
existing_posts = [f for f in os.listdir(posts_dir) if f.endswith(".md")]

# Extract and sort the numbers from the existing posts to find the next available number
post_numbers = sorted([int(os.path.splitext(f)[0].split('-')[1]) for f in existing_posts], reverse=True)
next_number = 1 if not post_numbers else post_numbers[0] + 1

# Generate the new post filename and content
new_post_filename = "fact-list.py"
new_post_content = f"""---
layout: default
title: Fact {next_number} - Title Goes Here
date: {datetime.now().strftime('%Y-%m-%d')}
number: {next_number}
---

Write your content here...
"""

# Write the new post to a file in the posts directory
with open(os.path.join(posts_dir, new_post_filename), "w") as f:
f.write(new_post_content)

print(f"New post created: {new_post_filename}")
