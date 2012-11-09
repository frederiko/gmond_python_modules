#!/usr/bin/python

# based on 'Dive into Python' BaseHTMLProcessor.py

from sgmllib import SGMLParser

class BaseHTMLProcessor(SGMLParser):
	def reset(self):
		SGMLParser.reset(self)

  # 	def unknown_starttag(self, tag, attrs):
  #		pass

  # 	def unknown_endtag(self, tag):
#		pass	
	
	def handle_data(self, text):
		self.pieces.append(text)
		