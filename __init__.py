import os
import sys

# Get the directory of the current script (or where the file is)
current_file_directory = os.path.dirname(os.path.abspath(__file__))

# Add this directory to sys.path
sys.path.append(current_file_directory)
