#!/usr/bin/python3

import ipaddress

def main():
    #ipchk='192.168.0.1'
    ipchk=input('Apply an IP address: ')

    try:

        ipaddress.ip_address(ipchk)

        if ipchk=='192.168.70.1':
            #print ('Looks like the IP address was set: '+ipchk)
            print ('Looks like the IP address of the Gateway was set: '+ipchk+' This is not recommended')
        else:
            print ('Looks like the IP address was set: '+ipchk)
        #else:
        #    print ('You did not provide input')
    except:
        print("Invalid IP address")


main()
