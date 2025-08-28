import unittest

from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode
from main import text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
    def test_link(self):
        node = TextNode("click here!", TextType.LINK, "https://armandomarquez.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "click here!")
        self.assertEqual(html_node.props, {"href": "https://armandomarquez.com"})

if __name__ == "__main__":
    unittest.main()