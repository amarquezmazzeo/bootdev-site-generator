import unittest

from textnode import TextNode, TextType
from split import split_nodes_delimiter

class TestSplitNodesDelimiterCode(unittest.TestCase):
    def test_split_backticks_single(self):
        node = TextNode("This has a `code` bit", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        print(result)

        self.assertEqual(len(result), 3)

        self.assertIsInstance(result[0], TextNode)  # class type checked via attributes below
        self.assertEqual(result[0].text, "This has a ")
        self.assertEqual(result[0].text_type, TextType.TEXT)

        self.assertEqual(result[1].text, "code")
        self.assertEqual(result[1].text_type, TextType.CODE)

        self.assertEqual(result[2].text, " bit")
        self.assertEqual(result[2].text_type, TextType.TEXT)

    def test_non_text_nodes_passthrough(self):
        # a CODE node should be left untouched by this function
        node = TextNode("already code", TextType.CODE)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(len(result), 1)
        self.assertIs(result[0], node)

    def test_unmatched_backtick_raises(self):
        node = TextNode("Unclosed `code span here", TextType.TEXT)
        with self.assertRaises(Exception):
            split_nodes_delimiter([node], "`", TextType.CODE)

if __name__ == "__main__":
    unittest.main()