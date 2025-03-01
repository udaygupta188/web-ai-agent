import os
import openai
import json
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()

# Initialize OpenAI client
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_project_structure(tech_stack):
    prompt = f"""
    You are an expert software architect. Based on the provided tech stack, generate a clean, runnable, and dynamic project structure tailored to a {tech_stack} project.

    **Rules:**
    - Return only valid JSON.
    - Do not include duplicate folders or files.
    - Do not output extra characters (like quotes, slashes, or comments) outside the valid JSON.
    - The JSON should include two keys:
         - "folders": an array of folder paths.
         - "files": an array of objects, each having "path" and "content".
    - If the tech stack uses a package manager (e.g., npm, yarn), include a configuration file (like package.json) with appropriate scripts, dependencies, and necessary configurations (e.g., browserslist for React).
    - Adapt the structure to the tech stack:
         - For React, include folders like "src" and "public" and files such as "src/index.js", "src/App.js", etc.
         - For Angular, include "src/app", "angular.json", etc.
         - For Vue, include "src", "public", etc.
         - For other stacks, generate a suitable structure.

    **Example for a React project:**
    {{
        "folders": ["src", "public", "src/components", "src/pages"],
        "files": [
            {{
                "path": "package.json",
                "content": "{{ \\"name\\": \\"my-react-app\\", \\"version\\": \\"1.0.0\\", \\"scripts\\": {{ \\"start\\": \\"react-scripts start\\", \\"build\\": \\"react-scripts build\\" }}, \\"dependencies\\": {{ \\"react\\": \\"^18.0.0\\", \\"react-dom\\": \\"^18.0.0\\" }} }}"
            }},
            {{
                "path": "src/index.js",
                "content": "import React from 'react';\\nimport ReactDOM from 'react-dom/client';\\nimport App from './App';\\nconst root = ReactDOM.createRoot(document.getElementById('root'));\\nroot.render(<App />);"
            }},
            {{
                "path": "src/App.js",
                "content": "import React from 'react';\\nfunction App() {{ return <h1>Hello, React!</h1>; }}\\nexport default App;"
            }},
            {{
                "path": "public/index.html",
                "content": "<!DOCTYPE html>\\n<html lang='en'>\\n<head><meta charset='UTF-8'><meta name='viewport' content='width=device-width, initial-scale=1.0'><title>My React App</title></head>\\n<body><div id='root'></div></body></html>"
            }}
        ]
    }}

    Generate a similar dynamic and runnable project structure for a {tech_stack} project.
    """
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return json.loads(response.choices[0].message.content)
