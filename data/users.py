import sqlalchemy
from .db_session import SqlAlchemyBase



class Messages(SqlAlchemyBase):
    __tablename__ = 'messages'

    id = sqlalchemy.Column(sqlalchemy.Integer)
    message = sqlalchemy.Column(sqlalchemy.String, nullable=True, primary_key=True)


    def __repr__(self):
        return f"<Messages> {self.id}, {self.message}"


