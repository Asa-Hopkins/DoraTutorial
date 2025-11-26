import time
from dora import Node
import cv2
import pyarrow as pa

def main():
    node = Node()
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("Cannot open camera")
        return
    t = 0
    
    while True:
        ret, frame = cap.read()
        
        #Check framerate
        #print(1/(time.time() - t))
        #t = time.time()
        
        if not ret:
            #Camera has stopped sending photos so we close
            return
        
        # check for stop event
        # Note that timing out returns an event of type "ERROR" , but we ignore them
        event = node.next(timeout=0)
        if event != None:
            if event["type"] == "STOP":
                return

        #Can either send as bytes or pa array
        arr = frame.tobytes()
        #pa.array(frame.flatten(), type=pa.uint8())

        #In either case, we also need to send the image shape
        #Make sure to send the shape first too
        node.send_output("imageshape", pa.array(frame.shape))
        node.send_output("image", arr)
        

if __name__ == "__main__":
    main()
