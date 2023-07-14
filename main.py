#program to capture video from camera using openCV

# import the opencv library
import cv2

# define a video capture object
vid = cv2.VideoCapture(0)

while(True):   
    # Capture the video frame by frame
    ret, frame = vid.read()

    # Display the resulting frame
    cv2.imshow('Zafe Video Capture using OpenCV', frame)

    # the 'q' button is set as the quit button here we can use any desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
# After the loop release the capture object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()   