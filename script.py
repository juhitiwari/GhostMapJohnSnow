#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 14 17:53:00 2018

@author: slytherin
"""

import pandas as pd
import folium
deaths=pd.read_csv("data.csv")
deaths.rename(columns={'Number of deaths':'death_count','X coordinate':'x_coordinate','Y coordinate':'y_coordinate'},inplace=True)
locations=deaths[['x_coordinate','y_coordinate']]

deaths_list=locations.values.tolist()

map = folium.Map(location=[51.5132119,-0.13666], tiles='Stamen Toner', zoom_start=17)
for point in range(0, len(deaths_list)):
    folium.CircleMarker(deaths_list[point], radius=8, color='red', fill=True, fill_color='red', opacity = 0.4).add_to(map)
map.save("map.html")
