import os

def create_user_file(name, content):
    folder_name = name.replace(" ", "_")  # Replace spaces with underscores
    os.makedirs(folder_name, exist_ok=True)  # Create folder if not exists

    file_path = os.path.join(folder_name, f"{name}.txt")  
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(content)
    
    print(f"File created: {file_path}")

# Example Usage
user_name = "John Doe"
user_input = "This is a sample portfolio data."

create_user_file(user_name, user_input)
