# File: test_leafnode.py

import unittest
from htmlnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_node_without_value_raises_error(self):
        with self.assertRaises(ValueError):
            LeafNode("p")

    def test_leaf_node_without_tag(self):
        node = LeafNode(value="Raw text")
        self.assertEqual(node.to_html(), "Raw text")

    def test_leaf_node_with_tag_and_value(self):
        node = LeafNode("p", "This is a paragraph.")
        self.assertEqual(node.to_html(), "<p>This is a paragraph.</p>")

    def test_leaf_node_with_tag_value_and_props(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_repr(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        expected_repr = "LeafNode(tag='a', value='Click me!', props={'href': 'https://www.google.com'})"
        self.assertEqual(repr(node), expected_repr)

if __name__ == "__main__":
    unittest.main()
