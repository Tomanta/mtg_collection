from typing import Optional, Dict
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Integer, String, Uuid, Float, JSON  # , ForeignKey
from sqlalchemy.orm import Mapped, mapped_column  # , relationship
from uuid import uuid4

class Base(DeclarativeBase):
    pass


# TODO: multiverse_ids to join cards together


class Card(Base):
    __tablename__ = "card"

    id: Mapped[uuid4] = mapped_column(Uuid, primary_key=True)  # Technically a UUID
    arena_id: Mapped[Optional[int]] = mapped_column(Integer)
    lang: Mapped[str] = mapped_column(String(50))  # TODO: Validate length
    tcgplayer_id: Mapped[Optional[int]] = mapped_column(Integer)
    tcgplayer_etched_id: Mapped[Optional[int]] = mapped_column(Integer)
    cardmarket_id: Mapped[Optional[int]] = mapped_column(Integer)
    layout: Mapped[str] = mapped_column(String(50))  # TODO: Validate length
    oracle_id: Mapped[Optional[uuid4]] = mapped_column(Uuid)
    scryfall_uri: Mapped[str] = mapped_column(String(100))  # TODO: Validate length needed here
    uri: Mapped[str] = mapped_column(String(100))  # TODO: Validate length needed
    name: Mapped[str] = mapped_column(String(100))  # TODO: Validate length
    data: Mapped[Dict[str, object]] = mapped_column(JSON)

    def __repr__(self) -> str:
        return f"NAME({self.name!r}), ID({self.id!r}), ARENA_ID({self.arena_id!r}), TCGPLAYER_ID({self.tcgplayer_id!r})"

