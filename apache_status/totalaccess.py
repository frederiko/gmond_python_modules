#!/usr/bin/python

import sys, os, urllib2
from ApacheServerStatusHTMLParser import ApacheServerStatusHTMLParser	
#import pdb  

descriptors = list()
statusUrl = None

def totalAccessMetric(s, text):
	# string will come in the format
	# ex:'Total accesses: 63 - Total Traffic: 34 kB'
	for i in text:
	 	if s in i:
		   return int(i.split()[2]) # return 63 for example	
		
def totalAccess(name):
   '''Return a metric value.'''
   global statusUrl
   srcStr = "Total accesses" # string from the src html
   try: 
   		sock = urllib2.urlopen(statusUrl)
   except urllib2.URLError as e:
		print "Error opening %s: %s" % (statusUrl, e.strerror)
   		sys.exit(1)

   htmlSource = sock.read()
   
   sock.close()
   parser = ApacheServerStatusHTMLParser()
   parser.feed(htmlSource)
   parser.close()
   return totalAccessMetric(srcStr, parser.output())

def metric_init(params):
	'''Initialize all necessary initialization here.'''
	global descriptors
	global statusUrl
	statusUrl = params['url']
	
	d1 = {'name': 'Total_Access',
	     'call_back': totalAccess,
		 'time_max': 90,
		 'value_type': 'uint',
		 'units': 'Req',
		 'slope': 'both',
		 'format': '%u',
		 'description':'Returns the number of total access of this Apache server instance',
		 'groups': 'devel'}
	descriptors = [d1]
	return descriptors

def metric_cleanup():
	'''Clean up the metric module'''
	pass

# debugging and unit testing
if __name__ == '__main__':
	#global statusUrl
	params_ = { "url": 'http://lbre-db01.stanford.edu/server-status' }
	ret = metric_init(params_)
	for d in ret:
		v = d['call_back'](d['name'])
		print 'value for %s is %u' % (d['name'], v)
