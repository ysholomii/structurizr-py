from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Set, TYPE_CHECKING

from structurizr_py.core.model.model import Model
from structurizr_py.core.model.model_item import ModelItem
from structurizr_py.core.util.url import Url

if TYPE_CHECKING:
    from structurizr_py.core.model.relationship import Relationship


class Element(ModelItem, ABC):
    """This is the superclass for all model elements."""

    CANONICAL_NAME_SEPARATOR = "/"

    __model: Model = None
    __name: str = None
    __description: str = None
    __url: str = None
    __relationships: Set[Relationship] = None

    @property
    def model(self) -> Model:
        return self.__model

    @model.setter
    def model(self, model: Model):
        self.__model = model

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        if name is None or name.strip() == "":
            raise ValueError(
                "The name of an element must not be null or empty")

        self.__name = name

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def url(self) -> str:
        return self.__url

    @url.setter
    def url(self, url: str):
        if url is not None and len(url.strip()) > 0:
            if Url.is_url(url):
                self.__url = url
            else:
                raise ValueError(
                    url + " is not a valid URL.")

    @abstractmethod
    def get_canonical_name(self) -> str:
        pass

    def format_for_canonical_name(self, name: str) -> str:
        return name.replace(self.CANONICAL_NAME_SEPARATOR, "")

    @abstractmethod
    def get_parent(self) -> Element or None:
        """
        Gets the parent element of this element.

        :return: the parent Element, or None if this element doesn't have a
                 parent element (e.g. a SoftwareSystem)
        """
        pass

    @property
    def relationships(self) -> Set[Relationship]:
        """
        Gets the set of outgoing relationships.
        :return: a Set of Relationship objects, or am empty Set if none exist
        """
        return self.__relationships or {}

    @relationships.setter
    def relationships(self, relationships: Set[Relationship]):
        if relationships is not None and type(relationships) is set:
            self.__relationships = relationships

    def has_afferent_relationships(self) -> bool:
        """
        Determines whether this element has afferent (incoming) relationships.

        :return: true if this element has afferent relationships, false
                 otherwise
        """
        return any(relation.destination == self for relation in
                   self.model.relationships)

    def has_efferent_relationship_with(self, element) -> bool:
        """
        Determines whether this element has an efferent (outgoing) relationship
        with the specified element.

        :param element: an instance of Element class
        :return: true if this element has efferent relationship with the
                 specified element, false otherwise
        """
        return True if self.get_efferent_relationship_with(element) is not None\
            else False

    def get_efferent_relationship_with(self, element) -> Relationship or None:
        """
        Gets the efferent (outgoing) relationship with the specified element.

        :param element: the element to look for
        :return: a Relationship object if an efferent relationship exists, None
                 otherwise
        """
        if element is None:
            return None

        for relation in self.relationships:
            if relation.destination == self:
                return relation

        return None

    def has(self, relationship: Relationship) -> bool:
        return True if relationship in self.relationships else False

    def add_relationship(self, relationship: Relationship):
        self.relationships.add(relationship)

    def __str__(self) -> str:
        return f"{{{self.identity} | {self.name} | {self.description}}}"

    def __hash__(self) -> int:
        return hash(self.name) if self.name is not None else hash(super())

    def __eq__(self, other: Element) -> bool:
        if self is other:
            return True

        if other is None or not isinstance(other, Element):
            return False

        return self.get_canonical_name() == other.get_canonical_name()
