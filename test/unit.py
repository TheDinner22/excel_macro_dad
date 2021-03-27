# all unit tests
unit_tests = {}

# dependencies
import os, sys, unittest

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # adds project dir to places it looks for the modules
sys.path.append(BASE_PATH)

from lib.data import Data

# return_column_as_list should throw if given any non-capital letter
def return_column_as_list_does_not_throw(done):
    # create instance of data class
    data = Data("Book1","poopPy")
    
    # list of all invalid inputs
    invalid_inputs = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","1","2","3","4","5","6","7","8","9","AB","AA","11","aa","#","$","##A","AS",]
    for invalid_input in invalid_inputs:
        try:
            data.return_column_as_list(invalid_input)
            raise AssertionError("return_column_as_list did not throw (it should have) when given input: " + invalid_input)
        except Exception:
            continue
    done("return_column_as_list should throw if it is passed anything but a non-capital letter")

unit_tests["return_column_as_list should throw if it is passed anything but a non-capital letter"] = return_column_as_list_does_not_throw




# ignore tests below me 
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