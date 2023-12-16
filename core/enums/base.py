from enum import Enum
from typing import Set, TypeVar, Type, KeysView, ItemsView


__all__ = ("StrEnum",)


StrEnumType = TypeVar("StrEnumType", bound="StrEnum")


class StrEnum(str, Enum):
    @classmethod
    def all_values(cls: StrEnumType) -> Set[StrEnumType]:
        return {value for value in cls.__members__.values()}

    @classmethod
    def items(cls: Type[StrEnumType]) -> ItemsView[str, StrEnumType]:
        return cls.__members__.items()
