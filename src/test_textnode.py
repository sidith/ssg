import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node: TextNode = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2: TextNode = TextNode("This is a text node", TextType.BOLD_TEXT)
        self.assertEqual(node, node2)

    def test_eq_url(self):
        node: TextNode = TextNode(
            "This is a text node", TextType.BOLD_TEXT, url='www.test.com')
        node2: TextNode = TextNode(
            "This is a text node", TextType.BOLD_TEXT, url='www.test.com')
        self.assertEqual(node, node2)

    def test_something(self):
        node: TextNode = TextNode("This is a string", TextType.ITALIC_TEXT)
        self.assertEqual(node.text, "This is a string")

    def test_ineq_text_type(self):
        node: TextNode = TextNode('This is a string', TextType.ITALIC_TEXT)
        node2: TextNode = TextNode('This is a string', TextType.BOLD_TEXT)

        self.assertNotEqual(node, node2)

    def test_ineq_text_url(self):
        node: TextNode = TextNode('This is a string', TextType.ITALIC_TEXT)
        node2: TextNode = TextNode(
            'This is a string', TextType.ITALIC_TEXT, url='www.test.com')

        self.assertNotEqual(node, node2)

    def test_ineq_text(self):
        node: TextNode = TextNode('This is a string', TextType.ITALIC_TEXT)
        node2: TextNode = TextNode('This is also string', TextType.ITALIC_TEXT)

        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()
