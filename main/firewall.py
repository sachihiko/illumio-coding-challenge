from attributes import Port, IPAddress, Rule
import csv
import sys


class Firewall():
    '''
    Sample CSV File
    inbound,tcp,80,192.168.1.2
    outbound,tcp,10000-20000,192.168.10.11
    inbound,udp,53,192.168.1.1-192.168.2.5
    outbound,udp,1000-2000,52.12.48.92

    Given a CSV file, this class defines the rules for a network packet
    '''

    def __init__(self, path: str):
        # takes O(n) time and O(n) space
        self.rules = {
            # each of the sets contain rules specifiying ports and ip addresses
            "inbound_tcp": set(),
            "inbound_udp": set(),
            "outbound_tcp": set(),
            "outbound_udp": set(),
        }

        with open(path) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            # row = [direction, protocol, port_range, ip_range]
            for line in csv_reader:
                direction, protocol, port, ip = line
                key = direction + '_' + protocol
                self.rules[key].add(Rule(
                    direction, protocol, port, ip))

    def accept_packet(self, direction: str, protocol: str,
                      port: int, ip_address: str) -> bool:
        # check if packet matches at least one rule
        # create the rule using the given attributes
        #
        input_rule = Rule(
            direction, protocol, str(port), ip_address)
        input_key = input_rule.direction + '_' + input_rule.protocol

        for r in self.rules[input_key]:
            if r.accepts(input_rule):
                return True
        return False
