import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = sa.Column(sa.Integer, primary_key=True)
    email = sa.Column(sa.String(100), unique=True)
    first_name = sa.Column(sa.String(50))
    last_name = sa.Column(sa.String(50), nullable=True)
    created_at = sa.Column(sa.DateTime, default=sa.func.now())
    last_login_at = sa.Column(sa.DateTime, nullable=True)


class Token(Base):
    __tablename__ = 'tokens'

    id = sa.Column(sa.Integer, primary_key=True)
    user_id = sa.Column(sa.Integer, sa.ForeignKey('users.id'))
    type_ = sa.Column(sa.String(25))
    token = sa.Column(sa.String(100))
    created_at = sa.Column(sa.DateTime, default=sa.func.now())
