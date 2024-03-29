import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline
from plotly import colors

for key in colors.PLOTLY_SCALES.keys():
    print(key)

#explroe the structure of the data
#filename = "Chapter_16\data\eq_data_1_day_m1.json"
filename = "Chapter_16\data\eq_data_30_day_m1.json"

with open(filename) as f:
    all_eq_data = json.load(f)

all_eq_dicts = all_eq_data['features']

mags, lons, lats, hover_texts = [], [], [], []

for eq_dict in all_eq_dicts:
    title = eq_dict['properties']['title']
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    hover_texts.append(title)

#Map the earthquakes
#data = [Scattergeo(lon = lons, lat = lats)]
data = [{
    'type':'scattergeo',
    'lon' : lons,
    'lat' : lats,
    'text' : hover_texts,
    'marker' : {
        'size' : [5*mag for mag in mags],
        'color' : mags,
        'reversescale' : True,
        'colorbar' : {'title' : 'Magnitude'}
    },
}]
my_layout = Layout(title = 'Glogal Earthquakes')

fig = {'data': data, 'layout' : my_layout}
offline.plot(fig, filename='Chapter_16\global_earthquakes.html')