"""
# Program Description


"""
import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook
from openpyxl.styles import *
from openpyxl.worksheet.table import Table, TableStyleInfo


r = requests.get("https://www.worldometers.info/world-population/")

print(r)

