import unittest

from textnode import TextType, TextNode
from text_to_html import text_node_to_html_node


class TestTextToHTML(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold_italic_and_code(self):
        bold_node = TextNode("This is a bold node", TextType.BOLD)
        italic_node = TextNode("This is an italic node", TextType.ITALIC)
        code_node = TextNode("This is a code node", TextType.CODE)

        leaf_bold_node = text_node_to_html_node(bold_node)
        leaf_italic_node = text_node_to_html_node(italic_node)
        leaf_code_node = text_node_to_html_node(code_node)

        self.assertEqual(leaf_bold_node.tag, "b")
        self.assertEqual(leaf_italic_node.tag, "i")
        self.assertEqual(leaf_code_node.tag, "code")

    def test_link(self):
        link_node = TextNode("Boot.dev", TextType.LINK, "https://www.boot.dev")
        leaf_link_node = text_node_to_html_node(link_node)
        self.assertEqual(leaf_link_node.tag, "a")
        self.assertEqual(leaf_link_node.value, "Boot.dev")
        self.assertEqual(leaf_link_node.props, {"href": "https://www.boot.dev"})

    def test_image(self):
        image_node = TextNode(
            "This is an image", TextType.IMAGE, "/home/image/cats.jpg"
        )
        leaf_image_node = text_node_to_html_node(image_node)
        self.assertEqual(leaf_image_node.tag, "img")
        self.assertEqual(leaf_image_node.value, "")
        self.assertEqual(
            leaf_image_node.props,
            {"src": "/home/image/cats.jpg", "alt": "This is an image"},
        )

    def test_raise(self):
        bork = TextNode(None, TextType.LINK)
        self.assertRaises(Exception, text_node_to_html_node, bork)
        snork = TextNode(None, TextType.IMAGE)
        self.assertRaises(Exception, text_node_to_html_node, snork)

    def test_empty(self):
        none_node = text_node_to_html_node(TextNode(None, TextType.TEXT))
        self.assertEqual(none_node.tag, None)
        self.assertEqual(none_node.value, None)
        empty_node = text_node_to_html_node(TextNode("", TextType.ITALIC))
        self.assertEqual(empty_node.tag, "i")
        self.assertEqual(empty_node.value, "")
        whitespace_node = text_node_to_html_node(TextNode("     ", TextType.BOLD))
        self.assertEqual(whitespace_node.tag, "b")
        self.assertEqual(whitespace_node.value, "     ")


if __name__ == "__main__":
    unittest.main()
