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
            self._body = self._create_primary()

    def _create_primary(self):
        all_case = db.get_all_case()
        body_items = []
        while all_case:
            row_items = []
            for _ in range(min(self.col_num, len(all_case))):
                case = all_case.pop()
                case_body = self._create_card(case)
                row_items.append(case_body)
            body_items.append(dbc.Row(row_items, className="mb-3"))
        return html.Div(body_items)

    @staticmethod
    def _create_card(case: Case):
        img = case.get_element(Case.IMAGE).source
        logo = case.get_element(Case.ICON).source
        title = case.get_element(Case.TITLE).source
        desc = case.get_element(Case.DESC).source
        card_body = dbc.Card(
            [
                dbc.CardImg(src=img, top=True, style={"object-fit": "contain"}),
                dbc.CardBody([
                    dbc.Row([
                        dbc.Col([html.Img(src=logo, style={"width": "10rem"})]),
                        dbc.Col([
                            html.H4(title, className=f"{case.name}-card-title"),
                            html.P(desc, className=f"{case.name}-card-text"),
                            html.Small(case.name, className="card-text text-muted")
                        ])
                    ])
                ]),
            ],
            style={"width": "25rem", "margin-left": "15px"}
        )
        return card_body


show_case = ShowCase()
