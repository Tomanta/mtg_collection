from .db_conn import DBConn
from .models import Base


def init_db(db_conn=None, connection_string=None):
    if not connection_string:
        connection_string = "sqlite:///:memory:"
    if not db_conn:
        db_conn = DBConn(connection_string, echo=True)
    engine = db_conn.get_engine()
    Base.metadata.create_all(engine)
