from htmlnode import *
from textnode import *
from inline import *
from block import *


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

    

    node = TextNode("**bold** and *italic*", TextType.TEXT)
    result = split_nodes_delimiter([node], "**", TextType.BOLD)
    result = split_nodes_delimiter(result, "*", TextType.ITALIC)
    print(result)

    

    text = "Here is an image ![alt text](https://example.com/image.jpg) and another ![alt2](https://example.com/image2.jpg)"
    print(extract_markdown_images(text))
   

    node = TextNode(
        "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
        TextType.TEXT,
    )

    new_nodes = split_nodes_image([node])
    print(new_nodes)
    

    text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
    result = text_to_textnodes(text)
    print(result)

    """

    markdown = """ # Heading


Some text


  asd


* List item"""

    print(markdown_to_blocks(markdown))


if __name__ == "__main__":
    main()
