# main replacement logic goes in here

# dependencies
import os, sys

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # adds project dir to places it looks for the modules
sys.path.append(BASE_PATH)

from lib.data import Data

class replacer():
    def __init__(self):
        self.iv = "Q"
        self.dv = "Z"