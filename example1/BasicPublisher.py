import time
from dora import Node
import pyarrow as pa

def main():
    node = Node()
    counter = 0

    while True:
        # check for stop event
        # Note that timing out returns an event of type "ERROR" , but we ignore them
        event = node.next(timeout=0)
        if event != None:
            if event["type"] == "STOP":
                return
            
        # wrap the counter in a PyArrow array
        payload = pa.array([counter])
        node.send_output("counter", payload)
        counter += 1
        time.sleep(0.1)
        

if __name__ == "__main__":
    main()
