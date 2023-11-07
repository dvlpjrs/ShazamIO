from typing import Generic
from typing import Optional
from typing import TypeVar

from pydantic import BaseModel

T = TypeVar("T")


class BaseIdTypeHref(BaseModel):
    id: str
    type: str
    href: str


class BaseDataModel(BaseModel, Generic[T]):
    attributes: T


class BaseHrefNextData(BaseModel, Generic[T]):
    href: str
    next: Optional[str] = None
    data: T
