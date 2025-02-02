import cv2

# Initialize video capture
cap = cv2.VideoCapture(0)

# Define the codec and create a VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # Convert frame to YCbCr color space
    ycbcr = cv2.cvtColor(frame, cv2.COLOR_BGR2YCrCb)
    
    # Write the frame
    out.write(ycbcr)
    
    # Display the frame
    cv2.imshow('Video', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
