"""
# Program Description
Program process world population data using some python modules, and then export processed data in Excel file.
"""
import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook
from openpyxl.styles import *
from openpyxl.worksheet.table import Table, TableStyleInfo

r = requests.get("https://www.worldometers.info/world-population/population-by-country")
c = r.text

soup = BeautifulSoup(c, "html.parser")

data = soup.find("tbody")
rows = data.find_all("tr")

all_countries_ls = []

for index, row in enumerate(rows, 1):
    columns = row.find_all("td")
    c = columns

    # print(f"{index} - {c[1].text} - {c[2].text} - {c[3].text}")

    country = columns[1].text
    population = columns[2].text.replace(",", "")
    percent = columns[3].text

    each_country_ls = [index, country, population, percent]

    all_countries_ls.append(each_country_ls)

# test code
"""
for item in all_countries_ls:
    print(item)
"""

# add table header beginning of table
all_countries_ls.insert(0, ["N", "Country", "Population", "Percentage"])

# print(all_countries_ls)

# create new variable
records = all_countries_ls

workbook = Workbook()

file_name = "population.xlsx"
workbook.save(file_name)

# rename excel sheet name
sheet = workbook["Sheet"]  # select working sheet
sheet.title = "Population"  # rename working sheet
sheet = workbook["Population"]  # select working sheet again

for item in records:
    sheet.append(item)

table = Table(displayName="Population_Data", ref="A1:D236")
style = TableStyleInfo(name="TableStyleMedium4", showRowStripes=True, showColumnStripes=True)

# style table
table.tableStyleInfo = style

# add sheet in excel
sheet.add_table(table)

font_styles_lower = Font(color="fc1303", bold=True)
font_styles_higher = Font(color="008c1e", bold=True)

for cell in range(2, 237):
    x = sheet[f"C{cell}"].value
    x = int(x)

    if x < 10000000:
        sheet[f"C{cell}"].font = font_styles_lower

    else:
        sheet[f"C{cell}"].font = font_styles_higher

workbook.save(file_name)
workbook.close()
