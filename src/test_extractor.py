import unittest

from extractor import extract_markdown_images, extract_markdown_links


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


if __name__ == "__main__":
    unittest.main()
