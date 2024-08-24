from typing import Generic, TypeVar
from sqlalchemy.orm.session import Session
from abc import ABCMeta

T = TypeVar('T')


class Repository(Generic[T], metaclass=ABCMeta):
    model = None

    def __init__(
        self,
        session: Session
    ):
        self.session = session

    def get_by_id(self, id: int) -> T:
        return self.session.query(
            self.model
        ).filter(
            self.model.id == id
        ).first()

    def get_all(self) -> list[T]:
        return self.session.query(
            self.model
        ).all()

    def add(self, obj: T):
        self.session.add(obj)
