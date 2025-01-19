from typing import Optional
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Integer, String  # , ForeignKey
from sqlalchemy.orm import Mapped, mapped_column  # , relationship


class Base(DeclarativeBase):
    pass


class Card(Base):
    __tablename__ = "card"

    id: Mapped[str] = mapped_column(String(36), primary_key=True)  # Technically a UUID
    arena_id: Mapped[Optional[int]] = mapped_column(Integer)
    tcgplayer_id: Mapped[Optional[int]] = mapped_column(Integer)
    oracle_id: Mapped[Optional[str]] = mapped_column(String(36))
    scryfall_uri: Mapped[str] = mapped_column(String(100))  # TODO: Validate length needed here

    def __repr__(self) -> str:
        return f"ID({self.id!r}), ARENA_ID({self.arena_id!r}), TCGPLAYER_ID({self.tcgplayer_id!r})"
