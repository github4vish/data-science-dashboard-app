import os
from pathlib import Path


def create_project(project_name):
    base_path = Path(project_name)

    folders = [
        "models",
        "data",
        "tests",
        "static/js",
        "templates"
    ]

    files = {
        "app.py": "",
        "requirements.txt": "",
        "tests/APITest.http": "",
        "templates/index.html": "",
        "static/js/dashboard.js": ""
    }

    # Create base directory
    base_path.mkdir(exist_ok=True)

    # Create folders
    for folder in folders:
        (base_path / folder).mkdir(parents=True, exist_ok=True)

    # Create empty files
    for file_path, content in files.items():
        file_full_path = base_path / file_path
        file_full_path.parent.mkdir(parents=True, exist_ok=True)
        file_full_path.write_text(content)

    print(f"\n✅ Project '{project_name}' created successfully!\n")