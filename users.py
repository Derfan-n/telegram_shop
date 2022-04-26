import datetime
import sqlalchemy

from data.db_session import SqlAlchemyBase


class User(SqlAlchemyBase):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    telegram_id = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    user_name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    added_products = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    elected_products = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    shopping_cart = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    created_date = sqlalchemy.Column(sqlalchemy.DateTime,
                                     default=datetime.datetime.now)
