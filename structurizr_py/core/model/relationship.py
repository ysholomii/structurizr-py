from __future__ import annotations
from typing import Set, TYPE_CHECKING

from structurizr_py.core.model.interaction_style import InteractionStyle
from structurizr_py.core.model.model_item import ModelItem
from structurizr_py.core.model.tags import Tags

if TYPE_CHECKING:
    from structurizr_py.core.model.element import Element


class Relationship(ModelItem):
    """A relationship between two elements."""

    __source: Element = None
    __source_identity: str = None
    __destination: Element = None
    __destination_identity: str = None
    __description: str = None
    __technology: str = None
    __interaction_style: str = InteractionStyle.SYNCHRONOUS

    def __init__(self, source: Element, destination: Element, description: str,
                 technology: str, interaction_style: str):
        super()

        self.__source = source
        self.__destination = destination
        self.__description = description
        self.__technology = technology
        self.__interaction_style = interaction_style

    @property
    def source(self) -> Element:
        return self.__source

    @source.setter
    def source(self, source: Element):
        self.__source = source

    @property
    def source_identity(self) -> str:
        return self.__source.identity if self.__source is not None \
            else self.__source_identity

    @source_identity.setter
    def source_identity(self, source_identity: str):
        self.__source_identity = source_identity

    @property
    def destination(self) -> Element:
        return self.__destination

    @destination.setter
    def destination(self, destination: Element):
        self.__destination = destination

    @property
    def destination_identity(self) -> str:
        return self.__destination.identity if self.__source is not None \
            else self.__destination_identity

    @destination_identity.setter
    def destination_identity(self, destination_identity: str):
        self.__destination_identity = destination_identity

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def technology(self) -> str:
        return self.__technology

    @technology.setter
    def technology(self, technology: str):
        self.__technology = technology

    @property
    def interaction_style(self) -> str:
        return self.__interaction_style

    @interaction_style.setter
    def interaction_style(self, interaction_style: str):
        self.__interaction_style = interaction_style

        if interaction_style == InteractionStyle.SYNCHRONOUS:
            self.remove_tag(Tags.ASYNCHRONOUS)
            self.add_tags({Tags.SYNCHRONOUS})
        else:
            self.remove_tag(Tags.SYNCHRONOUS)
            self.add_tags({Tags.ASYNCHRONOUS})

    def get_required_tags(self) -> Set[str]:
        return {Tags.RELATIONSHIP}

    def __eq__(self, other: Relationship) -> bool:
        if self is other:
            return True
        if other is None or not isinstance(other, Relationship):
            return False

        if self.description != other.description:
            return False
        if self.destination != other.destination:
            return False
        if self.source != other.source:
            return False

        return True

    def __ne__(self, other: Relationship) -> bool:
        return not self.__eq__(other)

    def __hash__(self) -> int:
        result = hash(self.source_identity)
        result = 31 * result + hash(self.destination)
        result = 31 * result + hash(self.description)

        return result

    def __str__(self) -> str:
        return str(self.source) + "---[" + self.description + "]--->" + \
               str(self.destination)
