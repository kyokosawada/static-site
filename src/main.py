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
    """

    leaf = LeafNode("a", "Click me!", {"href": "https://www.google.com"})

    print(leaf.to_html())


if __name__ == "__main__":
    main()
