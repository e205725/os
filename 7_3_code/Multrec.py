from __future__ import print_function
import socket
import time
from contextlib import closing
def main():
  local_address   = '192.168.64.1' 
  multicast_group = '239.255.0.1' 
  port = 4000
  with closing(socket.socket(socket.AF_INET, socket.SOCK_DGRAM)) as sock:
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_IF, socket.inet_aton(local_address))

    count = 0
    while True:
      message = 'Hello world'.format(count).encode('utf-8')
      sock.sendto(message, (multicast_group, port))
      time.sleep(1.0)
  return
if __name__ == '__main__':
  main()