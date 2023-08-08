from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship

from manage.database import Base


class Element(Base):
    __tablename__ = "element"

    id = Column(Integer, primary_key=True)
    case_id = Column(Integer, ForeignKey("case.id"))
    case = relationship("Case", back_populates="The related case of this element")

    type = Column(String)
    name = Column(String)
    source = Column(String)

    def __init__(self, ele_type, name, source):
        self.type = ele_type
        self.name = name
        self.source = source
