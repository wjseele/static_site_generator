import unittest

from text_to_textnodes import text_to_textnodes
from textnode import TextNode, TextType


class TestTextToTextNodes(unittest.TestCase):
    def test_all_the_things(self):
        sample = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode(
                "obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"
            ),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ]
        self.assertEqual(text_to_textnodes(sample), expected)

    def test_empty(self):
        sample = ""
        self.assertRaises(ValueError, text_to_textnodes, sample)

    def test_plain(self):
        sample = "plain text"
        self.assertEqual(
            text_to_textnodes(sample), [TextNode("plain text", TextType.TEXT)]
        )

    def test_single_type(self):
        sample = "**bolded**"
        expected = [TextNode("bolded", TextType.BOLD)]
        self.assertEqual(text_to_textnodes(sample), expected)


if __name__ == "__main__":
    unittest.main()
