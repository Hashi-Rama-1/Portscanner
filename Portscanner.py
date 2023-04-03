import socket
import termcolor



def scan(target,ports):
        print('\n' + "Starting scan of " + str(target)) 
        
        for port in range(1,ports):
            scan_port(target, port)



def scan_port(ipaddress, port):
    try:

        sock = socket.socket()
        sock.connect((ipaddress, port))
        print("[+]Port connected " + str(port))
        socket.close()

    except:
        

        pass


targets = input("[*]Enter IP addresses of targets to be scanned (split them by ,): ")
ports = int(input("[*]Enter number of ports to be scanned: "))


if ',' in targets:
    print(termcolor.colored(("[*]Scanning multiple targets....."),'green'))
    for ip_addr in targets.split(','):
        scan(ip_addr.strip(' '), ports)

else:
    scan(targets,ports)






