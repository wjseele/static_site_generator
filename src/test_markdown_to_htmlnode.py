import unittest
from markdown_to_htmlnode import markdown_to_html_node
from htmlnode import HTMLNode, ParentNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_paragraphs(self):
        md = """
    This is **bolded** paragraph
    text in a p
    tag here

    This is another paragraph with _italic_ text and `code` here

    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_text_with_title(self):
        md = """
            # Title

            
            ## Subtitle


            text
        """
        expected = "<div><h1>Title</h1><h2>Subtitle</h2><p>text</p></div>"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html, expected)

    def test_codeblock(self):
        md = """
    ```
    This is text that _should_ remain
    the **same** even with inline stuff
    ```
    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_unordered_list(self):
        md = """- item1
        - item2
        - item3
        """
        expected = "<div><ul><li>item1</li><li>item2</li><li>item3</li></ul></div>"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html, expected)

    def test_ordered_list(self):
        md = """1. item1
        2. item2
        3. item3
        """
        expected = "<div><ol><li>item1</li><li>item2</li><li>item3</li></ol></div>"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html, expected)


if __name__ == "__main__":
    unittest.main()
