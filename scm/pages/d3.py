from nicegui import ui
from compenents.header import c_d

@ui.page("/3d")
def d3():
    c_d()
    ui.label("welcome to 3d page")