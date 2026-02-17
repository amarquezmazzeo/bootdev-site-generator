import re
from enum import Enum
from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode
from shared import text_node_to_html_node
from inline_markdown import text_to_textnodes

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
        if ol_match and not re.match(rf'({i})\.\ ', line):
            ol_match = False
        if not ul_match and not ol_match:
            return BlockType.PARAGRAPH
        i+=1
    if ul_match:
        return BlockType.UNORDERED_LIST
    if ol_match:
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH

def block_to_html_node(block): # TODO: break down long func
    list_tag = {
        BlockType.UNORDERED_LIST : 'ul',
        BlockType.ORDERED_LIST : 'ol'
    }

    list_tag_re = {
        BlockType.UNORDERED_LIST : r"\-\ ",
        BlockType.ORDERED_LIST : r"[0-9]+\.\ "
    }


    block_type = block_to_block_type(block)
    if block_type == BlockType.HEADING:
        h_num = re.findall(r"^(#+) ", block)
        text = re.sub(r"\#+\ ", "", block, 1),
        c, v = text_to_children_value(text)
        if c is None:
            html_node = LeafNode(
                tag = f"h{len(h_num)}",
                value = v,
                props = None
            )
        else:
            html_node = ParentNode(
                tag = f"h{len(h_num)}",
                children = c,
                props = None
            )
        return html_node
    if block_type == BlockType.CODE:
        inner_node = LeafNode(
            tag = "code",
            value = block[4:-3],
            props = None
        )
        html_node = ParentNode(
            tag = "pre",
            children = [inner_node],
            props = None
        )
        return html_node
    if block_type == BlockType.QUOTE:
        text = re.sub(r"\>\ *", "", block, 1),
        c, v = text_to_children_value(text)
        if c is None:
            html_node = LeafNode(
                tag = "blockquote",
                value = v,
                props = None
            )
        else:
            html_node = ParentNode(
                tag = "blockquote",
                children = c,
                props = None
            )
        return html_node
    if block_type in list_tag:
        inner_nodes = []
        items = block.split('\n')
        for item in items:
            text = re.sub(list_tag_re[block_type], "", item, 1)
            c, v = text_to_children_value(text)
            if c is None:
                inner_nodes.append(
                    LeafNode(
                        tag = "li",
                        value = v,
                        props = None
                    )
                )
            else:
                inner_nodes.append(
                    ParentNode(
                        tag = "li",
                        children = c,
                        props = None
                    )
                )
        html_node = ParentNode(
            tag = list_tag[block_type],
            children = inner_nodes,
            props = None,
        )
        return html_node
    block = block.replace('\n', ' ')
    c, v = text_to_children_value(block)
    if c is None:
        html_node = LeafNode(
            tag = "p",
            value = v,
            props = None,
        )
    else:
        html_node = ParentNode(
            tag = "p",
            children = c,
            props = None,
        )
    return html_node

def text_to_children_value(text):
    html_children = []
    text_nodes = text_to_textnodes(text)
    for text_node in text_nodes:
        html_children.append(text_node_to_html_node(text_node))
    if len(html_children) <= 1:
        return (None, html_children)
    return (html_children, None)

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    html_nodes = []
    for block in blocks:
        html_nodes.append(block_to_html_node(block))
    parent_node = ParentNode(
        tag = "div",
        children = html_nodes,
        props={'id' : 'parent'},
    )
    return parent_node

