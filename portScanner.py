from socket import *
from threading import *
from queue import Queue
import sys

print_lock = Lock()
target = sys.argv[1]
start = sys.argv[2]
stop = sys.argv[3]

def portscan(port):
    s = socket(AF_INET, SOCK_STREAM)
    try:
      con = s.connect((target, port))
      with print_lock:
          print('port', port,'is open!')
      con.close()
    except:
        pass
    
def threader():
    while True:
        worker = q.get()
        portscan(worker)
        q.task_done()
        
q = Queue()
for x in range(75):
    t = Thread(target=threader)
    t.daemon = True
    t.start()
for worker in range(start, stop):
    q.put(worker)
print('Scanning...')
q.join()
