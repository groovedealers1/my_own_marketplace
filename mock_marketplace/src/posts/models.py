from sqlalchemy.orm import Mapped, mapped_column, relationship, DeclarativeBase
from sqlalchemy import MetaData, ForeignKey, text, CheckConstraint, Index
import enum
import datetime
from typing import Annotated, Optional


str_256 = Annotated[str, 256]
intpk = Annotated[int, mapped_column(primary_key=True)]


class Base(DeclarativeBase): pass


class Products(Base):
    __tablename__ = 'products'

    id: Mapped[intpk]
    name: Mapped[str_256]
    price: Mapped[int] = mapped_column(nullable=False)
    collection: Mapped[str_256 | None]
    discount: Mapped[int | None]
    quantity: Mapped[int] = mapped_column(nullable=False)

