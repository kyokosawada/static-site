from textnode import TextNode, TextType
import re


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for node in old_nodes:
        current_text = node.text

        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        while current_text:

            first_delimiter = current_text.find(delimiter)
            # print(f"first- {first_delimiter}")

            if first_delimiter != -1:

                second_delimiter = current_text.find(
                    delimiter, first_delimiter + len(delimiter)
                )
                # print(f"second- {second_delimiter}")

                if second_delimiter == -1:
                    raise ValueError("Unmatched delimiter")

                else:
                    new_nodes.append(
                        TextNode(current_text[:first_delimiter], TextType.TEXT)
                    )
                    new_nodes.append(
                        TextNode(
                            current_text[
                                first_delimiter + len(delimiter) : second_delimiter
                            ],
                            text_type,
                        )
                    )

                    current_text = current_text[second_delimiter + len(delimiter) :]
                    # print(current_text)
            else:
                new_nodes.append(TextNode(current_text, TextType.TEXT))
                break

    return new_nodes


def extract_markdown_images(text):
    match = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return match


def extract_markdown_links(text):
    match = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return match


def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        current_text = node.text

        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        images = extract_markdown_images(node.text)
        if len(images) == 0:
            new_nodes.append(node)
            continue

        for image in images:
            sections = current_text.split(f"![{image[0]}]({image[1]})", 1)
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))

            new_nodes.append(TextNode(image[0], TextType.IMAGE, image[1]))

            current_text = sections[1]

        if current_text != "":
            new_nodes.append(TextNode(current_text, TextType.TEXT))

    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        current_text = node.text

        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        links = extract_markdown_links(node.text)
        if len(links) == 0:
            new_nodes.append(node)
            continue

        for link in links:
            sections = current_text.split(f"[{link[0]}]({link[1]})", 1)
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))

            new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))

            current_text = sections[1]

        if current_text != "":
            new_nodes.append(TextNode(current_text, TextType.TEXT))

    return new_nodes


def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "*", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)

    return nodes
