import folium
import requests
import pandas
from bs4 import BeautifulSoup  # process data

r = requests.get("https://www.worldometers.info/coronavirus/")
# <Response [404]> Bad
# <Response [200]> Good

# # receiving websites entire code
c = r.content

soup = BeautifulSoup(c, "html.parser")
# print(soup)


# find - finds only  first
# find_all - finds all


data = soup.find("tbody")
rows = data.find_all("tr", {"style": ""})

data_dict = {}

for item in rows:
    c_cases = item.find_all("td")[2].text
    c_name = item.find_all("td")[1].text

    data_dict[c_name] = int(c_cases.replace(",", ""))

    # data_dict = {c_name, c_cases}
    # key = c_name
    # value = c_cases
    # data_dict.update({key: value})

print(data_dict)

cdata = pandas.read_csv("countries.csv")
# print(cdata)

lat = list(cdata["latitude"])
lon = list(cdata["longitude"])
cnt = list(cdata["name"])

map = folium.Map(location=[32.2248, 46.626], zoom_start=6, tiles="Stamen Terrain")

fg = folium.FeatureGroup(name="My Markers")



def radius_gen(radius):
    return radius ** 0.20

def color_gen(num):
    if num < 10000:
        return "green"
    elif num < 100000:
        return "pink"
    elif num < 1000000:
        return "orange"
    elif num < 10000000:
        return "purple"
    else:
        return "red"

for lt, ln, ct in zip(lat, lon, cnt):

    if ct in data_dict.keys():
        fg.add_child(folium.CircleMarker(location=[lt, ln], popup=str(ct) + "\n" + str(data_dict[ct]),
                                         radius=radius_gen(data_dict[ct]),
                                         fill_color=color_gen(data_dict[ct]), color="#cc1e0e", fill_opacity=0.5))

map.add_child(fg)
map.save("CoronaMap.html")
