import os
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
	dt = datetime.now() 
	utc_time = dt.replace(tzinfo = timezone.utc) 
	utc_timestamp = utc_time.timestamp() 
	unresponsive_list.insert(0, f'{domain}={utc_timestamp}')

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

#	now let's see if a domain is responsive, who knows!
test('www.maybe.com')

#	the universe has ended, how does it look like?
show_universe()