#!/usr/bin/python

# Parse tags that interest Gmond and return the text
# based on Dive into Python dialect.py

#from BaseHTMLProcessor import BaseHTMLProcessor
from sgmllib import SGMLParser

class ApacheServerStatusHTMLParser(SGMLParser):
	def reset(self):
		SGMLParser.reset(self)
		self.text = []
		self.searchedTag = 0
		
	def start_dt(self, attrs):
		self.searchedTag = True
		
	def end_dt(self):
		self.searchedTag = None

	def handle_data(self, content):
		if self.searchedTag is True:
			self.text.append(content)

	def output(self):
		return self.text
