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

    def _create_card(self, case: Case):
        img = case.get_element(Case.IMAGE).source
        title = case.get_element(Case.TITLE).source
        desc = case.get_element(Case.DESC).source
        card_body = dbc.Card(
            [
                dbc.CardImg(src=img, top=True),
                dbc.CardBody([html.H4(title, className=f"{case.case_name}-card-title"),
                              html.P(desc, className=f"{case.case_name}-card-text"),
                              dbc.Button("Go somewhere", color=f"primary")]),
            ],
            style={"width": "18rem"},
        )
        return card_body

    def _create_card_title(self):
        pass

    def _create_card_logo(self):
        pass

    def add_case(self):
        pass


show_case = ShowCase()
