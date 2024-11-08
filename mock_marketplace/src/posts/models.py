from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
from .database import intpk, str_256, str_1024


class Base(DeclarativeBase): pass


class Products(Base):
    __tablename__ = 'product'

    id: Mapped[intpk]

    name: Mapped[str_256] = mapped_column(nullable=False)
    description: Mapped[str_256] = mapped_column(nullable=False)
    characteristics: Mapped[str_1024] = mapped_column(nullable=False)
    colors: Mapped[str_256] = mapped_column(nullable=False)
    price: Mapped[int] = mapped_column(nullable=False)
    collection: Mapped[str_256 | None]
    discount: Mapped[int | None]
    quantity: Mapped[int] = mapped_column(nullable=False)


class Images(Base):
    __tablename__ = 'image'

    id: Mapped[intpk]

    name_for_image_1: Mapped[str_256] = mapped_column(nullable=False)
    name_for_image_2: Mapped[str_256] = mapped_column(nullable=False)
    name_for_image_3: Mapped[str_256] = mapped_column(nullable=False)
