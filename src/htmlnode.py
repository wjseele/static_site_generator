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

    def __eq__(self, other):
        if self.__class__ is not other.__class__:
            return NotImplemented
        tag = self.tag == other.tag
        value = self.value == other.value
        children = self.children == other.children
        props = self.props == other.props
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


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("This node lacks a tag")
        if self.children is None or len(self.children) == 0:
            raise ValueError("This parent has no children")
        return_string = f"<{self.tag}{self.props_to_html()}>"

        for child in self.children:
            return_string += child.to_html()

        return_string += f"</{self.tag}>"
        return return_string
