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
        text = text[index+1:]
        index = text.find(delimiter)
        if index == -1:
            raise ValueError(f"unmatched delimiter: {delimiter}")
        if len(text[:index]) > 0:
            splits.append(TextNode(text=text[:index],text_type=text_type))
        if len(text[index+1:]) > 0:
            splits.append(TextNode(text=text[index+1:],text_type=textType))
        result.extend(splits)
    return result


def extract_markdown_images(text):
    matches = re.findall(r"\!\[([\w\s\d]+)\]\((https?:\/\/[a-z0-9]+(?:[-.][a-z0-9]+)*(?::[0-9]{1,5})?(?:\/[a-zA-Z0-9]+)*(?:\.[a-z]{2,5})*)\)", text)
    extract = []
    for match in matches:
        extract.append(match)
        # extract.append((match[0], match[1]))
    return extract

def extract_markdown_links(text):
    matches = re.findall(r"\[([\w\s\d]+)\]\((https?:\/\/[a-z0-9]+(?:[-.][a-z0-9]+)*(?::[0-9]{1,5})?(?:\/[a-zA-Z0-9@]+)*(?:\.[a-z]{2,5})*)\)", text)
    extract = []
    for match in matches:
        extract.append(match)
    return extract
