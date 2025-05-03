import pkg_resources

output = "\n".join(sorted(f"{pkg.key}=={pkg.version}" for pkg in pkg_resources.working_set))

with open("requirements.txt", "w") as f:
    f.write(output)

print("✅ requirements.txt updated with all installed packages.")
# This script generates a requirements.txt file with all installed packages in the current environment.
# It uses the pkg_resources module to list all packages and their versions.