import re

def extract_markdown_images(text):
    """
    Extracts markdown images from raw text.
    
    Args:
        text (str): The raw text containing markdown images.
    
    Returns:
        list: A list of tuples, where each tuple contains the alt text and URL of the markdown image.
    """
    pattern = r"!\[(.*?)\]\((.*?)\)"
    return re.findall(pattern, text)

def extract_markdown_links(text):
    """
    Extracts markdown links from raw text.
    
    Args:
        text (str): The raw text containing markdown links.
    
    Returns:
        list: A list of tuples, where each tuple contains the anchor text and URL of the markdown link.
    """
    pattern = r"\[(.*?)\]\((.*?)\)"
    return re.findall(pattern, text)

# # Test the functions
# text_with_images = "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and ![another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)"
# print(extract_markdown_images(text_with_images))

# text_with_links = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
# print(extract_markdown_links(text_with_links))
