from xlrd import *
from Generic.Logs import *
import json


def read_locator(data):
    with open(r"../Data/Locators.json") as file:
        d = json.load(file)

    if data in d:
        return d[data]
    else:
        log("error", "Invalid Data Name")
        raise Exception("Invalid Data Name")


def read_testdata(data):
    with open(r"../Data/Testdata.json") as file:
        d = json.load(file)

    if data in d:
        return d[data]
    else:
        log("error", "Invalid Data Name")
        raise Exception("Invalid Data Name")
