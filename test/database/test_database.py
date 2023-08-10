import unittest
from manage.database.case import Case
from manage.database import db


class TestDataBase(unittest.TestCase):

    def test_case_load(self):
        case = Case.from_json("../../static/case/dianshang_1.json")

        self.assertEquals(case.name, "dianshang_1")

    def test_add_case(self):
        case = Case.from_json("../../static/case/dianshang_1.json")

        num_case = len(db.find_all_case())
        db.add(case)

        self.assertEquals(num_case + 1, len(db.find_all_case()))
