from fastapi import FastAPI

import panel as pn
from panel.io.fastapi import add_application

from plot_service import create_app

app = FastAPI()

@add_application("/panel", app=app, title="My Panel App")
def create_panel_app():
    return create_app()
    # slider = pn.widgets.IntSlider(name="Slider", start=0, end=10, value=3)
    # return slider.rx() * '⭐'

@app.get("/")
async def read_root():
    return {"Hello": "World"}