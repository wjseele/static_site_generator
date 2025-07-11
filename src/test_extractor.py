import unittest

from extractor import (
    extract_markdown_images,
    extract_markdown_links,
    split_nodes_image,
    split_nodes_link,
)
from textnode import TextType, TextNode


class TestExtractor(unittest.TestCase):
    def test_image_extract(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        expected = [
            ("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
            ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg"),
        ]
        self.assertEqual(extract_markdown_images(text), expected)

    def test_link_extract(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        expected = [
            ("to boot dev", "https://www.boot.dev"),
            ("to youtube", "https://www.youtube.com/@bootdotdev"),
        ]
        self.assertEqual(extract_markdown_links(text), expected)

    def test_link_and_image_coexistence(self):
        text = "This is an ![image](https://i.imgur.com/example.png) and a [link](https://example.com)."
        expected = [("link", "https://example.com")]
        self.assertEqual(extract_markdown_links(text), expected)

    def test_empty_extract(self):
        text = ""
        expected = []
        self.assertEqual(extract_markdown_images(text), expected)
        self.assertRaises(ValueError, extract_markdown_images, None)

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_link(self):
        node = TextNode(
            "This is text with a [Boot](https://boot.dev) and another [Google](https://www.google.com)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("Boot", TextType.LINK, "https://boot.dev"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("Google", TextType.LINK, "https://www.google.com"),
            ],
            new_nodes,
        )

    def test_split_combo(self):
        node = TextNode(
            "This is a [link](https://boot.dev) and an ![image](https://image.com)",
            TextType.TEXT,
        )
        first_run = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is a [link](https://boot.dev) and an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://image.com"),
            ],
            first_run,
        )
        second_run = split_nodes_link(first_run)
        self.assertListEqual(
            [
                TextNode("This is a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
                TextNode(" and an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://image.com"),
            ],
            second_run,
        )
        nested_run = split_nodes_image(split_nodes_link([node]))
        self.assertListEqual(
            [
                TextNode("This is a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
                TextNode(" and an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://image.com"),
            ],
            nested_run,
        )


if __name__ == "__main__":
    unittest.main()
