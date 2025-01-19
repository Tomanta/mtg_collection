from sqlalchemy import create_engine
from sqlalchemy.orm import Session


class DBConn:
    def __init__(self, connection_string="sqlite:///:memory:", echo=False):
        self.engine = create_engine(connection_string, echo=echo)

    def get_engine(self):
        return self.engine
