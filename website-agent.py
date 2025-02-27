import os
import json
import subprocess
from prompts.webApp import get_project_structure

def create_project_files(project_name, tech_stack):
    structure = get_project_structure(tech_stack)

    # Define the root folder inside 'app'
    root_folder = os.path.join("app", project_name)

    # Create the root folder
    os.makedirs(root_folder, exist_ok=True)

    # Create folders
    for folder in structure.get("folders", []):
        folder_path = os.path.join(root_folder, folder)  
        os.makedirs(folder_path, exist_ok=True)

    # Create files
    for file in structure.get("files", []):
        file_path = os.path.join(root_folder, file["path"])  
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(file["content"])  

    # Change directory to the project root
    os.chdir(root_folder)

    # Ensure package.json has browserslist
    package_json_path = os.path.join(root_folder, "package.json")
    if os.path.exists(package_json_path):
        with open(package_json_path, "r+", encoding="utf-8") as f:
            package_data = json.load(f)
            if "browserslist" not in package_data:
                package_data["browserslist"] = {
                    "production": [">0.2%", "not dead", "not op_mini all"],
                    "development": ["last 1 chrome version", "last 1 firefox version", "last 1 safari version"]
                }
                f.seek(0)
                json.dump(package_data, f, indent=2)
                f.truncate()

    # Install dependencies silently (avoid npm audit prompts)
    try:
        print("📦 Installing dependencies...")
        subprocess.run(["npm", "install", "--silent", "--no-audit"], check=True)  
    except subprocess.CalledProcessError as e:
        print(f"❌ Error installing dependencies: {e}")
        return "❌ Installation failed."

    # Build the project (avoid prompts)
    try:
        print("⚙️ Building the project...")
        subprocess.run(["npm", "run", "build"], check=True, input=b"n\n")  
    except subprocess.CalledProcessError as e:
        print(f"❌ Error during build: {e}")
        return "❌ Build failed."

    print(f"✅ Project '{project_name}' setup successfully!")
    return "✅ Project setup done successfully!"

# Example Usage
if __name__ == "__main__":
    project_name = "MyReactApp"
    tech_stack = "React app"
    response = create_project_files(project_name, tech_stack)
    print(response)
