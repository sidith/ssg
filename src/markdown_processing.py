from textnode import TextNode, TextType
import re


def split_nodes_delimiter_ideal(
    old_nodes: list[TextNode], delimiter: str, text_type: TextType
) -> list[TextNode]:
    """
    Splits text nodes by a given delimiter while treating text between
    delimiters as a specific text type.

    This function assumes no nested delimiters exist and riases an ecpetion for unpaired delimiters.

    Args:
        old_nodes (list[TextNode]): A list of TextNode objects to be split.
        delimiter (str): The delimiter used to partition the text.
        text_type (TextType): The type of text to apply to the content between paired delimiters.

    Returns:
        list[TextNode]: A new list of TextNode objects after splitting.
    """
    if not old_nodes or not delimiter or text_type is None:
        raise ValueError("Arguments cannot be None or Empty")

    if all(delimiter not in node.text for node in old_nodes):
        return old_nodes

    output_list = []
    for node in old_nodes:
        if node.text_type is not TextType.NORMAL_TEXT:
            output_list.append(node)
            continue

        if delimiter not in node.text:
            output_list.append(node)

        parts: list[str] = node.text.split(delimiter, 2)
        if len(parts) == 3:
            pretext, inflected_text, posttext = parts
            output_list.append(TextNode(pretext, TextType.NORMAL_TEXT))
            output_list.append(TextNode(inflected_text, text_type))
            output_list.append(TextNode(posttext, TextType.NORMAL_TEXT))
        else:
            raise ValueError("Cannot have lone delimiter")
    return output_list


def extract_markdown_images(text: str) -> list[tuple[str, str]]:
    pattern: str = r'!\[([^\[\]]{1,})\]\(([^\(\)]{1,})\)'
    image_markdown_links: list[tuple[str, str]] = re.findall(pattern, text)
    return image_markdown_links


def extract_markdown_links(text: str) -> list[tuple[str, str]]:
    pattern: str = r'(?<!!)\[([^\[\]]{1,})\]\(([^\(\)]{1,})\)'
    markdown_links: list[tuple[str, str]] = re.findall(pattern, text)
    return markdown_links


def main():
    test = """
This is an image test with multiple links:
![rick roll](https://i.imgur.com/aKaOqIh.gif)
Here is another image of a [cute cat website](https://cats.com):
![cute cat](https://example.com/cat.jpg)
And here's a dog from [this kennel](https://dogs.com):
![happy dog](https://example.com/dog.png)
Sometimes the description might have extra info like this:
![mountain view (sunset)](https://example.com/mountain.jpg)
Check out this [space website](https://nasa.gov) for more:
![space](https://example.com/space.jpg)
![space[Iam using brakets as a bad person]](https://example.com/space.jpg)
Here's a [link with (parentheses)](https://example.com/data)
And a [link with [brackets]](https://example.com/code)
"""
    print(extract_markdown_images(test))
    print(extract_markdown_links(test))


if __name__ == '__main__':
    main()
