import unittest

from htmlnode import ParentNode, LeafNode


class TestLeafNode(unittest.TestCase):

    def test_to_html_basic(self):
        parent = ParentNode(
            "div",
            [
                LeafNode("p", "Hello world!"),
                LeafNode("span", "This is a test."),
            ],
        )
        self.assertEqual(
            "<div><p>Hello world!</p><span>This is a test.</span></div>",
            parent.to_html(),
        )

    def test_to_html_deeply_nested(self):
        deeply_nested = ParentNode(
            "div",
            [
                ParentNode(
                    "ul",
                    [
                        LeafNode("li", "Item 1"),
                        ParentNode(
                            "li",
                            [
                                LeafNode(None, "Item with nested content"),
                                LeafNode("span", "(additional info)"),
                            ],
                        ),
                        LeafNode("li", "Item 3"),
                    ],
                )
            ],
        )
        self.assertEqual(
            "<div><ul><li>Item 1</li><li>Item with nested content<span>(additional info)</span></li><li>Item 3</li></ul></div>",
            deeply_nested.to_html(),
        )

    def test_to_html_no_children(self):
        invalid_parent = ParentNode("div", [])

        self.assertRaises(ValueError, invalid_parent.to_html)

    def test_to_html_none_tag(self):
        invalid_tag = ParentNode(None, [LeafNode("p", "Invalid parent tag")])

        self.assertRaises(ValueError, invalid_tag.to_html)

    def test_to_html_mixed(self):
        mixed_children = ParentNode(
            "section",
            [
                ParentNode(
                    "article",
                    [
                        LeafNode("h1", "Title"),
                        LeafNode("p", "This is a paragraph."),
                    ],
                ),
                LeafNode("footer", "Footer content."),
            ],
        )

        self.assertEqual(
            "<section><article><h1>Title</h1><p>This is a paragraph.</p></article><footer>Footer content.</footer></section>",
            mixed_children.to_html(),
        )


if __name__ == "__main__":
    unittest.main()
