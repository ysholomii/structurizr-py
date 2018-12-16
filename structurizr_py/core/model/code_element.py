from __future__ import annotations

from structurizr_py.core.model.code_element_role import CodeElementRole
from structurizr_py.core.util.url import Url


class CodeElement:
    """
    Represents a code element, such as a Python class or interface, that is
    a part of the design of a component.
    """

    """The role of the code element ... Primary or Supporting"""
    __role: CodeElementRole = CodeElementRole.SUPPORTING

    """
    The name of the code element ... typically the simple class/interface name
    """
    __name: str = None

    """The fully qualified type of the code element"""
    __type: str = None

    """A short description of the code element"""
    __description: str = None

    """A URL, e.g. a reference to the code element in source code control"""
    __url: str = None

    """The programming language used to create the code element"""
    __language: str = "Python"

    """The category of code element, e.g. class, interface, etc"""
    __category: str = None

    """The visibility of the code element, e.g. public, package, private"""
    __visibility: str = None

    """The size of the code element, e.g. the number of lines"""
    __size: int = 0

    def __init__(self, fully_qualified_type_name: str):
        if fully_qualified_type_name is None \
                or len(fully_qualified_type_name.strip()) == 0:
            raise ValueError("A fully qualified name must be provided")

        dot = fully_qualified_type_name.rfind(".")
        if dot > -1:
            self.name = fully_qualified_type_name[dot + 1:]
        else:
            self.name = fully_qualified_type_name

        self.type = fully_qualified_type_name

    @property
    def role(self) -> CodeElementRole:
        return self.__role

    @role.setter
    def role(self, role: CodeElementRole):
        self.__role = role

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, new_type: str):
        self.__type = new_type

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
                raise ValueError(f"{url} is not a valid URL.")

    @property
    def language(self) -> str:
        return self.__language

    @language.setter
    def language(self, language: str):
        self.__language = language

    @property
    def category(self) -> str:
        return self.__category

    @category.setter
    def category(self, category: str):
        self.__category = category

    @property
    def visibility(self) -> str:
        return self.__visibility

    @visibility.setter
    def visibility(self, visibility: str):
        self.__visibility = visibility

    @property
    def size(self) -> int:
        return self.__size

    @size.setter
    def size(self, size: int):
        self.__size = size

    def get_package(self) -> str:
        """
        Gets the package of this component (i.e. the package of the primary
        code element)

        :return: the package name, as a str
        """
        return self.type[:self.type.rfind(".")]

    def __eq__(self, other: CodeElement) -> bool:
        if self is other:
            return True

        if other is None or not isinstance(other, CodeElement):
            return False

        return self.type == other.type

    def __hash__(self) -> int:
        return hash(self.type)
