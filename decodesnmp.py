#!/usr/bin/env python3
import sys
import argparse

# Constants -------------------------------------------------------------------
PROG_DESC = """Decode the raw hex-encoded UDP payload of an SNMP packet and either print the
constituent fields to console or write to a JSON file"""


# Main ------------------------------------------------------------------------
def main():
    parser = argparse.ArgumentParser( description=PROG_DESC )

    parser.add_argument('-f', '--file',
                        help='the input file with the hex-encoded UDP payload (mutually exclusively to -d / --direct-input)')

    parser.add_argument('-d', '--direct-input',
                        help='the hex-encoded UDP payload as a command-line arg (mutually exclusive to -f / --file)')

    parser.add_argument('-o', '--output-file',
                        help='Output to specified file instead of stdout')

    # TODO: Add arguments for community string for SNMPv2c and engine ID, auth, and priv parameters for SNMPv3, to allow for more detailed decoding

    args = parser.parse_args()

    # CLI arg validation...
    if not args.file and not args.direct_input:
        parser.error('Missing argument. You need at least -f/--file OR -d/--direct-input to be present (but not both).')

    if args.file and args.direct_input:
        parser.error("Mutually exclusive argument clash. You can't have both -f/--file AND -d/--direct-input at the same time.")

    if args.output_file:
        print('Warning: -o/--output-file not yet implemented')

    # If file, read file into string. Otherwise, copy direct input into string.
    pld_str = ""
    if args.direct_input:
        pld_str = args.direct_input
    else
        # TODO

    # Convert ASCII string into bytes array
    # TODO

    # Check version
    # TODO

    # Call decode based on version
    # TODO

    # Print out decoding or output to args.output_file
    # TODO

if __name__ == "__main__":
    main()
