import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html
from manage import index, home
from manage.case import show_case, case_result
from tools import Console

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

index.add_page(home)
# 添加样例展示界面
index.add_page(show_case)
index.add_page(case_result)

index.activate()

app.layout = html.Div([dcc.Location(id="url"), index.sidebar, index.content])

if __name__ == '__main__':
    app.run(debug=True)
