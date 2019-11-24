'''
Classes for a firewall rule
'''

# Specifies the range of ports accepted for a rule


class Port():
    def __init__(self, port_str: str):
        if '-' in port_str:
            self.start, self.end = (int(x) for x in port_str.split('-'))
        else:
            self.start, self.end = int(port_str), int(port_str)

    def accepts_port(self, port) -> bool:
        return self.start <= port <= self.end

# Specifies the range of IP Addresses for a rule


class IPAddress():
    def __init__(self, ip_address_str: str):
        if '-' in ip_address_str:
            self.start, self.end = (str(x) for x in ip_address_str.split('-'))
            self.start = [int(s) for s in self.start.split('.')]
            self.end = [int(e) for e in self.end.split('.')]

        else:
            self.start = [int(s) for s in ip_address_str.split('.')]
            self.end = [int(e) for e in ip_address_str.split('.')]

    def accepts_ip(self, input_ip) -> bool:
        for i in range(4):
            # continue to next iteration if these digits are the same
            if self.start[i] == self.end[i]:
                continue
            if self.start[i] < input_ip.start[i] < self.end[i]:
                return True
            return False
        return True

# Specifies a rule


class Rule():
    def __init__(self, direction: str, protocol: str, port_str: str, ip_str: str):
        self.direction = direction
        self.protocol = protocol
        # range of ports allowed, inclusive
        self.port_range = Port(port_str)
        # range of ip addresses allowed, inclusive
        self.ip_range = IPAddress(ip_str)

    # checks if a network package is allowed
    # the network package comes in the form of a rule
    #
    # this function is called by Firewall, which maps directions and protocols
    # to IP Addresses

    def accepts(self, net_package):
        # input port and IP Address are single values
        port = net_package.port_range.start
        ip_address = net_package.ip_range.start

        return self.port_range.accepts_port(port) and \
            self.ip_range.accepts_ip(ip_address)
