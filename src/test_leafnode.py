import unittest

from htmlnode import LeafNode


class TestLeafNode(unittest.TestCase):

    def test_to_html(self):
        node = LeafNode("p", "hello")
        self.assertEqual("<p>hello</p>", node.to_html())

    def test_to_html_props(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(
            '<a href="https://www.google.com">Click me!</a>', node.to_html()
        )

    def test_to_html_no_tag(self):
        node = LeafNode(None, "Just some text")
        self.assertEqual("Just some text", node.to_html())

    def test_to_html_no_tag_with_props(self):
        node = LeafNode(None, "Just some text", {"href": "https://www.google.com"})
        self.assertEqual("Just some text", node.to_html())


if __name__ == "__main__":
    unittest.main()
