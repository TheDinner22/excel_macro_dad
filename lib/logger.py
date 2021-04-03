# log changes in log files

# dependencies
import os, sys

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # adds project dir to places it looks for the modules
sys.path.append(BASE_PATH)

from datetime import datetime

class Log_Maker(): # old dv list wont have none new dv list will have none
    def __init__(self,dv,old_dv_list,new_dv_list):
        self.current_datetime = str(datetime.now())
        self.log_file_path = ('.' + (os.path.join(os.path.join('.data','logs'),(self.current_datetime + '.log')).replace(':','-').split(".")[1] + ".log")).replace(' ', '_')
        self.recent_log_file_path = ('.' + (os.path.join(os.path.join('.data','logs'),('recent.log')).replace(':','-').split(".")[1] + ".log")).replace(' ', '_')
        self.dv = dv
        self.old_dv_list = old_dv_list
        self.new_dv_list = new_dv_list
    
    def update_time(self):
        self.current_datetime = str(datetime.now())
        self.log_file_path = ('.' + (os.path.join(os.path.join('.data','logs'),(self.current_datetime + '.log')).replace(':','-').split(".")[1] + ".log")).replace(' ', '_')
    
    def construct_line(self):
        if len(self.old_dv_list) == len(self.new_dv_list):
            line_changed_part = ''
            for x in range(len(self.new_dv_list)):
                cell_id = self.dv + str(x+1)
                current_old_element = self.old_dv_list[x]
                current_new_element = self.new_dv_list[x]
                if current_old_element.lower().strip() != current_new_element.lower().strip():
                    line_changed_part += 'changed cell ' + cell_id + ' from ' + current_old_element + ' to ' + current_new_element + "\n"
                
            if line_changed_part != '':
                line = '--------START LOG----------'

                line += '\nChanges made: ' + str(len(line_changed_part.split('\n')) - 1)
                line += '\nChanges were made in column ' + self.dv
                line += '\n'

                line += line_changed_part

                line += '\n--------END LOG----------'
                return line
            else:
                print('\033[91m'+"NO CHANGES WERE MADE\nNO LOG CREATED"+'\033[0m')
                return False
        else:
            raise Exception("Old dv list and new dv list were not equal in length")
    
    def create_unique_log(self):
        lines = self.construct_line()
        if lines:
            self.update_time()
            with open(self.log_file_path,'w') as file_object:
                file_object.write(lines)
        else:
            print('\033[91m'+"NO CHANGES WERE MADE\nNO LOG CREATED"+'\033[0m')
        
    
    def update_recent_log(self):
        lines = self.construct_line()
        if lines:
            self.update_time()
            with open(self.recent_log_file_path,"w") as file_object:
                file_object.write(lines)
        else:
            print('\033[91m'+"NO CHANGES WERE MADE\nNO LOG CREATED"+'\033[0m')

    def both(self):
        self.create_unique_log()
        self.update_recent_log()