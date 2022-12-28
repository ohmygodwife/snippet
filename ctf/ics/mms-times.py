#!/usr/bin/env python

import pyshark

captures = pyshark.FileCapture("tmflag.pcapng")
confirmed_services_request = {}
confirmed_services_response = {}
for capture in captures:
    for pkt in capture:
        if pkt.layer_name == "mms":
            if hasattr(pkt, "confirmedservicerequest"):
                service = pkt.confirmedservicerequest
                if service in confirmed_services_request:
                    confirmed_services_request[service] += 1
                else:
                     confirmed_services_request[service] = 1
            if hasattr(pkt, "confirmedserviceresponse"):
                service = pkt.confirmedserviceresponse
                if service in confirmed_services_response:
                    confirmed_services_response[service] += 1
                else:
                     confirmed_services_response[service] = 1
print(confirmed_services_request)
print(confirmed_services_response)