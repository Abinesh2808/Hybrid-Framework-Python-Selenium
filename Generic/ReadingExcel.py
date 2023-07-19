from xlrd import *
from Generic.Logs import *

def read_locator(sname):
    try:
        wb = open_workbook("../Excel/Locators.xlsx")
        sh = wb.sheet_by_name(sname)
        rw = sh.get_rows()
        next(rw)
        d = {row[0].value:(row[1].value,row[2].value) for row in rw}
        log("info", "Reading Data From Excel")
        return d
    except:
        log("error", "Invalid Sheet Name")

def read_testdata(sname):
    try:
        wb = open_workbook("../Excel/Testdata.xlsx")
        sh = wb.sheet_by_name(sname)
        rw = sh.get_rows()
        next(rw)
        d = {row[0].value:row[1].value for row in rw}
        log("info", "Reading Data From Excel")
        return d
    except:
        log("error", "Invalid Sheet Name")