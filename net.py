# coding:utf-8
import sys, time, os
 
 
'''
Inter-|  Receive                        | Transmit
 face |bytes  packets errs drop fifo frame compressed multicast|bytes  packets errs drop fifo colls carrier compressed
  lo:  28169   364  0  0  0   0     0     0  28169   364  0  0  0   0    0     0
 wlan1: 7432984  6018  0  0  0   0     0     0  681381  6115  0  0  0   0    0     0
vmnet1:    0    0  0  0  0   0     0     0    0   56  0  0  0   0    0     0
vmnet8:    0    0  0  0  0   0     0     0    0   55  0  0  0   0    0     0
 eth0:    0    0  0  0  0   0     0     0    0    0  0  0  0   0    0     0
 
'''
 
_unit_=['B','KB','MB','GB','TB']
 
def get_net_data(interface):
  for line in open('/proc/net/dev', 'r'):
    if line.split(':')[0].find(interface)>=0:
      return map(int, line.split(':')[1].split())
 
def convert_bytes_to_string(b):
  cnt = 0
  while b >= 1024.0:
    b = float(b) / 1024.0
    cnt += 1
  return '%.2f%s'%(b,_unit_[cnt])
 
if __name__ == '__main__':
  interface = sys.argv[1]
  while True:
    net_data = get_net_data(interface)
    receive_data_bytes = net_data[0]
    transmit_data_bytes = net_data[8]
    os.system('clear')
    print 'Interface:%s  -> Receive Data: %s  Transmit Data: %s'%(interface, convert_bytes_to_string(receive_data_bytes), convert_bytes_to_string(transmit_data_bytes))
    time.sleep(1)
