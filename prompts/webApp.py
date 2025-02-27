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
    You are an expert software architect. Generate a **clean and runnable** folder & file structure for a **{tech_stack}** project.

    **Rules:**
    - Return **only** valid JSON.
    - No duplicate folders or files.
    - No extra characters like quotes (`"`), slashes (`/`), or comments (`#`).
    - Each file should contain necessary code to run the project.
    - Include `package.json` with correct scripts and dependencies.

    **Example JSON format:**
    ```json
    {{
        "root": "MyProject",
        "folders": [
            "src",
            "src/components",
            "src/pages",
            "public"
        ],
        "files": [
            {{
                "path": "package.json",
                "content": "{{
                    \\"name\\": \\"my-app\\",
                    \\"version\\": \\"1.0.0\\",
                    \\"scripts\\": {{
                        \\"start\\": \\"react-scripts start\\",
                        \\"build\\": \\"react-scripts build\\",
                        \\"test\\": \\"react-scripts test\\",
                        \\"eject\\": \\"react-scripts eject\\"
                    }},
                    \\"dependencies\\": {{
                        \\"react\\": \\"^18.0.0\\",
                        \\"react-dom\\": \\"^18.0.0\\",
                        \\"react-scripts\\": \\"5.0.1\\"
                    }}
                }}"
            }},
            {{
                "path": "src/index.js",
                "content": "import React from 'react';\\nimport ReactDOM from 'react-dom/client';\\nimport App from './App';\\n\\nconst root = ReactDOM.createRoot(document.getElementById('root'));\\nroot.render(<App />);"
            }},
            {{
                "path": "src/App.js",
                "content": "import React from 'react';\\n\\nfunction App() {{\\n  return <h1>Hello, React!</h1>;\\n}}\\n\\nexport default App;"
            }},
            {{
                "path": "public/index.html",
                "content": "<!DOCTYPE html>\\n<html lang='en'>\\n<head>\\n<meta charset='UTF-8'>\\n<meta name='viewport' content='width=device-width, initial-scale=1.0'>\\n<title>My React App</title>\\n</head>\\n<body>\\n<div id='root'></div>\\n</body>\\n</html>"
            }}
        ]
    }}
    ```
    
    Generate a similar clean and **runnable** project structure for a {tech_stack} project.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return json.loads(response.choices[0].message.content)  # Convert response to JSON
