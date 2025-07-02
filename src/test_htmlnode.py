import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_format(self):
        node = HTMLNode("Hello", "World", None, {"href": "https://www.boot.dev"})
        nodeMom = HTMLNode("The mom", "is here", [node, node], None)
        self.assertIs(nodeMom.children[0], node)
        self.assertIsInstance(nodeMom.children[0], HTMLNode)
        self.assertIs(type(node.props), dict)
        self.assertIs(type(nodeMom.children), list)

    def test_not_format(self):
        node = HTMLNode("Hello", "World", None, {"href": "https://www.boot.dev"})
        nodeMom = HTMLNode("The mom", "is here", [node, node], None)
        self.assertIsNot(node, nodeMom)
        self.assertIsNone(node.children)
        self.assertIsNone(nodeMom.props)
        self.assertIsNot(type(nodeMom.children), dict)
        self.assertIsNot(type(node.props), list)

    def test_prop_print(self):
        node = HTMLNode("Hello", "World", None, {"href": "https://www.boot.dev"})
        self.assertEqual(node.props_to_html(), ' href="https://www.boot.dev"')
        big_dict = {"href": "www.google.com", "target": "_blank"}
        node2 = HTMLNode(None, None, None, big_dict)
        self.assertEqual(
            node2.props_to_html(), ' href="www.google.com" target="_blank"'
        )
        self.assertEqual(HTMLNode().props_to_html(), "")

    def test_raise_trouble(self):
        node = HTMLNode()
        self.assertRaises(NotImplementedError, node.to_html)


if __name__ == "__main__":
    unittest.main()
