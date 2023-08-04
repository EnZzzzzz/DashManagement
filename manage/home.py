from manage import Page


class Home(Page):

    def __init__(self):
        super(Home, self).__init__("Home", "/")


home = Home()