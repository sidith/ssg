from typing import Optional, List, Dict


class HTMLNode:
    def __init__(self,
                 tag: Optional[str] = None,
                 value: Optional[str] = None,
                 children: Optional[List['HTMLNode']] = None,
                 props: Optional[Dict[str, str]] = None):

        self.tag: Optional[str] = tag
        self.value: Optional[str] = value
        # Initialize children with an empty list if None is provided
        self.children: List[HTMLNode] = children if children is not None else []
        # Initialize props with an empty dictionary if None is provided
        self.props: Dict[str, str] = props if props is not None else {}

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        output_html: str = ''
        for key, value in self.props.items():
            output_html += f' {key}="{value}"'
        return output_html

    def __repr__(self):
        return f"HTMLNode(tag = '{self.tag}', value = '{self.value}', children = {self.children}, props = {self.props})"
