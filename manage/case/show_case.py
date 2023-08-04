import dash_bootstrap_components as dbc
from dash import html

empty = object()


class ShowCase:

    def __init__(self):
        self.name = "Case"
        self.url = "/case-list"

        self._case_list = []
        self._body = empty

    @property
    def body(self):
        self._lazy_init_layout()
        return self._body

    def _lazy_init_layout(self):
        if self._body is empty:
            self._body = dbc.Card(
                [
                    dbc.CardImg(src="/static/imgs/1.jpg", top=True),
                    dbc.CardBody(
                        [
                            html.H4("Card title", className="card-title"),
                            html.P(
                                "Some quick example text to build on the card title and "
                                "make up the bulk of the card's content.",
                                className="card-text",
                            ),
                            dbc.Button("Go somewhere", color="primary"),
                        ]
                    ),
                ],
                style={"width": "18rem"},
            )

    def _create_card(self):
        pass

    def _create_card_title(self):
        pass

    def _create_card_logo(self):
        pass

    def add_case(self):
        pass


show_case = ShowCase()