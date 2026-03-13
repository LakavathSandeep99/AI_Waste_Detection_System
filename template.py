import os
from pathlib import Path
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

project_name = "AI_Waste_Detection_System"

list_of_files = [
    ".github/workflows/.gitkeep",
    "data/.gitkeep",
    f"{project_name}/__init__.py",
    f"{project_name}/components/__init__.py",
    f"{project_name}/components/data_ingestion.py",
    f"{project_name}/components/data_validation.py",
    f"{project_name}/components/data_trainer.py",
    f"{project_name}/constants/__init__.py",
    f"{project_name}/constants/training_pipeline/__init__.py",
    f"{project_name}/constants/application.py",
    f"{project_name}/entity/config_entity.py",
    f"{project_name}/entity/artifact_entity.py",
    f"{project_name}/exceptions/__init__.py",
    f"{project_name}/logger/__init__.py",
    f"{project_name}/pipline/__init__.py",          # Note: 'pipline' is kept as per your original list
    f"{project_name}/pipline/training_pipeline.py",
    f"{project_name}/utils/__init__.py",
    f"{project_name}/utils/main_utils.py",
    "templates/index.html",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
]

for filepath in list_of_files:
    filepath = Path(filepath)                # Convert to Path object for easier handling
    filedir = filepath.parent
    filename = filepath.name

    # Create directory if it does not exist
    if filedir != Path(""):                  # Equivalent to checking if filedir is not empty
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file: {filename}")

    # Create the file only if it doesn't exist OR it exists but is empty
    if not filepath.exists() or filepath.stat().st_size == 0:
        with open(filepath, "w") as f:
            pass
        logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} already exists and is not empty, skipping.")