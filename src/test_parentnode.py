import unittest
from htmlnode import LeafNode, ParentNode

class TestParentNode(unittest.TestCase):
    def test_parent_node_without_tag_raises_error(self):
        with self.assertRaises(ValueError):
            ParentNode(children=[LeafNode("b", "Bold text")])

    def test_parent_node_without_children_raises_error(self):
        with self.assertRaises(ValueError):
            ParentNode(tag="p")

    def test_parent_node_with_tag_and_children(self):
        node = ParentNode(
            tag="p",
            children=[
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "Italic text"),
            ]
        )
        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>Italic text</i></p>")

    def test_nested_parent_nodes(self):
        inner_node = ParentNode(
            tag="span",
            children=[
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "Italic text"),
            ]
        )
        outer_node = ParentNode(
            tag="div",
            children=[
                inner_node,
                LeafNode(None, "Some other text"),
            ]
        )
        self.assertEqual(outer_node.to_html(), '<div><span><b>Bold text</b>Normal text<i>Italic text</i></span>Some other text</div>')

    def test_repr(self):
        node = ParentNode(
            tag="p",
            children=[
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "Italic text"),
            ]
        )
        expected_repr = "ParentNode(tag='p', children=[LeafNode(tag='b', value='Bold text', props={}), LeafNode(tag=None, value='Normal text', props={}), LeafNode(tag='i', value='Italic text', props={})], props={})"
        self.assertEqual(repr(node), expected_repr)

if __name__ == "__main__":
    unittest.main()
