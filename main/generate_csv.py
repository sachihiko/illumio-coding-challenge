import csv
from random import randint

with open('test.csv', 'w') as csv_file:
    package_writer = csv.writer(
        csv_file, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    #package_writer.writerow(['Direction', 'Protocol', 'Port', 'IP Address'])
    for i in range(100):
        direction = 'inbound' if randint(0, 1) == 0 else 'outbound'
        protocol = 'tcp' if randint(0, 1) == 0 else 'udp'
        port = randint(1, 65535)
        a, b, c, d = randint(0, 255), randint(0, 255), \
            randint(0, 255), randint(0, 255)

        ip_address = "{}.{}.{}.{}".format(a, b, c, d)
        package_writer.writerow([direction, protocol, port, ip_address])
