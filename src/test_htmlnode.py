import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode(tag="p",
                        value="hello peeps",
                        children=None,
                        props={
                            "class": "hello-text",
                            "id": "salutation"
                        })
        node2 = HTMLNode(tag="d",
                        value=None,
                        children=[node],
                        props={
                            "class": "hello-div",
                            "id": "test"
                        })
        props_result = 'class="hello-div" id="test"'
        # print(node2)
        self.assertEqual(props_result, node2.props_to_html())

    def test_eq2(self):
        node = HTMLNode(tag="p",
                        value="hello peeps",
                        children=None,
                        props={
                            "class": "hello-text",
                            "id": "salutation"
                        })
        node2 = HTMLNode(tag="d",
                        value=None,
                        children=[node],
                        props={
                            "class": "hello-div",
                            "id": "test"
                        })
        props_result = 'class="hello-text" id="salutation"'
        # print(node2)
        self.assertEqual(props_result, node.props_to_html())


if __name__ == "__main__":
    unittest.main()