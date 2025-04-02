import re
import subprocess

# Run pip list and filter for "ovos-" packages
result = subprocess.run(['pip', 'list', '--format=freeze'], capture_output=True, text=True)
packages = result.stdout.splitlines()


testing_constraints = []

# Regular expression to capture package name and version, with optional alpha tag
pattern = re.compile(r'^(ovos-[\w-]+)==(\d+)\.(\d+)\.(\d+)(a\d+)?$')

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
        testing_constraints.append(f"{name}>={minver},<{major+1}.0.0")


with open('constraints-testing.txt', 'w') as testing_file:
    testing_file.write("\n".join(testing_constraints))
    
print("Constraints files generated: constraints-testing.txt")
