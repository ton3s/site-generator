import unittest
from htmlnode import HTMLNode

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
	