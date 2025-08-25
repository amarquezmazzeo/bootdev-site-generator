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
    

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("Leaf node must have a value")
        
        if self.tag is None:
            return str(self.value)

        if not self.props:
            return f"<{self.tag}>{str(self.value)}</{self.tag}>"
        
        return f"<{self.tag} {self.props_to_html()}>{str(self.value)}</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if self.tag is None:
            raise ValueError("Parent node must have a tag")
        if self.children is None:
            raise ValueError("Parent node must have at least one child node")
        
        html_props = f" {self.props_to_html()}" if self.props else ""
        result = f"<{self.tag}{html_props}>"
        # print(result)
        for child in self.children:
            result += child.to_html()
        result += f"</{self.tag}>"
        return result