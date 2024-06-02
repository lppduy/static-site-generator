import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_empty_props(self):
        node = HTMLNode(tag='div', props={})
        self.assertEqual(node.props_to_html(), "")

    def test_props_to_html_single_prop(self):
        node = HTMLNode(tag='a', props={"href": "https://www.example.com"})
        self.assertEqual(node.props_to_html(), ' href="https://www.example.com"')

    def test_props_to_html_multiple_props(self):
        node = HTMLNode(tag='img', props={"src": "image.png", "alt": "An image"})
        self.assertEqual(node.props_to_html(), ' src="image.png" alt="An image"')

    def test_props_to_html_with_none_props(self):
        node = HTMLNode(tag='p')
        self.assertEqual(node.props_to_html(), "")

if __name__ == "__main__":
    unittest.main()
