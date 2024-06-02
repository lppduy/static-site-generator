from textnode import TextNode
from htmlnode import HTMLNode, LeafNode, ParentNode
from text_to_html import text_node_to_html_node

def main():
  # text_node = TextNode("Hello", "bold", "https://www.google.com")
  # print(text_node)
  # html_node = HTMLNode("p", "This is a paragraph.", {"class": "paragraph"})
  # print(html_node)
  # leaf_node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
  # print(leaf_node)
  # print(leaf_node.to_html())
  # parent_node = ParentNode(
  #   "p",
  #   [
  #       LeafNode("b", "Bold text"),
  #       LeafNode(None, "Normal text"),
  #       LeafNode("i", "italic text"),
  #       LeafNode(None, "Normal text"),
  #   ],
  # )
  # print(parent_node.to_html())

  text_node = TextNode(text="Click here", text_type="link", url="https://www.example.com")
  html_node = text_node_to_html_node(text_node)
  print(html_node.to_html())


main()