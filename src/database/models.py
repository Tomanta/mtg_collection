from typing import Optional, Dict
from uuid import uuid4
from sqlalchemy import Integer, String, Uuid, JSON
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class Card(Base):
    __tablename__ = "card"

    id: Mapped[uuid4] = mapped_column(Uuid, primary_key=True)
    arena_id: Mapped[Optional[int]] = mapped_column(Integer)
    lang: Mapped[str] = mapped_column(String(3))
    tcgplayer_id: Mapped[Optional[int]] = mapped_column(Integer)
    tcgplayer_etched_id: Mapped[Optional[int]] = mapped_column(Integer)
    cardmarket_id: Mapped[Optional[int]] = mapped_column(Integer)
    layout: Mapped[str] = mapped_column(String(25))
    oracle_id: Mapped[Optional[uuid4]] = mapped_column(Uuid)
    scryfall_uri: Mapped[str] = mapped_column(String(400))
    uri: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(200))
    data: Mapped[Dict[str, object]] = mapped_column(JSON)
    set: Mapped[str] = mapped_column(String(6))
    set_name: Mapped[str] = mapped_column(String(75))
    rarity: Mapped[str] = mapped_column(String(10))

    def __repr__(self) -> str:
        return f"NAME({self.name!r}), ID({self.id!r})"
