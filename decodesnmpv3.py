#!/usr/bin/env python3
"""
Decode a hex-encoded UDP payload of an SNMP GET request, response, or report
PDU errors (e.g., usmStats*).

Limitations:
- Assumes one variable binding in PDU
- Does not decrypt encrypted scopedPDU sections
- Only SNMPv3
"""
import sys



def main():
    sys.argv[0]

if __name__ == "__main__":
    main()
