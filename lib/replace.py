# main replacement logic goes in here

# dependencies
import os, sys

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # adds project dir to places it looks for the modules
sys.path.append(BASE_PATH)

from lib.data import Data
from lib.filename_finder import wb_name
from lib.logger import Log_Maker

class Replacer():
    def __init__(self, wb_name, ws_name):
        self.iv = "O"
        self.dv = "X"
        self.data = Data(wb_name, ws_name)
        self.new_dv_list = []
        self.empty_char = 's'

    def strip_all_elements(self, untrimmed_list):
        """strip all elements of a list"""
        for x in range(len(untrimmed_list)):
            untrimmed_list[x] = untrimmed_list[x].strip()
        return untrimmed_list

    def replace_iv_dv(self):
        """if iv in dv, remove it from dv"""
        # get iv and dv columns
        iv_list = self.data.return_column_as_list(self.iv)
        dv_list = self.data.return_column_as_list(self.dv)

        # sanity check that both lists are the same
        if len(iv_list) == len(dv_list):
            # loop through iv's
            for x in range(len(iv_list)):
                # define what cells we are working with
                iv_cell = str(iv_list[x])
                dv_cell = str(dv_list[x])

                # if the cell is empty, don't even bother comparing
                if iv_cell.strip() != "":
                    iv_cell_authors_list = self.strip_all_elements(iv_cell.split(","))
                    dv_cell_authors_list = self.strip_all_elements(dv_cell.split(","))

                    # loop through the authors
                    for untrimmed_iv_author in iv_cell_authors_list:
                        trimmed_iv_author = untrimmed_iv_author.split("(")[0].strip()
                        # loop through the dv comparing the trimmed author to the dv's authors
                        for untrimmed_dv_author in range(len(dv_cell_authors_list)):
                            if untrimmed_dv_author >= len(dv_cell_authors_list):
                                break
                            untrimmed_dv_author = dv_cell_authors_list[untrimmed_dv_author]
                            trimmed_dv_author = untrimmed_dv_author.split("(")[0].strip()
                            if trimmed_dv_author.lower() == trimmed_iv_author.lower():
                                while True:
                                    try:
                                        dv_cell_authors_list.remove(untrimmed_dv_author)
                                    except ValueError:
                                        break
                    if len(dv_cell_authors_list) != 0 and len(dv_cell_authors_list) != 1:
                        new_dv_cell_str = ", ".join(dv_cell_authors_list)
                        if new_dv_cell_str == dv_cell:
                            self.new_dv_list.append("none")
                        else:    
                            self.new_dv_list.append(new_dv_cell_str.strip())
                    elif len(dv_cell_authors_list) == 0:
                        self.new_dv_list.append(self.empty_char)
                    elif len(dv_cell_authors_list) == 1:
                        if dv_cell_authors_list[0].strip() == '':
                            self.new_dv_list.append(self.empty_char)
                        else:
                            self.new_dv_list.append(dv_cell_authors_list[0].strip())
                else:
                    self.new_dv_list.append("none")
            # update the cells with their new values
            self.data.update_all_cells_in_column(self.dv,self.new_dv_list)

            # log the changes to the file system
            log = Log_Maker(self.dv,dv_list,self.new_dv_list)
            log.both()

            return self.new_dv_list
        else:
            raise Exception("column " + self.dv + " was not equal in length to column " + self.iv)

if __name__ == "__main__":
    rep = Replacer(wb_name,"poopPy")
    rep.replace_iv_dv()