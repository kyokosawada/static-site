from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for node in old_nodes:
        current_text = node.text

        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        while current_text:

            first_delimiter = current_text.find(delimiter)

            if first_delimiter != -1:

                second_delimter = current_text.find(
                    delimiter, first_delimiter + len(delimiter)
                )
                if second_delimter == -1:
                    raise ValueError("Unmatched delimiter")

                else:
                    new_nodes.append(
                        TextNode(current_text[:first_delimiter], TextType.TEXT)
                    )
                    new_nodes.append(
                        TextNode(
                            current_text[
                                first_delimiter + len(delimiter) : second_delimter
                            ],
                            text_type,
                        )
                    )

                    current_text = current_text[second_delimter + len(delimiter) :]
            else:
                new_nodes.append(TextNode(current_text, TextType.TEXT))
                break

    return new_nodes
