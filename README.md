# illumio-coding-challenge

# Testing
Initially, I had used the given rules in the assignment specification and tested network packages within the some of the given ranges. To ensure that my solution was viable for input files with a large amount of entries, I created the script generate_csv.py, randomizing the values for 500000 entries. These entries were written to the file input.csv. For testing, I used the unittest library in python, and selected a few values to test. I ran into a few issues with the unit testing due to some errors with using the library. Also, for some reason, the file in which I wrote the unit tests were deleted. I suspect it might have been some issues with merging that I had when pushing to this repository.

# Design
I mainly had the idea of dividing each component of the rule into separate classes, handling the cases when the port and IP Address were ranges rather than single values. Verification of port and IP Address were done in their respective classes, which made verification of the rule as simple as calling the functions.

# Optimization
My first thought when solving this problem was to organize the rules into a trie-like data structure with the "alphabet": 
{directions, protocols, digits} where directions = {"inbound", "outbound"}, protocols = {"tcp, "udp"}, and digits are in the range [0,9] inclusive. 
Retrieval of the port and IP Address would be done by digit-by-digit. However, I hadn't thought of a way to implement this efficiently in the given time and instead opted for creating a dictionary that mapped direction and protocol combinations to port and IP address combinations. Since the values in the dictionary were sets, checking if a rule exists can be done in constant time, at the cost of linearly increasing memory. However, the actual speed of the algorithm would depend on the hashing function in use.

In retrospect, to implement the more efficient trie-like data structure, I would have converted each value to to have the same number of digits (i.e. port = 8080 -> 08080, ip_address = 0.0.0.0 -> 000000000000) so that a distinction could be made when going on to the next numerical value (i.e. from port to ip_address). Values for direction and protocol could be encoded with 0 or 1. This would greatly reduce the space complexity for initialization, at the cost of accept_package having logarithmic time. Overall, this implementation would likely be far more optimal than the solution I've provided in this challenge.


# Team Preference
I would like to work in the data team at Illumio.
