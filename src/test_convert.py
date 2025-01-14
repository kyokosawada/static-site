import unittest

from htmlnode import LeafNode
from textnode import TextNode, TextType, text_node_to_html_node


class TestHTMLNode(unittest.TestCase):
    def test_text_node(self):
        node = TextNode("This is a text", TextType.TEXT)
        html = text_node_to_html_node(node)
        self.assertIsInstance(html, LeafNode)
        self.assertEqual(html.tag, None)
        self.assertEqual(html.value, "This is a text")

    def test_bold_node(self):
        node = TextNode("This is bold", TextType.BOLD)
        html = text_node_to_html_node(node)
        self.assertIsInstance(html, LeafNode)
        self.assertEqual(html.tag, "b")
        self.assertEqual(html.value, "This is bold")

    def test_italic_node(self):
        node = TextNode("This is italic", TextType.ITALIC)
        html = text_node_to_html_node(node)
        self.assertIsInstance(html, LeafNode)
        self.assertEqual(html.tag, "i")
        self.assertEqual(html.value, "This is italic")

    def test_code_node(self):
        node = TextNode("This is code", TextType.CODE)
        html = text_node_to_html_node(node)
        self.assertIsInstance(html, LeafNode)
        self.assertEqual(html.tag, "code")
        self.assertEqual(html.value, "This is code")

    def test_link_node(self):
        node = TextNode("Click me", TextType.LINK, "https://www.google.com")
        html = text_node_to_html_node(node)
        self.assertIsInstance(html, LeafNode)
        self.assertEqual(html.tag, "a")
        self.assertEqual(html.value, "Click me")
        self.assertEqual(html.props["href"], "https://www.google.com")

    def test_image_node(self):
        node = TextNode("my image", TextType.IMAGE, "https://boot.dev/image.png")
        html = text_node_to_html_node(node)
        self.assertIsInstance(html, LeafNode)
        self.assertEqual(html.tag, "img")
        self.assertEqual(html.value, "")
        self.assertEqual(html.props["src"], "https://boot.dev/image.png")
        self.assertEqual(html.props["alt"], "my image")


if __name__ == "__main__":
    unittest.main()
