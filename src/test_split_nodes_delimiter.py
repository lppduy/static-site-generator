import unittest
from textnode import TextNode
from split_nodes_delimiter import split_nodes_delimiter

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_single_delimiter(self):
        # Test with a single delimiter "*"
        old_nodes = [TextNode("This is *italic* text", "text")]
        new_nodes = split_nodes_delimiter(old_nodes, "*", "italic")
        expected_result = [
            TextNode("This is ", "text"),
            TextNode("italic", "italic"),
            TextNode(" text", "text")
        ]
        self.assertEqual(new_nodes, expected_result)

    def test_multiple_delimiters(self):
        # Test with multiple delimiters "**" and "_"
        old_nodes = [TextNode("This is **bold** and _italic_ text", "text")]
        new_nodes = split_nodes_delimiter(old_nodes, "**", "bold")
        new_nodes = split_nodes_delimiter(new_nodes, "_", "italic")
        expected_result = [
            TextNode("This is ", "text"),
            TextNode("bold", "bold"),
            TextNode(" and ", "text"),
            TextNode("italic", "italic"),
            TextNode(" text", "text")
        ]
        self.assertEqual(new_nodes, expected_result)

    def test_no_delimiter(self):
        # Test with no delimiter
        old_nodes = [TextNode("This is regular text", "text")]
        new_nodes = split_nodes_delimiter(old_nodes, "*", "bold")
        expected_result = [
            TextNode("This is regular text", "text")
        ]
        self.assertEqual(new_nodes, expected_result)

    def test_empty_input(self):
        # Test with empty input list
        old_nodes = []
        new_nodes = split_nodes_delimiter(old_nodes, "*", "bold")
        expected_result = []
        self.assertEqual(new_nodes, expected_result)

if __name__ == "__main__":
    unittest.main()
