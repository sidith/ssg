import pytest

from markdown_processing import (extract_markdown_images,
                                 extract_markdown_links,
                                 split_nodes_delimiter_ideal,
                                 split_nodes_image)
from textnode import TextNode, TextType

# Test cases for split_nodes_delimiter_ideal
SPLIT_NODES_DELIMITER_IDEAL_TEST_CASES: list[
    tuple[
        str,
        list[TextNode] | None,
        str | None,
        TextType,
        list[TextNode] | type[Exception],
    ]
] = [
    (
        "no_delimiter_in_text",
        [TextNode("Test Node", TextType.NORMAL_TEXT)],
        "*",
        TextType.BOLD_TEXT,
        [TextNode("Test Node", TextType.NORMAL_TEXT)],
    ),
    ("empty_input_list", [], "*", TextType.BOLD_TEXT, ValueError),
    ("none_input_list", None, "*", TextType.BOLD_TEXT, ValueError),
    (
        "none_delimiter",
        [TextNode("Delim* at front", TextType.NORMAL_TEXT)],
        None,
        TextType.BOLD_TEXT,
        ValueError,
    ),
]


@pytest.mark.parametrize(
    "name, test_node_list, delimiter, text_type, expected",
    SPLIT_NODES_DELIMITER_IDEAL_TEST_CASES,
)
def test_split_nodes_delimiter_ideal(
    name: str,
    test_node_list: list[TextNode] | None,
    delimiter: str | None,
    text_type: TextType,
    expected: list[TextNode] | type[Exception],
) -> None:
    """Test split_nodes_delimiter_ideal with various inputs."""
    if isinstance(expected, type):
        with pytest.raises(expected):
            split_nodes_delimiter_ideal(test_node_list, delimiter, text_type)
    else:
        assert (
            split_nodes_delimiter_ideal(test_node_list, delimiter, text_type)
            == expected
        ), f"Failed {name}"


# Test cases for extract_markdown_links
EXTRACT_MARKDOWN_LINKS_TEST_CASES: list[tuple[str, str, list[tuple[str, str]]]] = [
    (
        "basic_extraction",
        "Check out this [space website](https://nasa.gov) for more",
        [("space website", "https://nasa.gov")],
    ),
    (
        "nested_brackets_rejected",
        "Here is a link to [space[I am using brackets as a bad person]](https://example.com/space)",
        [],
    ),
    (
        "image_links_not_extracted",
        "Look at this ![image](www.image.com/image.git)",
        [],
    ),
    (
        "multiple_links",
        "This [link1](url1) and that [link2](url2)",
        [("link1", "url1"), ("link2", "url2")],
    ),
    ("empty_url", "[link]()", []),
]


@pytest.mark.parametrize(
    "name, test_markdown, expected_output", EXTRACT_MARKDOWN_LINKS_TEST_CASES
)
def test_extract_markdown_links(
    name: str, test_markdown: str, expected_output: list[tuple[str, str]]
) -> None:
    """Test extract_markdown_links with various markdown inputs."""
    assert extract_markdown_links(test_markdown) == expected_output, f"Failed {name}"


# Test cases for extract_markdown_images
EXTRACT_MARKDOWN_IMAGES_TEST_CASES: list[tuple[str, str, list[tuple[str, str]]]] = [
    (
        "basic_extraction",
        "This is an ![image](www.image.com/image.png)",
        [("image", "www.image.com/image.png")],
    ),
    (
        "nested_brackets_rejected",
        "This is ![nested [bracket]](nested.bracket.jpg)",
        [],
    ),
    ("empty_urls_rejected", "This is ![an empty url]()", []),
    (
        "multiple_images",
        "This ![image1](url1) and ![image2](url2)",
        [("image1", "url1"), ("image2", "url2")],
    ),
]


@pytest.mark.parametrize(
    "name, test_markdown, expected_output", EXTRACT_MARKDOWN_IMAGES_TEST_CASES
)
def test_extract_markdown_images(
    name: str, test_markdown: str, expected_output: list[tuple[str, str]]
) -> None:
    """Test extract_markdown_images with various markdown inputs."""
    assert extract_markdown_images(test_markdown) == expected_output, f"Failed {name}"


# Test cases for split_nodes_image
SPLIT_NODES_IMAGE_TEST_CASES: list[tuple[str, list[TextNode], list[TextNode]]] = [
    (
        "No Image Return Same Input",
        [TextNode("This has no image", TextType.NORMAL_TEXT)],
        [TextNode("This has no image", TextType.NORMAL_TEXT)],
    )
]


@pytest.mark.parametrize("name, input, expected_output", SPLIT_NODES_IMAGE_TEST_CASES)
def test_split_nodes_image(
    name: str, input: list[TextNode], expected_output: list[TextNode]
) -> None:
    """Test split_nodes_image with various inputs."""
    assert split_nodes_image(input) == expected_output, f"Failed {name}"
