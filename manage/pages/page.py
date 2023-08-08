from dash import html



class Page:
    empty = object

    def __init__(self, name, url):
        self.name = name
        self.url = url
        self._layout = self.empty

    def get_body(self):
        self._lazy_init_layout()
        return self._layout

    def _lazy_init_layout(self):
        if self._layout is self.empty:
            self._layout = html.Div(
                [
                    html.H4("This Page is not implemented yet!"),
                    html.Hr(),
                    html.P("Page is created by super class, please implement in subclass")
                ]
            )
