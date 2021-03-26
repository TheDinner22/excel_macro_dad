# the file system so that we can crud excel files 

# dependencies
import openpyxl, os, sys

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # adds project dir to places it looks for the modules
sys.path.append(BASE_PATH)

class Data():
    """the fs for excel files"""
    def __init__(self, filename, ws_name):
        self.filename = filename + ".xlsx" # TODO decide if extension is provided by user later on
        self.file_path = os.path.join("PUT-EXCEL-FILE-HERE",self.filename)
        self.wb = openpyxl.load_workbook(self.file_path)
        self.ws = ""
        
        # set the active sheet to the one requested, if it does not exist: err
        
        sheets =  self.wb.sheetnames
        for sheet in sheets:
            if ws_name == sheet:
                self.ws = self.wb[sheet]

        if self.ws == "":
            raise Exception('That sheet name does not exist')


    def return_column_as_list(self, column_letter):
        """get a column by letter, each row is an element in a list"""
        # sanity check column_letter
        acceptable_letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        if not column_letter in acceptable_letters: # note, this means AA is invalid
            raise Exception("Invalid column letter(s)")
        
        column = self.ws[column_letter]
        column_list = []
        for cell in column:
            val = cell.value if cell.value != None else ""
            column_list.append(val)
        return column_list

    def update_all_cells_in_column(self):
        """update a specific cell to a new value"""
        pass

# TODO del me
data = Data("Book1","poopPy")
col = data.return_column_as_list('Q')
print(col)