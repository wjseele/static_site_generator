import html


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
        prop_strings = [
            f' {prop}="{html.escape(self.props[prop])}"' for prop in self.props
        ]
        return "".join(prop_strings)

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

    def __eq__(node1, node2):
        tag = node1.tag == node2.tag
        value = node1.value == node2.value
        children = node1.children == node2.children
        props = node1.props == node2.props
        return tag and value and children and props


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("This node lacks a value")
        if self.tag is None:
            return self.value
        return (
            f"<{self.tag}{self.props_to_html()}>{html.escape(self.value)}</{self.tag}>"
        )
