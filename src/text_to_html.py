from htmlnode import LeafNode

def text_node_to_html_node(text_node):
    if text_node.text_type == "text":
        return LeafNode(value=text_node.text)
    elif text_node.text_type == "bold":
        return LeafNode(tag="b", value=text_node.text)
    elif text_node.text_type == "italic":
        return LeafNode(tag="i", value=text_node.text)
    elif text_node.text_type == "code":
        return LeafNode(tag="code", value=text_node.text)
    elif text_node.text_type == "link":
        props = {"href": text_node.url}
        return LeafNode(tag="a", value=text_node.text, props=props)
    elif text_node.text_type == "image":
        props = {"src": text_node.url, "alt": text_node.text}
        return LeafNode(tag="img", value="", props=props)
    else:
        raise ValueError("Invalid TextNode type")
