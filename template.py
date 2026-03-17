import os
from pathlib import Path
import logging

# Set up logging to see the progress in the terminal
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "medical_chatbot"

list_of_files = [
    "SRC/__init__.py",
    "SRC/helper.py",
    "SRC/prompt.py",
    ".env",
    "setup.py",
    "app.py",
    "research/trials.ipynb",
    "test.py"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    # Create the directory if it doesn't exist
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    # Create the file if it doesn't exist or is empty
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} is already exists")