#!/usr/bin/env python3

import os
import subprocess
#seed domain enumerator
#takes asn_no and returns alist of seed domains
#also makes initial folder structure 
def seed(asn_no):

	try:

		res = subprocess.Popen(["amass","intel","--asn",f"{asn_no}"],stdout=subprocess.PIPE)
		
		for domain in res.stdout:
		
			os.mkdir(domain.strip(r"\n"))
			
			print(f"[STATUS] created folder for seed domain f{domain.strip()}")

			continue
		
		print("we are in tee")

		subprocess.Popen(["tee","-a","seed_domain.txt"],stdin=res.stdout,stdout=subprocess.PIPE)
		
		return 1

	except Exception as ex:

		print(ex)

		return -1

#subdomain enumerator
#takes list of seed domains and returns a list of subdomains

def subdomain_finder():
	
	try:

		with open("./seed_domain.txt") as list_of_seeds:

			for seed_dn in list_of_seeds:
				
				res = subprocess.Popen(["amass","enum","-d",f"{seed_dn.strip()}"],stdout=subprocess.PIPE)

				for domain in res.stdout:
					
					os.mkdir(os.path.join(seed_dn,f"{domain.strip()}"))

					continue

				continue

	except Exception as ex:

		print(ex)

		return -1
	

if __name__ == '__main__':
	
	import sys
	#: write a guard statement that checks the no of arguments entered
	
	asn_no = sys.argv[1]

	seed_domains = seed(asn_no)

	if not asn_no:

		print("[STATUS] failed to do root domain enumeration")

		sys.exit(-1)

	#subdomains = subdomain_finder()

	#if not subdomains:

	#	print("[STATUS] failed to do subdomain enumeration")

	#	sys.exit(-1)

		
