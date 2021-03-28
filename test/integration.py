# all integration tests

# dependencies
import openpyxl, os, sys

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # adds project dir to places it looks for the modules
sys.path.append(BASE_PATH)

from lib.data import Data
from lib.filename_finder import test_wb_name

# ws name
ws_name = "test"

# integration tests container
integration_tests = {}

# write to an excel file, read what was written and confirm it worked well
def test1(done):
    data = Data(test_wb_name, ws_name)

    # write to column b
    expected_outcome = ["thedinner","cool","me","tester","please","work","im","begging",'you']
    
    # try to update the cells make sure to catch all errors
    try:
        data.update_all_cells_in_column("B",expected_outcome)
    except Exception as e:
        raise AssertionError(str(e))

    # read column b make sure that you get the expected outcome
    outcome = data.return_column_as_list("B")
    msg = str(outcome) + " was not equal to " + str(expected_outcome)
    assert outcome == expected_outcome, msg

    # reset column b to empty
    empty_list = ["","","","","","","","",""]
    try:
        data.update_all_cells_in_column('B',empty_list)
    except Exception as e:
        raise AssertionError(str(e))

    # read column b assert that its empty
    outcome = data.return_column_as_list("B")
    msg = str(outcome) + " was not equal to " + str(empty_list)
    assert outcome == empty_list, msg

    done("Series of reads and writes to excel file. The reads make sure that the writes actually worked.")
integration_tests["Series of reads and writes to excel file. The reads make sure that the writes actually worked."] = test1




# example test below

"""def one_plus_one_is_two(done):
    outcome = 1+1
    desired_outcome = 2
    assert outcome == desired_outcome, "1+1 was not equal to two"
    done("one plus one is equal to two")
integration_tests["one plus one is equal to two"] = one_plus_one_is_two"""