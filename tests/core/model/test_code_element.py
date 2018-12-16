import unittest

from structurizr_py.core.model.code_element import CodeElement


class TestCodeElement(unittest.TestCase):

    def test_init_when_fully_qualified_type_is_specified(self):
        code_element = CodeElement("structurizr.component.SomeComponent")

        self.assertEqual("SomeComponent", code_element.name)
        self.assertEqual(
            "structurizr.component.SomeComponent",
            code_element.type)

    def test_init_when_fully_qualified_type_is_specified_in_default_pkg(self):
        code_element = CodeElement("SomeComponent")

        self.assertEqual("SomeComponent", code_element.name)
        self.assertEqual("SomeComponent", code_element.type)

    def test_description_property(self):
        code_element = CodeElement("structurizr.component.SomeComponent")
        self.assertIsNone(code_element.description)

        code_element.description = "Description"
        self.assertEqual("Description", code_element.description)

    def test_size_property(self):
        code_element = CodeElement("structurizr.component.SomeComponent")
        self.assertEqual(0, code_element.size)

        code_element.size = 123456
        self.assertEqual(123456, code_element.size)

    def test_language_property(self):
        code_element = CodeElement("structurizr.component.SomeComponent")
        self.assertEqual("Python", code_element.language)

        code_element.language = "Java"
        self.assertEqual("Java", code_element.language)

    def test_category_property(self):
        code_element = CodeElement("structurizr.component.SomeComponent")
        self.assertIsNone(code_element.category)

        code_element.category = "class"
        self.assertEqual("class", code_element.category)

    def test_visibility_property(self):
        code_element = CodeElement("structurizr.component.SomeComponent")
        self.assertIsNone(code_element.visibility)

        code_element.visibility = "package"
        self.assertEqual("package", code_element.visibility)

    def test_url_property(self):
        code_element = CodeElement("structurizr.component.SomeComponent")
        code_element.url = "https://structurizr.com"

        self.assertEqual("https://structurizr.com", code_element.url)

    def test_set_url_raises_error_on_invalid_url_provided(self):
        code_element = CodeElement("structurizr.component.SomeComponent")
        self.assertRaises(
            ValueError,
            setattr,
            code_element,
            "url",
            "dummy")

    def test_set_url_does_nothing_when_null_url_is_specified(self):
        code_element = CodeElement("structurizr.component.SomeComponent")
        code_element.url = None

        self.assertIsNone(code_element.url)

    def test_set_url_does_nothing_when_an_empty_url_is_specified(self):
        code_element = CodeElement("structurizr.component.SomeComponent")
        code_element.url = " "

        self.assertIsNone(code_element.url)

    def test_init_raises_exception_when_null_type_is_specified(self):
        self.assertRaises(ValueError, CodeElement, None)

    def test_init_raises_exception_when_empty_type_is_specified(self):
        self.assertRaises(ValueError, CodeElement, " ")

    def test_equals_returns_false_when_compared_to_none(self):
        code_element = CodeElement("structurizr.component.SomeComponent")
        self.assertNotEqual(code_element, None)

    def test_equals_returns_false_when_compared_to_other_type_of_object(self):
        code_element = CodeElement("structurizr.component.SomeComponent")
        self.assertNotEqual(code_element, "hello")
    
    def test_equals_returns_false_when_compared_to_elem_with_other_type(self):
        code_element1 = CodeElement("structurizr.component.SomeComponent1")
        code_element2 = CodeElement("structurizr.component.SomeComponent2")
        
        self.assertNotEqual(code_element1, code_element2)

    def test_equals_returns_true_when_compared_to_elem_with_same_type(self):
        code_element1 = CodeElement("structurizr.component.SomeComponent1")
        code_element2 = CodeElement("structurizr.component.SomeComponent1")

        self.assertEqual(code_element1, code_element2)

    def test_hashable(self):
        code_element = CodeElement("structurizr.component.SomeComponent")
        test_dict = {code_element: "hello"}

        self.assertEqual("hello", test_dict[code_element])
