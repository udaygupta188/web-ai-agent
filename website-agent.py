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

    # Install dependencies (e.g., npm install for React)
    try:
        print("📦 Installing dependencies...")
        subprocess.run(["npm", "install"], check=True)  # Adjust based on tech stack
    except subprocess.CalledProcessError as e:
        print(f"❌ Error installing dependencies: {e}")
        return "❌ Installation failed."

    # Build the project (if needed)
    try:
        print("⚙️ Building the project...")
        subprocess.run(["npm", "run", "build"], check=True)  # Adjust for different tech stacks
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
