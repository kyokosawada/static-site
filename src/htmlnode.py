class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html method not implemented")

    def props_to_html(self):
        if self.props == None:
            return ""

        html = ""
        for i, key in enumerate(self.props, start=1):
            html += f' {key}="{self.props[key]}"'

        return html

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, props=props)

    def to_html(self):

        if self.value is None:
            raise ValueError("All leaf nodes must have a value.")

        if self.tag is None or self.tag == "":
            return self.value

        prop_string = self.props_to_html()
        return f"<{self.tag}{prop_string}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, props={self.props})"


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, children=children, props=props)

    def to_html(self):
        string = ""
        if self.tag is None:
            raise ValueError("All parent nodes must have a tag.")

        if self.children is None or self.children == []:
            raise ValueError("All parent nodes must have children.")

        for child in self.children:
            string += child.to_html()

        return f"<{self.tag}>{string}</{self.tag}>"

    def __repr__(self):
        return f"ParentNode({self.tag}, {self.children}, props={self.props})"
