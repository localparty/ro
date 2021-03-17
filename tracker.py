import os
import functools 
from datetime import datetime, timezone

#	comma-separated domain & timestamp list entries– check!
unresponsive_list = [
	'www.ro.com,1615960018.251915', 
	'www.yes.com,1615960018.251915',
]

def show_universe():
	for i, val in enumerate(unresponsive_list):
		print (i, "– ",val)

def track(domain):
	index_found = -1

	def match(item):
		item_parts = item.split(',')
		item_domain = item_parts[0]
		if item_domain == domain:
			return True
		else:
			return False

	for index, item in enumerate(unresponsive_list):
		if match(item):
			index_found = index

	if index_found >= 0:
		print ('found at– ', index_found)
	else:
		dt = datetime.now() 
		utc_time = dt.replace(tzinfo = timezone.utc) 
		utc_timestamp = utc_time.timestamp() 
		unresponsive_list.insert(0, f'{domain}={utc_timestamp}')
		show_universe()


# 	everything is unresponsive today, so be it!
def responsive(domain):
	return False

#	track if unresponsive
def test(domain):
	_responsive = responsive(domain)
	if _responsive == False:
		track(domain)

#	at the beginning how does the universe look? lets find out!
show_universe()

#	now let's see if a new domain is responsive, who knows!
test('www.maybe.com')

#	now let's see if a domain is still unresponsive, who knows!
test('www.ro.com')

#	the universe has ended, how does it look like?
show_universe()