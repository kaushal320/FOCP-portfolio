#Write a program that takes a bunch of command-line arguments, and then prints
#out the shortest. If there is more than one of the shortest length, any will do.
#Hint: Don't overthink this. A good way to find the shortest is just to sort them. 

import sys
argument=sys.argv[1:]
if not argument:
    print("pls provide argument")
else:
    shortest_argument=min(argument, key=len)
    print(f"the shortest argument is {shortest_argument}")