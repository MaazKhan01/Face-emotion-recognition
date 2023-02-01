# Face Emotion Recognition
This code is a computer vision program that uses the OpenCV library and the DeepFace library to detect faces in a video stream and analyze the emotions of the detected faces.

The code sets up a video capture object, 'cap', that captures the video from the default camera (camera index 0). If the default camera is not available, the code tries to use camera index 1. If neither of the cameras is available, the code raises an error message, 'Cannot Open webcam'.

The 'haarcascade' in this code is a type of object detection classifier that is used to detect faces in images or video frames. The cv2.CascadeClassifier class is a part of the OpenCV library, which is a widely used computer vision library for image and video processing. 
