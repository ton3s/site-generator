import unittest
from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):	
	def test_props_to_html_empty(self):
		node = HTMLNode(props={})
		self.assertEqual(node.props_to_html(), "")
	
	def test_props_to_html_one_prop(self):
		node = HTMLNode(props={"class": "test"})
		self.assertEqual(node.props_to_html(), " class=\"test\"")
	
	def test_props_to_html_two_props(self):
		node = HTMLNode(props={"class": "test", "id": "test"})
		self.assertEqual(node.props_to_html(), " class=\"test\" id=\"test\"")
	
	def test_leaf_to_html_p(self):
		node = LeafNode(tag="p", value="Hello, world!")
		self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
	
	def test_leaf_to_html_p_with_props(self):
		node = LeafNode(tag="p", value="Hello, world!", props={"class": "test", "id": "test"})
		self.assertEqual(node.to_html(), "<p class=\"test\" id=\"test\">Hello, world!</p>")
	
	def test_leaf_to_html_p_with_no_tag(self):
		node = LeafNode(tag=None, value="Hello, world!")
		self.assertEqual(node.to_html(), "Hello, world!")