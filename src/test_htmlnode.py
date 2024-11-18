import unittest

from htmlnode import HTMLNode


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
            "href": "https://www.google.com", "target": "_blank"}

        node: HTMLNode = HTMLNode(
            tag='<p>', value="This is the Value", props=test_props)
        representaion = "HTMLNode(tag = '<p>', value = 'This is the Value', children = [], props = {'href': 'https://www.google.com', 'target': '_blank'})"

        self.assertEqual(representaion, node.__repr__())


if __name__ == "__main__":
    unittest.main()
