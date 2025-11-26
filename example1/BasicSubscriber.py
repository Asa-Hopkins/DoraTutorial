from dora import Node
import pyarrow as pa

def main():
    #Create a new node
    node = Node("subscriber")

    #The node acts as a generator for events
    for event in node:
        
        if event["type"] == "INPUT":
            #Listen for events on the "counter" topic
            if event["id"] == "counter":
                arr = event["value"]
                print(arr[0])

        elif event["type"] == "STOP":
            break

if __name__ == "__main__":
    main()

