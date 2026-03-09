import re
from textnode import TextNode, TextType

# TODO: make a better version of this
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    result = []
    for old_node in old_nodes:
        text = old_node.text
        textType = old_node.text_type
        splits = []
        index = text.find(delimiter)
        if index == -1:
            result.append(old_node)
            continue
        if len(text[:index]) > 0:
            splits.append(TextNode(text=text[:index],text_type=textType))
        text = text[index+len(delimiter):]
        index = text.find(delimiter)
        if index == -1:
            raise ValueError(f"unmatched delimiter: {delimiter}")
        if len(text[:index]) > 0:
            splits.append(TextNode(text=text[:index],text_type=text_type))
        if len(text[index+len(delimiter):]) > 0:
            splits.append(TextNode(text=text[index+len(delimiter):],text_type=textType))
        result.extend(splits)
    return result


def extract_markdown_images(text):
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    extract = []
    for match in matches:
        extract.append(match)
        # extract.append((match[0], match[1]))
    return extract

def extract_markdown_links(text):
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    extract = []
    for match in matches:
        extract.append(match)
    return extract

def split_nodes_image(old_nodes):
    result = []
    for old_node in old_nodes:
        text = old_node.text
        # skip if text is empty
        if len(text) == 0:
            continue
        images = extract_markdown_images(text)
        # process as is if no images exist
        if len(images) == 0:
            result.append(old_node)
            continue
        buffer = [text]
        for image in images:
            buffer =  buffer[-1].split(f"![{image[0]}]({image[1]})", 1)
            if len(buffer[0]) != 0:
                result.append(TextNode(buffer[0], TextType.TEXT))
            result.append(TextNode(image[0], TextType.IMAGE, image[1]))
        if len(buffer[-1]) != 0:
            result.append(TextNode(buffer[-1], TextType.TEXT))
    return result

def split_nodes_link(old_nodes):
    result = []
    for old_node in old_nodes:
        text = old_node.text
        # skip if text is empty
        if len(text) == 0:
            continue
        links = extract_markdown_links(text)
        # process as is if no links exist
        if len(links) == 0:
            result.append(old_node)
            continue
        buffer = [text]
        for link in links:
            buffer =  buffer[-1].split(f"[{link[0]}]({link[1]})", 1)
            if len(buffer[0]) != 0:
                result.append(TextNode(buffer[0], TextType.TEXT))
            result.append(TextNode(link[0], TextType.LINK, link[1]))
        if len(buffer[-1]) != 0:
            result.append(TextNode(buffer[-1], TextType.TEXT))
    return result

def text_to_textnodes(text):
    delimiters = {
        "**": TextType.BOLD,
        "__": TextType.BOLD,
        "_": TextType.ITALIC,
        "`": TextType.CODE
    }
    node = TextNode(text, TextType.TEXT)
    nodes = [node]
    for k, v in delimiters.items():
        nodes = split_nodes_delimiter(nodes, k, v)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes
