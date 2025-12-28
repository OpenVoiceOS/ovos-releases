import re
import subprocess

# Run pip list and filter for "ovos-" packages
with open('resolved-constraints.txt', 'r') as f:
    packages = f.readlines()

alpha_constraints = []

# Regular expression to capture package name and version, with optional alpha tag
pattern = re.compile(r'^(ovos[\w-]+)==(\d+)\.(\d+)\.(\d+)(a\d+)?$')

for package in packages:
    match = pattern.match(package)
    if match:
        name, major, minor, patch, alpha = match.groups()
        minver = f"{major}.{minor}.{patch}"
        if alpha:
            minver += f"{alpha}"
        major = stable_major = int(major)
        minor = stable_minor = int(minor)
        patch = int(patch)
        print(package)
        alpha_constraints.append(f"{name}>={minver}")


# hivemind packages
pattern = re.compile(r'^(hivemind-[\w-]+)==(\d+)\.(\d+)\.(\d+)(a\d+)?$')

for package in packages:
    match = pattern.match(package)
    if match:
        name, major, minor, patch, alpha = match.groups()
        minver = f"{major}.{minor}.{patch}"
        if alpha:
            minver += f"{alpha}"
        major = stable_major = int(major)
        minor = stable_minor = int(minor)
        patch = int(patch)
        print(package)
        alpha_constraints.append(f"{name}>={minver}")
        
# Write alpha constraints to respective files

with open('constraints-alpha.txt', 'w') as alpha_file:
    alpha_file.write("\n".join(alpha_constraints))
    
print("Constraints files generated: constraints-alpha.txt")
