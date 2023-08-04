from dash import html
import dash_bootstrap_components as dbc

from manage import Page


class CaseResult(Page):

    def __init__(self):
        super(CaseResult, self).__init__("Result", "/result")

    def _lazy_init_layout(self):
        if self._layout is Page.empty:
            self._layout = html.Div([
                html.H4("生成结果"),
                html.Hr(),
                html.H4("暂未实现"),
                html.Div([dbc.Pagination(max_value=50, first_last=True, previous_next=True, fully_expanded=False,
                                         style={"justify-content": "center"})])
            ])


case_result = CaseResult()
