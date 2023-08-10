import os.path

from sqlalchemy.ext.declarative import declarative_base
from manage import POJ_DIR

Base = declarative_base()
db_url = f"sqlite:///{os.path.join(POJ_DIR, 'manage', 'database', 'case.db')}"


from .database import db