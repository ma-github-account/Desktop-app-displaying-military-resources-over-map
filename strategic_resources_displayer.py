
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

import sys
if sys.version_info[0] < 3:
    import Tkinter as Tk
else:
    import tkinter as Tk

from db_data_management import select_all_coordinates_list_from_db

root = Tk.Tk()
root.wm_title("Strategic resources map")
root.columnconfigure(0, weight=1)

ttk.Label(
  root,
  text="Strategic resources map",
  font=("TkDefaultFont", 16)
).grid()

fig = Figure(figsize=(10, 7), dpi=100)
ax = fig.add_subplot(111)

m = Basemap(llcrnrlon=23,llcrnrlat=44,urcrnrlon=41,urcrnrlat=52,
         resolution='i', projection='tmerc', lat_0 = 50, lon_0 = 30, ax=ax)

# Region setting frame

region_choice_frame = ttk.LabelFrame(root, text='Region specific Maps')
region_choice_frame.grid(sticky=(tk.W + tk.E))
for i in range(3):
  region_choice_frame.columnconfigure(i, weight=1 )

regions = ["Whole Ukraine","Capital region","Donbas region","Crimea region"]

region_dropdown_value = tk.StringVar()
ttk.Label(region_choice_frame, text='Select region to be displayed on the map').grid(row=2, column=0, sticky=(tk.W + tk.E))
ttk.Combobox(
  region_choice_frame,
  textvariable=region_dropdown_value,
  values=regions
).grid(row=3, column=0, sticky=(tk.W + tk.E))

# Map type setting frame

map_type_frame = ttk.LabelFrame(root, text='Map type setting')
map_type_frame.grid(sticky=(tk.W + tk.E))
for i in range(2):
  map_type_frame.columnconfigure(i, weight=1 )

map_type_radiobutton_value = tk.StringVar()
ttk.Label(map_type_frame , text='Select map type').grid(row=4, column=0)
map_type_radiobutton_frame = ttk.Frame(map_type_frame)
for lab in ('Political', 'Physical'):
  ttk.Radiobutton(
    map_type_radiobutton_frame, value=lab, text=lab, variable=map_type_radiobutton_value
).pack(side=tk.LEFT, expand=True)
map_type_radiobutton_frame.grid(row=5, column=0, sticky=(tk.W + tk.E))

settings_frame = ttk.LabelFrame(root, text='Map type setting')
settings_frame.grid(sticky=(tk.W + tk.E))

show_rivers_checkbutton_value = tk.BooleanVar(value=False)
ttk.Checkbutton(
  settings_frame, variable=show_rivers_checkbutton_value,
  text='Show Rivers'
).grid(row=6, column=0, sticky=tk.W, pady=5)

# Reload button frame

reload_button_frame = ttk.LabelFrame(root, text='Reload button')
reload_button_frame.grid(sticky=(tk.W + tk.E))
for i in range(3):
  reload_button_frame.columnconfigure(i, weight=1 )

ttk.Label(reload_button_frame , text='Click Reload button to refresh the map after setting changes').pack(side=tk.TOP)
Reload_button = ttk.Button(reload_button_frame, text='RELOAD')
Reload_button.pack(side=tk.LEFT)

# importing coordianates from database

strategic_resources = select_all_coordinates_list_from_db()

# Functions

def add_strategic_resources_to_the_map(map):

    for resource in strategic_resources:

        x1, y1 = map(resource[0], resource[1])

        map.plot(x1, y1, marker='o',color='r')

def on_reset():

    region_value = region_dropdown_value.get()
    map_type_value = map_type_radiobutton_value.get()
    show_rivers_value = show_rivers_checkbutton_value.get()

    fig = Figure(figsize=(10, 7), dpi=100)
    ax = fig.add_subplot(111)

    if region_value == "Whole Ukraine":
        ll_lon_coordinates = 23
        ll_lat_coordinates = 44
        ur_lon_coordinates = 41
        ur_lat_coordinates = 52
        lat_0 = 50
        lon_0 = 30
    elif region_value == "Capital region":
        ll_lon_coordinates = 28
        ll_lat_coordinates = 49
        ur_lon_coordinates = 33
        ur_lat_coordinates = 51
        lat_0 = 50
        lon_0 = 30
    elif region_value == "Donbas region":
        ll_lon_coordinates = 34
        ll_lat_coordinates = 46
        ur_lon_coordinates = 40
        ur_lat_coordinates = 50
        lat_0 = 50
        lon_0 = 30
    elif region_value == "Crimea region":
        ll_lon_coordinates = 32
        ll_lat_coordinates = 44
        ur_lon_coordinates = 38
        ur_lat_coordinates = 46
        lat_0 = 45
        lon_0 = 34
    else:
        ll_lon_coordinates = 23
        ll_lat_coordinates = 44
        ur_lon_coordinates = 41
        ur_lat_coordinates = 52
        lat_0 = 50
        lon_0 = 30        

    map_displayed = Basemap(ll_lon_coordinates,ll_lat_coordinates,ur_lon_coordinates,ur_lat_coordinates,
             resolution='i', projection='tmerc', lat_0 = 50, lon_0 = 30, ax=ax)

    if map_type_value == "Political":

        map_displayed.drawmapboundary(fill_color='aqua')
        map_displayed.fillcontinents(color='coral',lake_color='aqua')

    elif map_type_value == "Physical":

        map_displayed.shadedrelief()

    map_displayed.drawcoastlines()
    map_displayed.drawcountries()

    if show_rivers_value == True:

        map_displayed.drawrivers(color='#0000ff')

    # a tk.DrawingArea
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().grid(row=7, column=0, sticky=(tk.W + tk.E))
    
    add_strategic_resources_to_the_map(map_displayed)

    # Display icon for Kiev location
    x1, y1 = map_displayed(30.5, 50.4)
    map_displayed.plot(x1, y1, marker='D',color='w')

# Binding button to function

Reload_button.configure(command=on_reset)

canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().grid(row=7, column=0, sticky=(tk.W + tk.E))

Tk.mainloop()
