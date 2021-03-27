# all unit tests
unit_tests = {}

# dependencies
import os, sys

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # adds project dir to places it looks for the modules
sys.path.append(BASE_PATH)

from lib.data import Data

# return_column_as_list should throw if given any non-capital letter
def return_column_as_list_throws(done):
    # create instance of data class
    data = Data("Book1","poopPy")
    
    # list of all invalid inputs
    invalid_inputs = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","1","2","3","4","5","6",6,4,3,98,23894,"7","8","9","AB","AA","11","aa","#","$","##A","AS",]
    for invalid_input in invalid_inputs:
        try:
            data.return_column_as_list(invalid_input)
            raise AssertionError("return_column_as_list did not throw (it should have) when given input: " + str(invalid_input))
        except Exception as e:
            # it will catch the Assertion error
            msg = "return_column_as_list did not throw (it should have) when given input: " + str(invalid_input)
            if str(e) == msg:
                raise AssertionError("return_column_as_list did not throw (it should have) when given input: " + str(invalid_input))         
    done("return_column_as_list should throw if it is passed anything but a non-capital letter")
unit_tests["return_column_as_list should throw if it is passed anything but a non-capital letter"] = return_column_as_list_throws

# update_all_cells_in_column should throw if given any non-capital letter
def update_all_cells_in_column_throws(done):
    # create instance of data class
    data = Data("Book1","poopPy")
    
    # list of all invalid inputs
    invalid_inputs = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","1","2","3","4","5","6","7","8",1,2,3,243,"9","AB","AA","11","aa","#","$","##A","AS",]
    for invalid_input in invalid_inputs:
        try:
            data.update_all_cells_in_column(invalid_input,["tester"])
            raise AssertionError("update_all_cells_in_column did not throw (it should have) when given input: " + str(invalid_input))
        except Exception as e:
            # it will catch the Assertion error
            msg = "update_all_cells_in_column did not throw (it should have) when given input: " + str(invalid_input)
            if str(e) == msg:
                raise AssertionError("update_all_cells_in_column did not throw (it should have) when given input: " + str(invalid_input))         
    done("update_all_cells_in_column should throw if it is passed anything but a non-capital letter")
unit_tests["update_all_cells_in_column should throw if it is passed anything but a non-capital letter"] = update_all_cells_in_column_throws

# update_all_cells_in_column should throw if the second argument is: empty list, not a list, very long list
def update_all_cells_in_column_throws_param2(done):
    # create instance of data class
    data = Data("Book1","poopPy")
    
    # list of all invalid inputs
    long_list = ["im long","im long","im long","im long","im long","im long","im long","im long","im long","im long","im long","im long","im long","im long","im long","im long","im long","im long","im long","im long","im long","im long","im long","im long","im long","im long","im long","im long","im long","im long","im long","im long","im long","im long","im long","im long","im long","im long","im long","im long","im long","im long","im long","im long","im long","im long","im long","im long","im long","im long","im long","im long","im long","im long","im long","im long","im long","im long","im long","im long","im long","im long","im long","im long","im long","im long","im long","im long","im long","im long","im long","im long","im long","im long","im long","im long","im long","im long","im long","im long","im long","im long","im long","im long","im long","im long","im long","im long","im long","im long","im long","im long","im long","im long","im long","im long","im long","im long","im long","im long"]
    invalid_inputs = [long_list,[],"a","b",1,2,6,243,"c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","1","2","3","4","5","6","7","8","9","AB","AA","11","aa","#","$","##A","AS",]
    for invalid_input in invalid_inputs:
        try:
            data.update_all_cells_in_column('A',invalid_input)
            raise AssertionError("update_all_cells_in_column did not throw (it should have) when given input: " + str(invalid_input))
        except Exception as e:
            # it will catch the Assertion error
            msg = "update_all_cells_in_column did not throw (it should have) when given input: " + str(invalid_input)
            if str(e) == msg:
                raise AssertionError("update_all_cells_in_column did not throw (it should have) when given input: " + str(invalid_input))         
    done("update_all_cells_in_column should throw if the second argument is: empty list, not a list, very long list")
unit_tests["update_all_cells_in_column should throw if the second argument is: empty list, not a list, very long list"] = update_all_cells_in_column_throws_param2



# ignore tests below me 
"""
def one_plus_one_is_two(done):
    outcome = 1+1
    desired_outcome = 2
    assert outcome == desired_outcome, "1+1 was not equal to two"
    done("one plus one is equal to two")
unit_tests["one plus one is equal to two"] = one_plus_one_is_two

def one_plus_one_is_three(done):
    outcome = 1+1
    desired_outcome = 3
    assert outcome == desired_outcome, "1+1 was not equal to three"
    done("one plus one is equal to three")
unit_tests["one plus one is equal to three"] = one_plus_one_is_three
"""