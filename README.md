# Face-emotion-recognition
This code is a computer vision program that uses the OpenCV library and the DeepFace library to detect faces in a video stream and analyze the emotions of the detected faces.
The code then sets up a video capture object, 'cap', that captures the video from the default camera (camera index 0). If the default camera is not available, the code tries to use camera index 1. If neither of the cameras is available, the code raises an error message, 'Cannot Open webcam'.
