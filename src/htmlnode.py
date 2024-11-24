from typing import Optional
from textnode import TextType, TextNode
import tags


class HTMLNode:
    def __init__(
        self,
        tag: Optional[str] = None,
        value: Optional[str] = None,
        children: Optional[list["HTMLNode"]] = None,
        props: Optional[dict[str, str]] = None,
    ) -> "HTMLNode":
        self.tag: Optional[str] = tag
        self.value: Optional[str] = value
        self.children: list[HTMLNode] = (
            children if children is not None else None
        )
        self.props: dict[str, str] = props if props is not None else None

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self) -> str:
        output_html: str = ""
        if self.props is None:
            return ""
        for key, value in self.props.items():
            output_html += f' {key}="{value}"'
        return output_html

    def __repr__(self) -> str:
        parts: list[str] = []
        if self.tag is not None:
            parts.append(f"tag = '{self.tag}'")
        if self.value is not None:
            parts.append(f"value = '{self.value}'")
        if self.children is not None:
            parts.append(f"children={self.children}")
        if self.props is not None:
            parts.append(f"props = {self.props}")

        return f"HTMLNode({', '.join(parts)})"


class LeafNode(HTMLNode):
    def __init__(
        self,
        tag: Optional[str] = None,
        value: str = None,
        props: Optional[dict[str, str]] = None,
    ) -> "LeafNode":
        super().__init__(tag, value, None, props)

    def to_html(self) -> str:
        if self.value is None or self.value == "":
            raise ValueError("All leaf nodes must have a value.")
        elif self.tag is None:
            return self.value
        else:
            opening_tag = f"<{self.tag}{self.props_to_html()}>"
            closing_tag = f"</{self.tag}>"
            return opening_tag + self.value + closing_tag


class ParentNode(HTMLNode):
    def __init__(
        self,
        tag: str,
        children: list[HTMLNode],
        props: Optional[dict[str, str]] = None,
    ):
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):
        if (self.tag is None) or (self.tag == ""):
            raise ValueError("Parents nodes must have tags")
        if (self.children is None) or (self.children == []):
            raise ValueError("Parents Nodes must have children nodes")

        opening_tag: str = f"<{self.tag}{self.props_to_html()}>"
        closing_tag: str = f"</{self.tag}>"

        body: str = ""
        for child in self.children:
            body += child.to_html()
        return opening_tag + body + closing_tag


def text_node_to_html_node(text_node: TextNode) -> HTMLNode:
    if text_node is None:
        raise ValueError("Text Node was None")
    match (text_node.text_type):
        case (TextType.NORMAL_TEXT):
            return LeafNode(value=text_node.text)
        case (TextType.BOLD_TEXT):
            return LeafNode(tag=tags.BOLD, value=text_node.text)
        case (TextType.ITALIC_TEXT):
            return LeafNode(tag=tags.MOOD, value=text_node.text)
        case (TextType.CODE_TEXT):
            return LeafNode(tag=tags.CODE, value=text_node.text)
        case (TextType.LINK_TEXT):
            url_as_prop: dict = {"href": text_node.url}
            return LeafNode(
                tag=tags.LINK, value=text_node.text, props=url_as_prop
            )
        case (TextType.IMAGE_TEXT):
            alt_text_and_link_as_props: dict = {
                "href": text_node.url,
                "alt": text_node.text,
            }
            return LeafNode(tag=tags.IMAGE, props=alt_text_and_link_as_props)
        case _:
            raise ValueError("Unexpected TextType")
