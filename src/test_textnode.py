import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node: TextNode = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2: TextNode = TextNode("This is a text node", TextType.BOLD_TEXT)
        self.assertEqual(node, node2)

    def test_eq_url(self):
        node: TextNode = TextNode(
            "This is a text node", TextType.BOLD_TEXT, url="www.test.com"
        )
        node2: TextNode = TextNode(
            "This is a text node", TextType.BOLD_TEXT, url="www.test.com"
        )
        self.assertEqual(node, node2)

    def test_something(self):
        node: TextNode = TextNode("This is a string", TextType.ITALIC_TEXT)
        self.assertEqual(node.text, "This is a string")

    def test_ineq_text_type(self):
        node: TextNode = TextNode("This is a string", TextType.ITALIC_TEXT)
        node2: TextNode = TextNode("This is a string", TextType.BOLD_TEXT)

        self.assertNotEqual(node, node2)

    def test_ineq_text_url(self):
        node: TextNode = TextNode("This is a string", TextType.ITALIC_TEXT)
        node2: TextNode = TextNode(
            "This is a string", TextType.ITALIC_TEXT, url="www.test.com"
        )

        self.assertNotEqual(node, node2)

    def test_ineq_text(self):
        node: TextNode = TextNode("This is a string", TextType.ITALIC_TEXT)
        node2: TextNode = TextNode("This is also string", TextType.ITALIC_TEXT)

        self.assertNotEqual(node, node2)

    def test_repr(self):
        no_url_node: TextNode = TextNode(
            "This is a string", TextType.NORMAL_TEXT
        )
        no_url_node_repr = "TextNode('This is a string', 'normal')"

        self.assertEqual(no_url_node.__repr__(), no_url_node_repr)

        url_node: TextNode = TextNode(
            "This is a string", TextType.BOLD_TEXT, "www.google.com"
        )
        url_node_repr = "TextNode('This is a string', 'bold', 'www.google.com')"

        self.assertEqual(url_node.__repr__(), url_node_repr)


if __name__ == "__main__":
    unittest.main()
