import os
import sys
import logging

# Step 1: Create logging str
'''
1. time code excute
2. write log to file level - folder
3. Write log of module/file name
4. write log message
'''
logging_str=  "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

# Step 2: Create log directory
log_dir="logs"

log_filepath= os.path.join(log_dir, "running_log.log")

os.makedirs(log_dir, exist_ok=True)

# Step 3: Create logger and set its properties (level and formats)

logging.basicConfig(
     level= logging.INFO,
     format= logging_str,

     handlers=  [
          # Stream handler for stdout --> log in terminal
         logging.StreamHandler(sys.stdout),

          # File handler for log file --> log into a file in the repo folder
         logging.FileHandler(filename= log_filepath)
     ])
logger = logging.getLogger()


