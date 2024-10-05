from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
from .database import intpk, str_256


class Base(DeclarativeBase): pass


class Products(Base):
    __tablename__ = 'product'

    id: Mapped[intpk]
    name: Mapped[str_256]
    price: Mapped[int] = mapped_column(nullable=False)
    collection: Mapped[str_256 | None]
    discount: Mapped[int | None]
    quantity: Mapped[int] = mapped_column(nullable=False)
    name_for_image: Mapped[str_256] = mapped_column(nullable=False)