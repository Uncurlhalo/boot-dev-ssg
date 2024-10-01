"""
A program to convert Markdown files into static HTML
"""

from textnode import TextNode


def main():
    """
    main function loop
    """
    my_text_node = TextNode("This is a text node", "bold", "http://www.boot.dev")
    print(my_text_node)


main()
