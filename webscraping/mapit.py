#mapit.py - tool to search physical addresses
# usage -- python mapit.py 66600 Williams Road Richmond

#    Output: should take us to the address in GMaps

import webbrowser
import sys

# TODO: read the arguments from the command line
address = " ".join(sys.argv[1:])
print(address)
# join(list) -> string

# TODO: open the browser at a GMaps page with the arguments
prefix = "https://google.com/maps/place/"
webbrowser.open(prefix+address)

# TODO: add feature to grab address from clipboard
