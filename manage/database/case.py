import os
from collections import namedtuple
from sqlalchemy import Column, Integer, String

from manage.database import Base
from manage.tools import read_json, Console

Prop = namedtuple("Prop", ["style", "industry"])
Element = namedtuple("Element", ["name", "type", "source"])


class Case(Base):
    __tablename__ = "case"
    TITLE = "title"
    DESC = "subtitle"
    IMAGE = "image"
    ICON = "icon"

    id = Column(Integer, primary_key=True)
    name = Column(String)

    industry = Column(String, default="auto")
    style = Column(String, default="atuo")
    strategy = Column(String, default="auto")
    scenario = Column(String, default="auto")

    num = Column(Integer, default=1)

    def __init__(self, case_name, prop, elements, **kwargs):
        self.name = case_name
        self.industry = prop.get("industry")
        self.style = prop.get("style")
        self.scenario = prop.get("scenario")
        self.strategy = prop.get("strategy")

        self.elements = [Element(**ele_data) for ele_data in elements]

    @staticmethod
    def from_json(json_path):
        data = read_json(json_path)
        case_name = os.path.basename(json_path).split(".")[0]
        return Case(case_name, **data)

    def get_element(self, name):
        for ele in self.elements:
            if ele.name == name:
                return ele
        Console.warn(f"No such element named {name} found!")
        return None
