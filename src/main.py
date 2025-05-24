from textnode import TextNode, TextType

def main():
	text = TextNode("This is a link", TextType.LINK, "https://www.google.com")
	print(text)
    
if __name__ == "__main__":
    main()