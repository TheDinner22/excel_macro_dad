# get the filename of the excel spreadsheet from the 
# PUT-EXCEL-FILE-HERE dir

# dependencies
import os, sys

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # adds project dir to places it looks for the modules
sys.path.append(BASE_PATH)

# get the list of files from dir

dirname = "PUT-EXCEL-FILE-HERE"

dir_file_names = os.listdir(dirname)

if dir_file_names == []:
    wb_name = "none"
else:
    wb_name = os.path.join("PUT-EXCEL-FILE-HERE",dir_file_names[0])

dirs_paths = os.path.join(".data","test-sheet")
test_wb_name = os.path.join(dirs_paths,"test_sheet.xlsx")


