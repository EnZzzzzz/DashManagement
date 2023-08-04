import dash
from dash import html, Output, Input
import dash_bootstrap_components as dbc

# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

empty = object()


class Index:

    def __init__(self):
        self._nav_links = []
        self._navigator = {}

        self.title = "Sidebar"
        self.desc = "A simple sidebar layout with navigation links"

        self.content = html.Div(id="page-content", style=CONTENT_STYLE)
        self._sidebar = empty

    @staticmethod
    def _404_error(pathname):
        return html.Div([html.H1("404: Not found", className="text-danger"),
                         html.Hr(),
                         html.P(f"The pathname {pathname} was not recognised...")],
                        className="p-3 bg-light rounded-3")

    @property
    def sidebar(self) -> html.Div:
        self._lazy_load_layout()
        self._sidebar: html.Div
        return self._sidebar

    def _lazy_load_layout(self):
        if self._sidebar is empty:
            self._sidebar = html.Div(
                [
                    html.H2(self.title, className="display-4"),
                    html.Hr(),
                    html.P(self.desc, className="lead"),
                    dbc.Nav(self._nav_links, vertical=True, pills=True)
                ],
                style=SIDEBAR_STYLE,
            )

    def add_page(self, name, url, body):
        self._nav_links.append(dbc.NavLink(name, href=url, active="exact"))
        self._navigator[url] = body

    def activate(self):
        output = Output("page-content", "children")
        _input = Input("url", "pathname")

        def navigate_func(pathname):
            if pathname not in self._navigator:
                return self._404_error(pathname)
            else:
                return self._navigator.get(pathname)

        dash.callback(output, _input)(navigate_func)


index = Index()
