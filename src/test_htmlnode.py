import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


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
        # print(nodew.props_to_html())
        self.assertEqual(nodew.to_html(), '<a href="https://armandomarquez.com" target="_blank">Click here!</a>')
    
    def test_parent_to_html_div(self):
        grandchild_node1 = LeafNode("h3", "Hello, I am Boots",
                               props={"class": "highlight"})
        grandchild_node2 = LeafNode("p", "Your coding friend")
        child_node1 = LeafNode("h2", "About Me",
                               props={"class": "subtitle white"})
        child_node2 = ParentNode("div", [grandchild_node1, grandchild_node2],
                               props={"class": "content cols2"})
        node = ParentNode("div", [child_node1, child_node2])
        # print(node.to_html())
        self.assertEqual(node.to_html(), '<div><h2 class="subtitle white">About Me</h2><div class="content cols2"><h3 class="highlight">Hello, I am Boots</h3><p>Your coding friend</p></div></div>')

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

if __name__ == "__main__":
    unittest.main()
