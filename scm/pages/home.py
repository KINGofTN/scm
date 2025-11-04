from nicegui import ui
from compenents.header import c_d
from compenents.ldrawer import l_drawer

@ui.page("/")
def home():
    c_d()
    l_drawer()
    ui.link("3d","/3d")
