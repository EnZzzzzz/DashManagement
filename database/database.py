import glob
import os.path

from .case import Case
from tools.functional import SingletonMeta

POJ_ROOT = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))


class DataBase(object, metaclass=SingletonMeta):

    def __init__(self, resource_dir=None):
        self.res_dir = resource_dir if resource_dir is not None else os.path.join(POJ_ROOT, "static")

        self._case_dict = {}
        for case_path in glob.glob(os.path.join(self.res_dir, "case", "*.json")):
            case = Case.from_json(case_path)
            case_list = self._case_dict.get(case.prop.industry, [])
            case_list.append(case)
            self._case_dict[case.prop.industry] = case_list

    def get_all_case(self):
        all_case = []
        for case_list in self._case_dict.values():
            all_case += case_list
        return all_case


db = DataBase()