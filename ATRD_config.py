#!/usr/bin/env python

def trunking():
	file = open("gsm.csv").readlines()
	for line in file:
		text  = line.strip().split(',')[0].split('.')
		print("""
[GSM{0}]
type=peer
qualify=yes
host={1}
context=from-gsm
nat=no
disallow=all
allow=ulaw
allow=alaw""".format(text[2] + text[3],line.strip().split(',')[0]))

def gsm_config():
	count=1
	prefix=340

	file = open("gsm.csv").readlines()
	for line in file:
		channel=line.split(',')[1].strip()
		text=line.split(',')[0].strip().split('.')
		print("""\
GSM_TRUNK_MOBI_{0}_{1}=SIP/GSM{2}
GSM_TRUNK_MOBI_{0}_{1}_MAX={3}
GSM_TRUNK_MOBI_{0}_{1}_TOTAL=0""".format(prefix,count,text[2] + text[3],channel))
		count+=1
	print("""\
GSM_TOTAL_TRUNK_MOBI_{0}={1}
GSM_TOTAL_CALLS_MOBI_{0}=0
""".format(prefix,count-1))

if __name__ == '__main__':
	gsm_config()
