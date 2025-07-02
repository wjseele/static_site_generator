import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        nodeItalic = TextNode("This is a text node", TextType.ITALIC)
        nodeCode = TextNode("This is a text node", TextType.CODE)
        self.assertNotEqual(nodeItalic, nodeCode)

    def test_has_url(self):
        nodeUrl = TextNode("This is an url", TextType.LINK, "https://www.boot.dev")
        self.assertIsNotNone(nodeUrl.url)
        self.assertEqual(nodeUrl.url, "https://www.boot.dev")


if __name__ == "__main__":
    unittest.main()
