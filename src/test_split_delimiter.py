import unittest
from inline import split_nodes_delimiter
from textnode import TextNode, TextType


class TestSplitDelimiter(unittest.TestCase):

    def test_split_nodes_delimiter_basic(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        expected = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ]
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(result, expected)

    def test_split_nodes_delimiter_multiple(self):
        node = TextNode("Here is `one` and `two` codes", TextType.TEXT)
        expected = [
            TextNode("Here is ", TextType.TEXT),
            TextNode("one", TextType.CODE),
            TextNode(" and ", TextType.TEXT),
            TextNode("two", TextType.CODE),
            TextNode(" codes", TextType.TEXT),
        ]
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(result, expected)

    def test_delim_bold_and_italic(self):
        node = TextNode("**bold** and *italic*", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        new_nodes = split_nodes_delimiter(new_nodes, "*", TextType.ITALIC)

        self.assertListEqual(
            [
                TextNode("bold", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
            ],
            new_nodes,
        )


if __name__ == "__main__":
    unittest.main()
