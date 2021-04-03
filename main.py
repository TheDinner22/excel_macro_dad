# main file with all da ez logic

# dependencies
import os, sys

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # adds project dir to places it looks for the modules
sys.path.append(BASE_PATH)

from lib.replace import Replacer
from lib.filename_finder import wb_name

class Main():
    def __init__(self):
        self.wb_name = wb_name

    def green(self, input_str):
        """log string in green"""
        input_str = str(input_str)
        print('\033[92m'+input_str+'\033[0m')
    
    def red(self, input_str):
        """log string in red"""
        input_str = str(input_str)
        print('\033[91m'+input_str+'\033[0m')
    
    def fix_Q_Z_colums(self,ws_name):
        self.rep = Replacer(self.wb_name,ws_name)
        self.rep.replace_iv_dv()

def view_most_recent_log():
    recent_log_name = os.path.join(os.path.join(".data",'logs'),'recent.log')
    with open(recent_log_name,'r') as fo:
        lines = fo.readlines()

    for x in range(3,int(lines[1].split(" ")[-1].replace("\n",'')) + 3):
        line = lines[x].replace("^|^",'\033[0m').replace("^^",'\033[92m').replace("||",'\033[91m')
        print(line)
        

if __name__ == "__main__":
    main = Main()
    while True:
        raw_command = input("$")

        if raw_command.strip().lower() == 'exit':
            sys.exit(0)
        elif raw_command.strip().lower() == 'run':
            name = input("What is the work-sheet name?:").strip()
            main.fix_Q_Z_colums(name)
        elif raw_command.strip().lower() == 'help':
            print('"run" to fix the columns\n"exit" to exit\n"log" to view the most recent log with color')
        elif raw_command.strip().lower() == 'log':
            view_most_recent_log()