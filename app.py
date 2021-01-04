import cv2
# set the webcam as cam variable
cam = cv2.VideoCapture(0)
# code will execute only while webcam is opened
while cam.isOpened():
    ret, frame1 = cam.read()
    ret, frame2 = cam.read()
    # get the difference between frame1 and frame2
    diff = cv2.absdiff(frame1, frame2)
    # convert the colorfull image into gray color image
    gray = cv2.cvtColor(diff, cv2.COLOR_RGB2GRAY)
    # convert the gray image to slightly blur image
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    # to get sharper and bright image we use threshhold
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    # remove unwantend image and focus on intrested things 
    dilated = cv2.dilate(thresh, None, iterations=3)
    # countours bound the things which are moving 
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for c in contours:
        # neglect the smallest moving portions
        # to be bound with countours the moving thing will greater than 5000
        if cv2.contourArea(c) < 5000:
            continue
        x, y, w, h = cv2.boundingRect(c)
        cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2)
        # terminate the opened window on clicking q keyword
    if cv2.waitKey(10) == ord('q'):
        break
    # open the webcam and display the image
    cv2.imshow('Open CV Project', frame1)