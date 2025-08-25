import unittest

from htmlnode import HTMLNode, LeafNode


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
        # print(node2)
        props_result = 'class="hello-text" id="salutation"'
        self.assertEqual(props_result, node.props_to_html())

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
    def test_leaf_to_html_url(self):
        nodew = LeafNode("a", "Click here!",
                        props={"href": "https://armandomarquez.com",
                                "target": "_blank"})
        print(nodew.props_to_html())
        self.assertEqual(nodew.to_html(), '<a href="https://armandomarquez.com" target="_blank">Click here!</a>')

if __name__ == "__main__":
    unittest.main()