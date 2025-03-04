import os

# Define the project structure in a nested dictionary
project_structure = {
    "backend": {
        "Dockerfile": "",
        "app.py": "",
        "requirements.txt": "",
        "templates": {
            "index.html": "",
            "resume.html": ""
        },
        "static": {
            "css": {
                "style.css": ""
            },
            "js": {
                "script.js": ""
            }
        }
    },
    "frontend": {
        "Dockerfile": '',
        "default.conf": ''
    },
    "os": {
        "Dockerfile": ''
    },
    "docker-compose.yaml": '',
    "notes.txt" : ''
}


def create_structure(base_path, structure):
    """
    Recursively creates directories and files.
    
    Args:
        base_path (str): The root directory to start creating the structure.
        structure (dict): A nested dictionary representing the directory structure.
    """
    for name, content in structure.items():
        path = os.path.join(base_path, name)
        # If the content is a dictionary, it's a directory.
        if isinstance(content, dict):
            os.makedirs(path, exist_ok=True)
            print(f"Directory created: {path}")
            create_structure(path, content)  # Recursive call for nested structure
        else:
            # Create an empty file (or you can add starter code as content)
            with open(path, "w") as file:
                file.write(content)
            print(f"File created: {path}")

if __name__ == "__main__":
    # Start from the current directory
    create_structure(".", project_structure)
