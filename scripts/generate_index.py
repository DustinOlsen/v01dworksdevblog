import os
import json
import re

# Configuration
CONTENT_DIR = '../content/posts'
OUTPUT_FILE = '../apps/blogs/posts.json'

# Regex to parse frontmatter (simple version)
# Looks for content between two --- lines at the start of the file
FRONTMATTER_PATTERN = re.compile(r'^---\s*\n(.*?)\n---\s*\n', re.DOTALL)

def parse_frontmatter(content):
    match = FRONTMATTER_PATTERN.match(content)
    metadata = {}
    if match:
        yaml_block = match.group(1)
        for line in yaml_block.split('\n'):
            if ':' in line:
                key, value = line.split(':', 1)
                metadata[key.strip()] = value.strip().strip('"').strip("'")
    return metadata

def generate_index():
    posts = []
    
    # Walk through the content directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    abs_content_dir = os.path.join(script_dir, CONTENT_DIR)
    
    print(f"Scanning {abs_content_dir}...")

    for root, dirs, files in os.walk(abs_content_dir):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    
                metadata = parse_frontmatter(content)
                
                # Only add if we found a title
                if 'title' in metadata:
                    # Calculate relative path for the browser
                    # We want: /content/posts/category/filename.md
                    rel_path = os.path.relpath(file_path, os.path.join(script_dir, '..'))
                    web_path = '/' + rel_path
                    
                    post_entry = {
                        'title': metadata.get('title', 'Untitled'),
                        'date': metadata.get('date', ''),
                        'category': metadata.get('category', 'tech'),
                        'excerpt': metadata.get('excerpt', ''),
                        'path': web_path
                    }
                    posts.append(post_entry)
                    print(f"Found: {post_entry['title']}")

    # Sort by date (newest first)
    posts.sort(key=lambda x: x['date'], reverse=True)

    # Write to JSON file
    abs_output_file = os.path.join(script_dir, OUTPUT_FILE)
    with open(abs_output_file, 'w', encoding='utf-8') as f:
        json.dump(posts, f, indent=4)
        
    print(f"Successfully generated index with {len(posts)} posts at {OUTPUT_FILE}")

if __name__ == "__main__":
    generate_index()