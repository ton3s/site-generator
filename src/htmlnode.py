class HTMLNode:
	def __init__(self, tag = None, value = None, children = None, props = None):
		self.tag = tag
		self.value = value
		self.children = children
		self.props = props

	def to_html(self):
		raise NotImplementedError("to_html not implemented")
	
	def props_to_html(self):
		if self.props is None:
			return ""
		props_html = ""
		for prop in self.props:
			props_html += f' {prop}="{self.props[prop]}"'
		return props_html

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
		return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
	
	def __repr__(self):
		return f"LeafNode({self.tag}, {self.value}, {self.props})"
	
class ParentNode(HTMLNode):
	def __init__(self, tag, children, props = None):
		super().__init__(tag, children = children, props = props)
	
	def to_html(self):
		if self.tag is None:
			raise ValueError("Tag cannot be None for a parent node")
		if self.children is None:
			raise ValueError("Children cannot be None for a parent node")
		children_html = ""
		for child in self.children:
			children_html += child.to_html()
		final_html = f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"
		return final_html
	
	def __repr__(self):
		return f"ParentNode({self.tag}, {self.children}, {self.props})"