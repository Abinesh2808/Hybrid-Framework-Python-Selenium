from xlrd import *
from Generic.Logs import *
import yaml


def read_locator(data):
    with open(r"../Data/Locators.yml") as file:
        d = yaml.safe_load(file)

    if data in d:
        return d[data]
    else:
        log("error", "Invalid Data Name")
        raise Exception("Invalid Data Name")


def read_testdata(data):
    with open(r"../Data/Testdata.yml") as file:
        d = yaml.safe_load(file)

    if data in d:
        return d[data]
    else:
        log("error", "Invalid Data Name")
        raise Exception("Invalid Data Name")
