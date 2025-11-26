from dora import Node
import pyarrow as pa
import numpy as np
import cv2

def main():
    #Create a new node
    node = Node("subscriber")
    
    shape = None
    frame = None

    face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

    #The node acts as a generator for events
    for event in node:
        
        if event["type"] == "INPUT":
            
            if event["id"] == "imageshape":
                shape = np.array(event["value"])
                
            if event["id"] == "image":
                frame = np.array(event["value"], dtype=np.uint8).reshape(shape)
                grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

                faces = face_cascade.detectMultiScale(grey, scaleFactor=1.1, minNeighbors=5, minSize=(60, 60))
                for face in faces:
                    node.send_output("face", pa.array(face))
            
        elif event["type"] == "STOP":
            break

if __name__ == "__main__":
    main()

