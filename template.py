import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO , format='%(asctime)s - %(levelname)s - %(message)s')

project_name = "mlProject"

list_of_files = [
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "app.py",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html",
    "test.py"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    file_dir , file = os.path.split(filepath)

    if file_dir != "":
        os.makedirs(file_dir , exist_ok=True)

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Created file: {filepath}")

    else:
        logging.info(f"File {filepath} already exists")