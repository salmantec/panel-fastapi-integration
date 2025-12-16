import panel as pn

from sinewave import SineWave

def create_app():
    sw = SineWave()
    return pn.Row(sw.param, sw.plot).servable()