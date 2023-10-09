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
    json_title = all_eq_data['metadata']['title']

all_eq_dicts = all_eq_data['features']

mags, lons, lats, hover_texts = [], [], [], []

for eq_dict in all_eq_dicts:
    mags.append(eq_dict['properties']['mag'])
    lons.append(eq_dict['geometry']['coordinates'][0])
    lats.append(eq_dict['geometry']['coordinates'][1])
    hover_texts.append(eq_dict['properties']['title'])

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

my_layout = Layout(title = json_title)

fig = {'data': data, 'layout' : my_layout}
offline.plot(fig, filename='Chapter_16\global_earthquakes_16_6.html')