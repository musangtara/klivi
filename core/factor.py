#!/usr/bin/python3
e = "../vi"
if e:
    print()

def gen_uuid(object):
	return hash(object)

print(gen_uuid("klivi"))
