import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode, text_node_to_html_node
from textnode import TextNode, TextType
import tags


class TestHTMLNode(unittest.TestCase):
    def setUp(self) -> None:
        self.props: dict[str, str] = {
            "href": "https://www.google.com",
            "target": "_blank",
        }
        self.node: HTMLNode = HTMLNode(props=self.props)

    def test_to_html_raises_not_implemented_exception(self) -> None:
        """Test that calling to_html on base HTMLNode raises NotImplementedError."""
        with self.assertRaises(NotImplementedError):
            self.node.to_html()

    def test_props_to_html(self) -> None:
        """Test if properties are converted to HTML format correctly."""
        expected_html: str = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(expected_html, self.node.props_to_html())

    def test_repr(self) -> None:
        """Test the __repr__ method for correct formatting."""
        node_repr: str = (
            "HTMLNode(tag = 'p', value = 'This is the Value', "
            "props = {'href': 'https://www.google.com', 'target': '_blank'})"
        )
        self.node.tag = tags.PARAGRAPH
        self.node.value = "This is the Value"
        self.assertEqual(node_repr, repr(self.node))


class TestLeafNode(unittest.TestCase):
    def setUp(self) -> None:
        self.empty_value_node: LeafNode = LeafNode(tag=tags.PARAGRAPH, value="")
        self.no_value_node: LeafNode = LeafNode()
        self.basic_tag_node: LeafNode = LeafNode(
            tag=tags.BOLD, value="bolded text"
        )
        self.node_with_props: LeafNode = LeafNode(
            tag=tags.LINK,
            value="Click Me",
            props={"href": "https://www.google.com"},
        )

    def test_to_html_raises_value_error_for_empty_value(self) -> None:
        """Test to_html raises ValueError if value is empty."""
        with self.assertRaises(ValueError):
            self.empty_value_node.to_html()

    def test_to_html_basic_tag(self) -> None:
        """Ensure basic tags are converted to HTML properly."""
        expected_html: str = "<b>bolded text</b>"
        self.assertEqual(expected_html, self.basic_tag_node.to_html())

    def test_to_html_with_props(self) -> None:
        """Check that HTML with attributes is generated correctly."""
        expected_html: str = '<a href="https://www.google.com">Click Me</a>'
        self.assertEqual(expected_html, self.node_with_props.to_html())


class TestParentNode(unittest.TestCase):
    def setUp(self) -> None:
        self.nodes: list[LeafNode] = [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "Italic text"),
            LeafNode(None, "Normal text"),
        ]
        self.empty_children_node: ParentNode = ParentNode(
            tags.PARAGRAPH, [], props=None
        )
        self.node: ParentNode = ParentNode(
            tags.PARAGRAPH, self.nodes, props=None
        )

    def test_to_html_with_varied_children(self) -> None:
        """Test HTML generation with a mixture of children nodes."""
        expected_html: str = (
            "<p><b>Bold text</b>Normal text" "<i>Italic text</i>Normal text</p>"
        )
        self.assertEqual(expected_html, self.node.to_html())

    def test_to_html_raises_for_empty_children(self) -> None:
        """Ensure ValueError is raised if children are empty."""
        with self.assertRaises(ValueError):
            self.empty_children_node.to_html()

    def test_nested_children_structure(self) -> None:
        """Test nested children HTML structure is generated correctly."""
        head_node: ParentNode = ParentNode(
            tags.HEAD, [LeafNode(tags.TITLE, "This is a title.")]
        )
        body_nodes: list[ParentNode] = [
            ParentNode(tags.PARAGRAPH, self.nodes) for _ in range(2)
        ]
        html_node: ParentNode = ParentNode(tags.HTML, [head_node] + body_nodes)
        expected_html: str = (
            "<html><head><title>This is a title.</title></head>"
            "<p><b>Bold text</b>Normal text<i>Italic text</i>Normal text</p>"
            "<p><b>Bold text</b>Normal text<i>Italic text</i>Normal text</p></html>"
        )
        self.assertEqual(expected_html, html_node.to_html())


class TestTextNodeToHTMLNode(unittest.TestCase):
    def setUp(self) -> None:
        self.null_node: None = None
        self.unexpted_text_type_node = TextNode(
            text="Bad Text Type", text_type="Bad Text Type"
        )

    def test_null_node_raises_error(self):
        with self.assertRaises(ValueError):
            text_node_to_html_node(self.null_node)

    def test_unexpected_text_type_raises_error(self):
        with self.assertRaises(ValueError):
            text_node_to_html_node(self.unexpted_text_type_node)


if __name__ == "__main__":
    unittest.main()
