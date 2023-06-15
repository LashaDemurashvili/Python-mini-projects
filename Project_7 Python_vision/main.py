import folium
import requests
from bs4 import BeautifulSoup  # process data

r = requests.get("https://www.worldometers.info/coronavirus/")
# <Response [404]> Bad
# <Response [200]> Good

# # receiving websites entire code
c = r.content

soup = BeautifulSoup(c, "html.parser")
# print(soup)

"""
# find - finds only  first 
# find_all - finds all  
"""

data = soup.find("tbody")
rows = data.find_all("tr", {"style": ""})

print(rows[1])


"""
map = folium.Map(location=[32.2248, 46.626], zoom_start=6, tiles="Stamen Terrain")

fg = folium.FeatureGroup(name="My Markers")

for item in [[32.21, 46.92], [32.32, 46.72], [32.92, 46.12]]:
    fg.add_child(folium.Marker(location=item, popup="Testing"))

map.add_child(fg)
map.save("CoronaMap.html")
"""
