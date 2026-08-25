import os
import re
import shutil

md_files = []
for root, dirs, files in os.walk('.'):
    if '.git' in dirs:
        dirs.remove('.git')
    if 'scratch' in dirs:
        dirs.remove('scratch')
    for f in files:
        if f.endswith('.md'):
            md_files.append(os.path.normpath(os.path.join(root, f)))

print(f"Auditing {len(md_files)} markdown files...\n")

broken_links = []
placeholder_issues = []
link_pattern = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')

for path in md_files:
    dir_name = os.path.dirname(path)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    matches = link_pattern.findall(content)
    for text, target in matches:
        if target.startswith(('http://', 'https://', 'mailto:', '#')):
            continue
        target_path = target.split('#')[0]
        if not target_path:
            continue
        resolved_path = os.path.normpath(os.path.join(dir_name, target_path))
        if not os.path.exists(resolved_path):
            broken_links.append((path, target, resolved_path))

    if 'TODO' in content:
        placeholder_issues.append((path, 'Contains TODO'))

print(f"=== BROKEN LINKS ({len(broken_links)}) ===")
for src, target, res in broken_links:
    print(f"In {src}: link '{target}' -> resolved '{res}' (NOT FOUND)")

print(f"\n=== PLACEHOLDER / TODO ISSUES ({len(placeholder_issues)}) ===")
for src, issue in placeholder_issues:
    print(f"In {src}: {issue}")

print("\nAudit finished.")
