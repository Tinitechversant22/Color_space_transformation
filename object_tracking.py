'''Convert RGB images to HSV to track colored objects by their hue, saturation, and value components in real-time.'''

import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Define the range of the color to track
    lower_color = np.array([30, 100, 100])
    upper_color = np.array([60, 255, 255])
    
    # Threshold the HSV image to get the color
    mask = cv2.inRange(hsv, lower_color, upper_color)
    
    # Bitwise-AND mask and original image
    result = cv2.bitwise_and(frame, frame, mask=mask)
    
    cv2.imshow('Tracking', result)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
