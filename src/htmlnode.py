class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("Should be overridden by child")

    def props_to_html(self):
        if self.props is None:
            return ""
        string_to_return = ""
        for prop in self.props:
            string_to_return += f' {prop}="{self.props[prop]}"'
        return string_to_return

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
