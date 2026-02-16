import re
from enum import Enum
from textnode import TextNode, TextType

class BlockType(Enum):
    PARAGRAPH = 'paragraph'
    HEADING = 'heading'
    CODE = 'code'
    QUOTE = 'quote'
    UNORDERED_LIST = 'unordered_list'
    ORDERED_LIST = 'ordered_list'

def markdown_to_blocks(markdown):
    lines = markdown.split("\n\n")
    lines = [line.strip() for line in lines if len(line) > 0]
    return lines

def block_to_block_type(block):
    heading_match = re.match(r"(#+) ", block)
    if heading_match:
        return BlockType.HEADING
    code_match = block[:3] == '```' and block[-3:] == '```'
    if code_match:
        return BlockType.CODE
    quote_match = block[0] == '>'
    if quote_match:
        return BlockType.QUOTE
    lines = block.split("\n")
    ul_match = True
    ol_match = True
    i = 1
    for line in lines:
        if ul_match and line[:2] != '- ':
            ul_match = False
        if ol_match and not re.match(f'({i})\.\ ', line):
            ol_match = False
        if not ul_match and not ol_match:
            return BlockType.PARAGRAPH
        i+=1
    if ul_match:
        return BlockType.UNORDERED_LIST
    if ol_match:
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH
