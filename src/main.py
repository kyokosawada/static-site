from htmlnode import *
from textnode import *


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

    """

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


if __name__ == "__main__":
    main()
