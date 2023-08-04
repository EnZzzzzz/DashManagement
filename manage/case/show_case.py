import glob

import dash_bootstrap_components as dbc
from dash import html

from database.case import Case
from database.database import db

empty = object()


class ShowCase:

    def __init__(self):
        self.name = "Case"
        self.url = "/case-list"

        self._case_list = []
        self._body = empty
        self.col_num = 3

    @property
    def body(self):
        self._lazy_init_layout()
        return self._body

    def _lazy_init_layout(self):
        if self._body is empty:
            all_case = db.get_all_case()
            self._body = self._create_card(all_case[0])

    @staticmethod
    def _create_card(case: Case):
        img = case.get_element(Case.IMAGE).source
        logo = case.get_element(Case.ICON).source
        title = case.get_element(Case.TITLE).source
        desc = case.get_element(Case.DESC).source
        card_body = dbc.Card(
            [
                dbc.CardImg(src=img, top=True),
                dbc.CardBody([
                    dbc.Row([
                        dbc.Col([html.Img(src=logo, style={"width": "10rem"})]),
                        dbc.Col([html.H4(title, className=f"{case.name}-card-title"),
                                 html.P(desc, className=f"{case.name}-card-text"),
                                 html.Small(case.name, className="card-text text-muted")])
                    ])
                ]),
            ],
            style={"width": "25rem"},
        )
        return card_body


show_case = ShowCase()
