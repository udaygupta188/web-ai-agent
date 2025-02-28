# **AI Agent for Web Application Setup** 🚀  

This AI Agent automates the process of creating and setting up a web application using different tech stacks. It initializes the project structure, installs dependencies, and builds the project.  

## **Features**  
👉 Automatically generates project files and folders based on the selected tech stack.  
👉 Installs required dependencies without manual intervention.  
👉 Configures `package.json` to avoid build errors (e.g., missing `browserslist`).  
👉 Runs the build process and provides real-time status updates.  

## **Installation**  
### **1. Clone the Repository**  
```bash
git clone https://github.com/udaygupta188/web-ai-agent.git
cd web-ai-agent
```

### **2. Create a Virtual Environment (Optional but Recommended)**  
```bash
python3 -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate  # On Windows
```

### **3. Install Dependencies**  
```bash
pip install -r requirements.txt
```
### **4. Create .env file**  
``` Create .env file and add  OPENAI_API_KEY

## **Usage**  
Run the script to create and set up a project:  
```bash
python website-agent.py
```

The script will:  
1. Ask for the **project name** and **tech stack**.  
2. Generate the required **folders and files**.  
3. Install dependencies.  
4. Build the project automatically.  
5. Display **"✅ Project setup done successfully!"** once everything is complete.  

## **Example**  
To create a React project:  
```bash
python website-agent.py
```
Output:  
```
🛂 Installing dependencies...
⚙️ Building the project...
👉 Project 'MyReactApp' setup successfully!
```

## **Troubleshooting**  
- If you get `browserslist` errors, ensure the script correctly updates `package.json`.  
- Run `npm install` manually if dependencies fail to install.  
- Ensure you have `Node.js` and `npm` installed before running the script.  

## **License**  
This project is open-source and available under the **MIT License**.  