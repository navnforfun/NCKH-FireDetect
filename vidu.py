# import cv2
# import time
# import urllib.request

# # Open the video stream
# stream = urllib.request.urlopen('http://192.168.0.103')

# # Create a VideoCapture object
# cap = cv2.VideoCapture(stream)

# # Check if the video stream is open
# if not cap.isOpened():
#     print('Failed to open video stream')
#     exit(1)

# # Read frames from the video stream
# while True:
#     # Capture frame-by-frame
#     ret, frame = cap.read()

#     # Check if the frame is read correctly
#     if not ret:
#         print('No more frames to read')
#         break

#     # Display the resulting frame
#     cv2.imshow('Video', frame)

#     # Wait for a key press
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# # Release the video stream and all windows
# cap.release()
# cv2.destroyAllWindows()


# importing pafy
import pafy 

# url of video 
url = "http://192.168.0.103"

# getting video
video = pafy.new(url) 

# getting all the available streams
streams = video.allstreams

# selecting one stream
stream = streams[1]

# getting url of stream
value = stream.url

# printing the value
print("URL : " + str(value))
