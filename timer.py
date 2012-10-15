'''
A self-rolled timer function
'''

import time

def timer(function):
	start = time.time()
	function()
	print "Function " + function.__name__ + " finished in " + str(time.time() - start) + " seconds"
