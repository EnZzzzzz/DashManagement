import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html
from index import index

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])


index.add_page("Home", "/", html.P("This is the content of the home page!"))
index.add_page("Page 1", "/page-1", html.P("This is the content of page 1. Yay!"))
index.add_page("Page 2", "/page-2", html.P("This is the content of page 2!"))

index.activate()

app.layout= html.Div([dcc.Location(id="url"), index.sidebar, index.content])

if __name__ == '__main__':
    app.run(debug=True)
