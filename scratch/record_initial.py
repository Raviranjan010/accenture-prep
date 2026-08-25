import os

# Record initial line counts
initial_counts = {}
files_to_update = [
    '02-technical-coding/cs-fundamentals/oop-concepts.md',
    '02-technical-coding/cs-fundamentals/dbms-normalization-joins.md',
    '02-technical-coding/cs-fundamentals/os-basics.md',
    '02-technical-coding/cs-fundamentals/networking-basics.md'
]

for path in files_to_update:
    with open(path, 'r', encoding='utf-8') as f:
        initial_counts[path] = len(f.readlines())

print("Initial line counts recorded:", initial_counts)
