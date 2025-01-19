from .db_conn import DBConn
from .models import Base


def init_db(connection_string=None):
    if not connection_string:
        connection_string = "sqlite:///:memory:"
    db_conn = DBConn(connection_string, echo=True)
    engine = db_conn.get_engine()
    Base.metadata.create_all(engine)
