import glob
import os

try:
    with open('target_filename.txt', 'r') as f:
        target_filename = f.read().strip()
except FileNotFoundError:
    print("Error: target_filename.txt not found.")
    exit(1)

batch_files = sorted(glob.glob('batch_*.txt'))

if not batch_files:
    print("Error: No batch files found.")
    exit(1)

contents = []
for filename in batch_files:
    with open(filename, 'r') as f:
        content = f.read().strip()
        if content:
            contents.append(content)

final_content = '\n\n--------------------\n\n'.join(contents)
# Make sure it ends with a newline
final_content += '\n'

with open(target_filename, 'w') as f:
    f.write(final_content)

print(f"Successfully combined {len(batch_files)} batch files into {target_filename}")
