
class HTMLNode:
	def __init__(self, tag = None, value = None, children = None, props = None):
		self.tag = tag
		self.value = value
		self.children = children
		self.props = props

	def to_html(self):
		raise NotImplementedError("to_html not implemented")
	
	def props_to_html(self):
		html = ""		
		for key, value in self.props.items():
			html += f" {key}=\"{value}\""
		return html
	
	def __repr__(self):
		return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
	
class LeafNode(HTMLNode):
	def __init__(self, tag, value, props = None):
		super().__init__(tag, value, children = None, props = props)
	
	def to_html(self):
		if self.value is None:
			raise ValueError("Value cannot be None for a leaf node")
		if self.tag is None:
			return self.value
		if self.props is None:
			return f"<{self.tag}>{self.value}</{self.tag}>"
		return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
	
	def __repr__(self):
		return f"LeafNode({self.tag}, {self.value}, {self.props})"