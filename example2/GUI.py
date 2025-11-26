from dora import Node
import pyarrow as pa
import numpy as np
import cv2

def main():
    #Create a new node
    node = Node("subscriber")

    shape = None
    frame = None

    #The node acts as a generator for events
    for event in node:
        
        if event["type"] == "INPUT":
            #There's three events to care about. New images, their shape, and detected faces
            #Ideally we'd put in some extra effort to make sure the detected faces are being plotted on the right image
            
            if event["id"] == "imageshape":
                shape = np.array(event["value"])
                
            if event["id"] == "image":
                frame = np.array(event["value"], dtype=np.uint8).reshape(shape)

            if event["id"] == "face":
                x,y,w,h = np.array(event["value"])
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        #If a frame exists, display it
        if type(frame) != type(None):
            cv2.imshow("Test", frame)
            cv2.waitKey(1)

        elif event["type"] == "STOP":
            cv2.destroyAllWindows()
            break

if __name__ == "__main__":
    main()

