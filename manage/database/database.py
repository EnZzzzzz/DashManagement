import glob
import os.path

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .case import Case
from manage.tools.functional import SingletonMeta

from manage import POJ_DIR, STATIC_DIR
from manage.database import db_url, Base


class DataBase(object, metaclass=SingletonMeta):

    def __init__(self, resource_dir=None):
        self.res_dir = resource_dir if resource_dir is not None else STATIC_DIR

        self.engine = create_engine(db_url, echo=True)
        self.session = sessionmaker(bind=self.engine)()

        Base.metadata.create_all(self.engine)

    def add(self, item):
        self.session.add(item)
        self.session.commit()

    def find_all_case(self):
        _filter = self.session.query(Case).filter()
        return _filter.all()

    def find_case(self, industry):
        self.session.query(Case).filter(
            Case.industry == industry
        )


db = DataBase()
