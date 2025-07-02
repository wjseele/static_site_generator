import unittest

from htmlnode import HTMLNode, LeafNode


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
        leaf = LeafNode(None, None)
        self.assertRaises(ValueError, leaf.to_html)

    def test_eq(self):
        node1 = HTMLNode("p", "Hello, world!")
        node2 = HTMLNode("p", "Hello, world!")
        self.assertEqual(node1, node2)

        leaf1 = LeafNode("a", "Leaf time")
        leaf2 = LeafNode("a", "Leaf time")
        self.assertEqual(leaf1, leaf2)

    def test_leaf_to_html(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
        tagless_node = LeafNode(None, "Wobbles")
        self.assertEqual(tagless_node.to_html(), "Wobbles")
        big_dict = {"href": "www.google.com", "target": "_blank"}
        node2 = LeafNode("a", "Google", big_dict)
        self.assertEqual(
            node2.to_html(), '<a href="www.google.com" target="_blank">Google</a>'
        )
        borked_node = LeafNode(
            "a", "<b>Bork</b>", {"target": """Hello "fellow" borkers!"""}
        )
        self.assertEqual(
            borked_node.to_html(),
            '<a target="Hello &quot;fellow&quot; borkers!">&lt;b&gt;Bork&lt;/b&gt;</a>',
        )


if __name__ == "__main__":
    unittest.main()
