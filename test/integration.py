# all integration tests

# dependencies
import openpyxl, os, sys

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # adds project dir to places it looks for the modules
sys.path.append(BASE_PATH)

from lib.data import Data
from lib.filename_finder import test_wb_name
from lib.replace import Replacer

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
    msg = str(outcome[0:9]) + " was not equal to " + str(expected_outcome)
    assert outcome[0:9] == expected_outcome, msg

    # write to column b with some none values
    new_cells = ['does','none','none','none','none','none','none','none','work?']
    expected_outcome = ["does","cool","me","tester","please","work","im","begging",'work?']

    # try to update the cells make sure to catch all errors
    try:
        data.update_all_cells_in_column("B",new_cells)
    except Exception as e:
        raise AssertionError(str(e))

    # read column b make sure that you get the expected outcome
    outcome = data.return_column_as_list("B")
    msg = str(outcome)[0:9] + " was not equal to " + str(expected_outcome)
    assert outcome[0:9] == expected_outcome, msg

    # reset column b to empty
    empty_list = ["","","","","","","","","",""] #TODO make this more robust
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

# Run the replace funtion, assert that the replaces happen correctly
def test2(done): # fails rn
    data = Data(test_wb_name,ws_name)
    replace = Replacer(test_wb_name,ws_name)
    iv = replace.iv
    dv = replace.dv

    # define input and expected out put
    iv_input = ["fizz, buzz, pop","pop","fiZZ, pop","fizz, buzz","18, pop, buzz","pop (fizz), 34","buzz","","fizz","fizz"]
    dv_input = ["pop","fizz (242), buzz","23, pop, pop","fuzz, buzz","23, 23, 23","pop, fizz, 34","BUZZ, FIZZ","","","fizz, fizz"]
    dv_expected_output = ['s', 'fizz (242), buzz', '23', 'fuzz', '23, 23, 23', 'fizz', 'FIZZ', '', 's', 's']
    empty_list = ["","","","","","","","","",""]

    # write inputs to the iv and dv columns
    data.update_all_cells_in_column(iv,iv_input)
    data.update_all_cells_in_column(dv,dv_input)

    # run replacer
    replace.replace_iv_dv()

    # get new dv column
    dv_output = data.return_column_as_list(dv)

    assert dv_output == dv_expected_output, "dv_output did not match the expected output when dv_output:\n"+str(dv_output)+"\nand expected output was:\n"+str(dv_expected_output)

    # replace the lines with empty strings
    data.update_all_cells_in_column(iv,empty_list)
    data.update_all_cells_in_column(dv,empty_list)

    # done
    done("Run the replace funtion, assert that the replaces happen correctly")
integration_tests["Run the replace funtion, assert that the replaces happen correctly"] = test2



# example test below

"""def one_plus_one_is_two(done):
    outcome = 1+1
    desired_outcome = 2
    assert outcome == desired_outcome, "1+1 was not equal to two"
    done("one plus one is equal to two")
integration_tests["one plus one is equal to two"] = one_plus_one_is_two"""