import unittest
from markdown_extractor import extract_markdown_images, extract_markdown_links

class TestMarkdownExtractor(unittest.TestCase):
    def test_extract_markdown_images(self):
        text_with_images = "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and ![another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)"
        expected_result = [
            ("image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
            ("another", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png")
        ]
        self.assertEqual(extract_markdown_images(text_with_images), expected_result)

    def test_extract_markdown_links(self):
        text_with_links = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
        expected_result = [
            ("link", "https://www.example.com"),
            ("another", "https://www.example.com/another")
        ]
        self.assertEqual(extract_markdown_links(text_with_links), expected_result)

    def test_empty_input(self):
        # Test with empty input text
        self.assertEqual(extract_markdown_images(""), [])
        self.assertEqual(extract_markdown_links(""), [])

    def test_no_matches(self):
        # Test with text containing no markdown images or links
        text = "This is regular text without any markdown formatting."
        self.assertEqual(extract_markdown_images(text), [])
        self.assertEqual(extract_markdown_links(text), [])

if __name__ == "__main__":
    unittest.main()
