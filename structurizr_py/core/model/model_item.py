from abc import ABC, abstractmethod
from typing import Set, Dict


class ModelItem(ABC):
    """The base class for model elements and relationships."""

    __identity: str = ""
    __tags: Set[str] = set()
    __properties: Dict[str, str] = {}

    @property
    def identity(self) -> str:
        """
        Gets the ID of this item in the model.

        :return: the ID, as a str
        """
        return self.__identity

    @identity.setter
    def identity(self, identity: str):
        """
        Sets the ID of this item in the model.

        :param identity: ID to be set, as a str
        :return: None
        """
        self.__identity = identity

    @property
    def tags(self) -> str:
        """
        Gets the comma separated list of tags. Please note that the list is
        unsorted.

        :return: a comma separated list of tags,
                 or an empty string if there are no tags
        """
        return ",".join(self.__tags)

    def get_tags_as_set(self) -> Set[str]:
        """
        Gets the set of tags of the model's item.

        :return: a set of tags (strings)
        """
        return self.__tags

    @tags.setter
    def tags(self, tags: Set[str]):
        """
        Sets the set of tags to the item.

        :param tags: a set of tags (strings)
        :return: None
        """
        self.__tags = tags

    def add_tags(self, tags: Set[str]):
        """
        Extends the set of the item's tags with a subset through union.

        :param tags: a set of tags (strings)
        :return: None
        """
        self.__tags = self.__tags.union(tags)

    @abstractmethod
    def get_required_tags(self) -> Set[str]:
        """
        Gets tags which are required by this item.

        :return: a set of required tags (strings)
        """
        pass

    def remove_tag(self, tag: str):
        """
        Removes the tag from the set of the item's tags.

        :param tag: str
        :return: None
        """
        self.__tags.remove(tag)

    def has_tag(self, tag: str) -> bool:
        """
        Checks whether the item has the specific tag.

        :param tag: str
        :return: True or False
        """
        return tag in self.__tags

    @property
    def properties(self) -> Dict[str, str]:
        """
        Gets the collection of name-value property pairs associated with this
        element as a Dict.

        :return: a Dict (str, str) (empty if there are no properties)
        """
        return self.__properties

    @properties.setter
    def properties(self, properties: Dict[str, str]):
        """
        Sets the collection of name-value property pairs to this element.

        :param properties: a Dict (str, str)
        :return: None
        """
        self.__properties = properties

    def add_property(self, name: str, value: str):
        """
        Adds a name-value property pair to this item.

        :param name: the name of the property
        :param value: the value of the property
        :return:
        """
        self.__properties[name] = value
