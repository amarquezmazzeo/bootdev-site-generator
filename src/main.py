from textnode import TextNode, TextType

print("hello world")
tex = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
print(tex)