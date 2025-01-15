from htmlnode import *
from textnode import *
from split_delimiter import *


def main():
    props = {
        "href": "https://www.google.com",
        "target": "_blank",
    }
    """
    test = TextNode("This is a text node", TextType.TEXT, "https://www.boot.dev")
    print(repr(test))

    html = HTMLNode("href", "value", "children", props)
    print(repr(html))
    

    leaf = LeafNode("a", "Click me!", {"href": "https://www.google.com"})

    print(leaf.to_html())

    

    parent = ParentNode(
        "p",
        [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ],
    )

    # print(parent.to_html())
    print(repr(parent))

    """

    node = TextNode("**bold** and *italic*", TextType.TEXT)
    result = split_nodes_delimiter([node], "**", TextType.BOLD)
    result = split_nodes_delimiter(result, "*", TextType.ITALIC)
    print(result)


if __name__ == "__main__":
    main()
