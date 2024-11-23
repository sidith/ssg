import unittest
from parameterized import parameterized
from markdown_processing import (
    split_nodes_delimiter_ideal as split,
    extract_markdown_links,
    extract_markdown_images)
from textnode import TextType, TextNode


class TestSplitNodesDelimiterIdeal(unittest.TestCase):
    @parameterized.expand([
        ("no_delimiter_in_text", [TextNode("Test Node", TextType.NORMAL_TEXT)],
         '*', TextType.BOLD_TEXT, [TextNode("Test Node", TextType.NORMAL_TEXT)]),
        ("empty_input_list", [], '*', TextType.BOLD_TEXT, ValueError),
        ("none_input_list", None, '*', TextType.BOLD_TEXT, ValueError),
        ("none_delimiter", [TextNode(
            "Delim* at front", TextType.NORMAL_TEXT)], None, TextType.BOLD_TEXT, ValueError),
        ("none_text_type", [TextNode("Delim* at front",
         TextType.NORMAL_TEXT)], '*', None, ValueError),
    ])
    def test_split_nodes_delimiter_ideal(self, name, test_node_list, delimiter, text_type, expected):
        """Test split_nodes_delimiter_ideal with various inputs."""
        if isinstance(expected, type) and issubclass(expected, Exception):
            with self.assertRaises(expected, msg=f"Expected {expected} for {name}"):
                split(test_node_list, delimiter, text_type)
        else:
            self.assertEqual(
                split(test_node_list, delimiter, text_type),
                expected,
                msg=f"Failed {name}"
            )


class TestExtractMarkdownLinks(unittest.TestCase):
    @parameterized.expand([
        ("basic_extraction", 'Check out this [space website](https://nasa.gov) for more', [
         ('space website', 'https://nasa.gov')]),
        ("nested_brackets_rejected",
         'Here is a link to [space[I am using brackets as a bad person]](https://example.com/space)', []),
        ("image_links_not_extracted",
         'Look at this ![image](www.image.com/image.git)', []),
        ("multiple_links", 'This [link1](url1) and that [link2](url2)', [
         ('link1', 'url1'), ('link2', 'url2')]),
        ("empty_url", '[link]()', []),
    ])
    def test_extract_markdown_links(self, name, test_markdown, expected_output):
        """Test extract_markdown_links with various markdown inputs."""
        self.assertEqual(
            extract_markdown_links(test_markdown),
            expected_output,
            msg=f"Failed {name}"
        )


class TestExtractMarkdownImages(unittest.TestCase):
    @parameterized.expand([
        ("basic_extraction", 'This is an ![image](www.image.com/image.png)', [
         ('image', 'www.image.com/image.png')]),
        ("nested_brackets_rejected",
         'This is ![nested [bracket]](nested.bracket.jpg)', []),
        ("empty_urls_rejected", 'This is ![an empty url]()', []),
        ("multiple_images", 'This ![image1](url1) and ![image2](url2)', [
         ('image1', 'url1'), ('image2', 'url2')]),
    ])
    def test_extract_markdown_images(self, name, test_markdown, expected_output):
        """Test extract_markdown_images with various markdown inputs."""
        self.assertEqual(
            extract_markdown_images(test_markdown),
            expected_output,
            msg=f"Failed {name}"
        )


if __name__ == '__main__':
    unittest.main()
