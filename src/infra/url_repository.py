from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime

from src.domain.url import OriginUrl, ShortenHash
from src.domain.url_repository import UrlRepository
from .sqlalchemy import Base, tx


class SAUrlRepository(UrlRepository):
    def save(
            self, origin: OriginUrl, shorten: ShortenHash, seq: bytes,
            ) -> None:
        new_url = Url(
                origin=origin.url, shorten=shorten.hash,
                seq=seq.decode())

        with tx() as session:
            session.add(new_url)


class Url(Base):
    __tablename__ = 'url'

    id = Column(Integer, primary_key=True)
    seq = Column(String, index=True, unique=True, nullable=False)
    origin = Column(String, nullable=False)
    shorten = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.now)
    updated_at = Column(
            DateTime, nullable=False, default=datetime.now,
            onupdate=datetime.now)