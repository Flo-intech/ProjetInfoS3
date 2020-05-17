import plotly.express as px
from tkinter import *

df = px.data.gapminder()


fig = px.scatter_geo(df, locations="iso_alpha", color="continent", hover_name="country", size="pop",
                projection="natural earth")

fig.update_layout(
    updatemenus=[
dict(
            active=0,
            buttons=list([
                dict(label="Sport",
                     method="update",
                     args=[{"visible": []},
                           {"title": "Sport",
                            "annotations": []}]),
                dict(label="Foot",
                     method="update",
                     args=[{"visible": []},
                           {"title": "Foot",
                            "annotations": []}]),
                dict(label="Basket",
                     method="update",
                     args=[{"visible": []},
                           {"title": "Basket",
                            "annotations": []}]),
                dict(label="Tennis",
                     method="update",
                     args=[{"visible": []},
                           {"title": "Tennis",
                            "annotations": []}]),
            ]),
        ),
        dict(
            buttons=list([
                dict(
                    args=[],
                    label="Login",
                    method="update"
                ),
            ]),
            type = "buttons",
            direction="right",
            pad={"r": 10, "t": 10},
            showactive=True,
            x=0.5,
            xanchor="left",
            yanchor="top"
        ),
    ]
)

fig.show()