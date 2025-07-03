import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


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

        oops = node1 == leaf1
        self.assertIs(oops, False)
        self.assertIs(node1.__eq__("Mittens"), NotImplemented)

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

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_big_family(self):
        child1 = LeafNode("a", "child1", {"href": "www.boot.dev"})
        child2 = LeafNode("li", "child2")
        child3 = LeafNode("li", "child3")
        parent2 = ParentNode("ul", [child2, child2, child2])
        parent3 = ParentNode("ul", [child3, child3])
        parent1 = ParentNode("p", [child1, parent2, parent3])
        self.assertEqual(
            parent1.to_html(),
            '<p><a href="www.boot.dev">child1</a><ul><li>child2</li><li>child2</li><li>child2</li></ul><ul><li>child3</li><li>child3</li></ul></p>',
        )


if __name__ == "__main__":
    unittest.main()
