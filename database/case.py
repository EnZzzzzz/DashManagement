import os
from collections import namedtuple

from tools import read_json, Console

Prop = namedtuple("Prop", ["style", "industry"])
Element = namedtuple("Element", ["name", "type", "source"])


class Case:
    TITLE = "title"
    DESC = "subtitle"
    IMAGE = "image"
    ICON = "icon"

    def __init__(self, case_name, data):
        self.name = case_name
        self.prop = Prop(**data.get("prop"))
        self.elements = [Element(**ele_data) for ele_data in data.get("element")]

    @staticmethod
    def from_json(json_path):
        data = read_json(json_path)
        case_name = os.path.basename(json_path).split(".")[0]
        return Case(case_name, data)

    def get_element(self, name):
        for ele in self.elements:
            if ele.name == name:
                Console.info("Element found!")
                return ele
        Console.warn(f"No such element named {name} found!")
        return None
