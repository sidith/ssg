import unittest

from htmlnode import HTMLNode, LeafNode
import tags


class TestHTMLNode(unittest.TestCase):
    def test_to_html_raises_excpetion(self):
        node: HTMLNode = HTMLNode()
        self.assertRaises(NotImplementedError, node.to_html)

    def test_props_to_html(self):
        test_props: dict[str, str] = {
            "href": "https://www.google.com", "target": "_blank"}
        node: HTMLNode = HTMLNode(props=test_props)

        props_html: str = node.props_to_html()
        test_html: str = ' href="https://www.google.com" target="_blank"'

        self.assertEqual(test_html, props_html)

    def test_repr(self):
        test_props: dict[str, str] = {
            "href": "https://www.google.com",
            "target": "_blank"
        }

        node: HTMLNode = HTMLNode(
            tag=tags.PARAGRAPH,
            value="This is the Value",
            props=test_props)

        tag_repr: str = "tag = 'p'"
        value_repr: str = "value = 'This is the Value'"
        children_repr: str = "children = []"
        props_repr = "props = {'href': 'https://www.google.com', 'target': '_blank'}"

        full_repr = f"HTMLNode({tag_repr}, {value_repr}, {children_repr}, {props_repr})"

        self.assertEqual(full_repr, node.__repr__())


class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        test_node_empty_str_value: LeafNode = LeafNode(
            tag=tags.PARAGRAPH, value='')
        self.assertRaises(ValueError, test_node_empty_str_value.to_html)

        test_node_no_value: LeafNode = LeafNode()
        self.assertRaises(ValueError, test_node_no_value.to_html)

        test_node_basic_tag: LeafNode = LeafNode(
            tag=tags.BOLD, value='bolded text')
        node_3_html = "<b>bolded text</b>"
        self.assertEqual(test_node_basic_tag.to_html(), node_3_html)

        test_node_with_props: LeafNode = LeafNode(tag=tags.LINK, value='Click Me', props={
            'href': 'https://www.google.com'})
        node_4_html = '<a href="https://www.google.com">Click Me</a>'
        self.assertEqual(test_node_with_props.to_html(), node_4_html)

        test_node_plain_text: LeafNode = LeafNode(value='plain text')
        test_node_plain_text_html = 'plain text'
        self.assertEqual(test_node_plain_text.to_html(),
                         test_node_plain_text_html)


if __name__ == "__main__":
    unittest.main()
