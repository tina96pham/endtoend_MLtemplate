# Step1: Libraries to track files creates in repo/folder

import os
from pathlib import Path
import logging

# Step 2: Record logging events in a file. 
# For configuration check library documentation: https://docs.python.org/3/howto/logging.html

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]:%(message)s:')

# Step 3: Create project file structure
project_name= "mlProject"

list_of_files= [
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
    "templates/index.html"
]

# Step 4: Python logic to create all the files
''' for filepath in the list_of_file 
    1. convert path to be unversal using python library Path ( window file path is fpward slash)
    2. seprate folfer and file
    3. Create file directories if not exist
    4. Create the file by checking file existence and if exist file size need to be 0 to make sure bot wiping out file with work 
'''

for filepath in list_of_files:
    filepath= Path(filepath)

    filedir, filename= os.path.split(filepath)
    # Create directories if they don't exist already
    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info (f"Creating directory; {filedir} for the file:  {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with  open(filepath, 'w', encoding='utf8') as f:
            pass
            logging.info(f"Creating an empty file :{filename}")
    else:
        logging.debug(f"{filename} already exists.")