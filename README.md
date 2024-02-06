## Overview
1. Repo Setup
2. Project Template creation
3. Project setup
4. Loggin, Exception and Utility
5. Project Workflow
6. Notebooks Experiment
7. Component Implementation
    - Data Ingestion
    - Data Validation
    - Data Transformation
    - Model Training
    - Model Evaluation
8. Training Pipeline
9. Prediction Pipeline
10. User app implementaion
11. Dockerization
12. Deployment on AWS CI/CD

End to End Implementation:
1. Project Structure should not be fixed
2. Why oops concept is required for end to end implementation


## 1. Repo SetUp
- Step 1:. Use GitHub to create a new repo  with the desired project name. 
- Step 2: Then use Git Bash or Command Prompt to clone that repository onto your local environment/computer
    ```bash
     git clone <HTTP/SSH link>
    ```
    - The local should have:
        -  README.md (Mandatory)
        - .gitignore (Optional but recommended)
        -  LICENSE (Optional but recommended) --> LICENSE is setup during the creation of the repo
## 2. Template SetUp
- Create template.py
- Follow the structure from template.py
- Automation to create folder or file by running the file
    ```python template.py```
    This will create a basic project structure with all necessary files in place
    - Update repo 
    ```bash 
    git add .
    ```
    ```bash 
    git commit -m <message>
    ```
    ``` bash
    git push origin main 
    ```
### 3. Project setup
- Step 1: Create Virtual environment
 ```bash
 conda create -n <envname/project_name> python=<version> 
 #Example : conda create -n mlProject python=3.8 -y
 ```
- Step 2: Activate  the virtual environment
```bash
 conda activate <envname>
```
OR 
    1. CTRL/CMD + SHIFT + P
    2. Type : Select Interpreter
    3. Choose the created env

- Step 3: Set up requirement.txt to include all the python libraries package with version use in the project. 
```bash 
pip install -r requirements.txt
```
<p> NOTE: Please look up packages that you need. What include in the repo is just for practical purposes.<p>

- Step 4: Create setup.py
    - Following this guide https://packaging.python.org/tutorials/packaging-projects/
    - Run setup.py to allow calling function from other file
    ```bash
     python setup.py install
     ``` 
    - Ex: calling function from src/mlProject/config/configuration
    ```python 
    from src.mlProject.config import configuration
    ```

### 4.1 Logging
- Install logging package (https://docs.python.org/3/library/logging.html
- Located src/mlProject/__init__.py 
```python 
from mlProject import logger 
```
- create logging folder
```python
from src.mlProject.logging import logger
```
- Control work from different components of work

### 4.2 Exception
- Using python box to set up 
- If not custom exception can be put into config

### 4.3 Utility
- Create utility for frequent use code to access in different components of the project in common.py
- Use for common utility in the project such as load json file,... ensure production grade code

### 6 Workflow
1. update config.yaml
2. update schema.yaml 
    - In schema: include columns and target columns and data type
3. update params.yaml
4. update the entity
5. update the configuration manager in src config
6. update the components
7. update the pipeline
8. update the main.py
9. update the app.py

### 7.1 Data Ingestion




# 6. Notebook Experiment
- EDA with jupyter
- include data in the research folder


