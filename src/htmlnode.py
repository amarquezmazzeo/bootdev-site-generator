class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        result = ""
        for k, v in self.props.items():
            result+= f'{k}="{v}" '
        return result[:-1]
    
    def __repr__(self):
        result = "HTMLNode(\n"
        result += f"Tag: {self.tag}\n"
        result += f"Value: {self.value}\n"
        result += f"Props {self.props_to_html()}\n"
        if self.children is None:
            result += f"Children: None"
        else:
            result += f"Children: {[x.tag for x in self.children]}\n"
        result += ")"
        return result
        