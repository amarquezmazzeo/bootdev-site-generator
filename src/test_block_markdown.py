import unittest

from textnode import TextNode, TextType
from block_markdown import (
    markdown_to_blocks,
    block_to_block_type,
    BlockType
)

class TestHandleBlockMarkdownCode(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph





This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_block_to_block_type_heading(self):
        block = "### This is a 3rd level heading"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.HEADING)

    def test_block_to_block_type_paragraph(self):
        block = "#¿Qué es la vida? Un frenesí. ¿Qué es la vida? Una ilusión, una sombra, una ficción, y el mayor bien es pequeño; que toda la vida es sueño, y los sueños, sueños son."
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.PARAGRAPH)

    def test_block_to_block_type_ol(self):
        block = "1. Un frenesí.\n2. Una ilusión.\n3. Una sombra.\n4. Una ficción."
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.ORDERED_LIST)

    def test_block_to_block_type_ul(self):
        block = "- Un frenesí.\n- Una ilusión.\n- Una sombra.\n- Una ficción."
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.UNORDERED_LIST)

    def test_block_to_block_type_code(self):
        block = "```\nprint('hello world')\n```"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.CODE)

    def test_block_to_block_type_code_blank(self):
        block = "```\n```"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.CODE)

    def test_block_to_block_type_quote(self):
        block = ">The mystery of human existence lies not in just staying alive, but in finding something to live for."
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.QUOTE)

    def test_block_to_block_type_quote_blank(self):
        block = ">"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.QUOTE)


if __name__ == "__main__":
    unittest.main()
