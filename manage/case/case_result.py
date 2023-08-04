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
                self._create_result(),
                self._create_result(),
                self._create_result(),
                self._create_processing(),
                html.Div([dbc.Pagination(max_value=50, first_last=True, previous_next=True, fully_expanded=False,
                                         style={"justify-content": "center"})])
            ])

    def _create_processing(self):
        processing = dbc.Card([
            dbc.Row([
                html.Div(
                    [
                        dbc.Button(dbc.Spinner(size="sm"), color="primary", disabled=True, className="me-2"),
                        dbc.Button("生成中: dianshang 1", color="primary", disabled=True),
                    ],
                    style={"border": "none"}
                ),
            ], justify="start")
        ], style={"border": "none"}
        )
        return processing

    def _create_color_sample(self, title, hex_color):
        return dbc.Row([
            dbc.Col(html.H5(title)),
            dbc.Col(html.Div(style={"background-color": hex_color,
                                    "height": "20px", "width": "80px"}))
        ], justify="start")

    def _create_result(self):
        created = dbc.Card([
            dbc.Row([
                dbc.Col([
                    dbc.Carousel(items=[
                        {"key": "1", "src": "/static/imgs/1.jpg", "caption": "Image 1"},
                        {"key": "2", "src": "/static/imgs/2.jpg", "caption": "Image 1"},
                        {"key": "3", "src": "/static/imgs/3.jpg", "caption": "Image 1"},
                        {"key": "4", "src": "/static/imgs/4.jpg", "caption": "Image 1"},
                        {"key": "5", "src": "/static/imgs/5.jpg", "caption": "Image 1"},
                    ], controls=True, indicators=False, interval=4000, ride="carousel",
                        style={"width": "28rem"},
                    )
                ]),
                dbc.Col([
                    html.H3("生成信息"),
                    html.Hr(),
                    dbc.Row([
                        dbc.Col([
                            html.H5("配色编号： 1104"),
                            html.H5("布局编号： 1104"),
                            html.H5("标题模板： 1104"),
                        ]),
                        dbc.Col([
                            self._create_color_sample("背景颜色是：", "#FF00FF"),
                            self._create_color_sample("标题颜色是：", "#FF00FF"),
                            self._create_color_sample("画框颜色是：", "#FF00FF"),
                        ])
                    ])
                ])
            ], className="mb-2"),
            html.Hr()
        ], style={"border": "0px"})
        return created


case_result = CaseResult()
