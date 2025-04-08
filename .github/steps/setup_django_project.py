import os
import subprocess

# Define project and app names
project_name = "octofit-tracker"
app_name = "octofit-tracker"
base_dir = (
    "/workspaces/skills-build-applications-w-copilot-agent-mode/octofit-tracker/backend"
)

# Step 1: Create the project directory
os.makedirs(base_dir, exist_ok=True)

# Step 2: Initialize Django project
subprocess.run(["django-admin", "startproject", project_name, base_dir])

# Step 3: Create the Django app
project_dir = os.path.join(base_dir, project_name)
subprocess.run(["python", "manage.py", "startapp", app_name], cwd=project_dir)

# Step 4: Update settings.py to include the app
settings_path = os.path.join(project_dir, project_name, "settings.py")
with open(settings_path, "a") as settings_file:
    settings_file.write(f"\nINSTALLED_APPS.append('{app_name}')\n")

print("Django project and app setup complete.")
