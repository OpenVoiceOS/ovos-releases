import re
import subprocess

# Run pip list and filter for "ovos-" packages
with open('resolved-constraints.txt', 'r') as f:
    packages = f.readlines()

stable_constraints = [
    "onnxruntime<=1.20.1"  # 1.21.0 breaks raspberry pi
]

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
        if not alpha:
            stable_constraints.append(f"{name}>={minver},<{major}.{minor + 1}.0")
        else:
            stable_constraints.append(f"{name}<{major}.{minor + 1}.0")

# Write stable, testing and alpha constraints to respective files
with open('constraints-stable.txt', 'w') as stable_file:
    stable_file.write("\n".join(stable_constraints))

    
print("Constraints files generated: constraints-stable.txt")
