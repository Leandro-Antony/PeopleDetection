print("\n\n[+]Program Started\n\n")

try:
    print("\nImporting...")
    import time
    import cv2
    import os
    import urllib.request
    print("\n[+]Imported")
except:
    print("\n[-]There was a error while importing")

try:
    print("\ngetting the cascade code...")
    #write the cascade code if it doesn't exist
    body_url = "https://raw.githubusercontent.com/opencv/opencv/4.x/data/haarcascades/haarcascade_fullbody.xml"
    face_url = "https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_frontalface_default.xml"
    print("\n[+]cascade code written")
except:
    print("\n[-]There was a error while getting the cascade code")

try:
    print("\nWritting the cascade code into a file...")
    file = open("haarcascade_fullbody.xml", 'w')

    response = urllib.request.urlopen(body_url)
    data = response.read()

    # Decode the bytes using the utf-8 encoding
    xml_string = data.decode('utf-8')

    # Write the XML string to the file
    file.write(xml_string)
    file.close()

    file = open("haarcascade_frontalface_default.xml", 'w')

    response = urllib.request.urlopen(face_url)
    data = response.read()

    # Decode the bytes using the utf-8 encoding
    xml_string = data.decode('utf-8')

    # Write the XML string to the file
    file.write(xml_string)
    file.close()
    print("\n[+]Succesfully written")
except:
    print("\n[-]There was an error while writting the cascade code into a file")

try:
    print("\nLoading the cascade classifier...")
    # Load the cascade classifier
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    body_cascade = cv2.CascadeClassifier('haarcascade_fullbody.xml')
    print("\n[+]Succesfully loaded")
except:
    print("\n[-]There was an error while loading the cascade classifier")

try:
    print("\ncreating a folder if it doesn't exist...")
    # Create the "faces" folder if it doesn't exist
    if not os.path.exists("faces"):
        os.makedirs("faces")

    # Create the "bodies" folder if it doesn't exist
    if not os.path.exists("bodies"):
        os.makedirs("bodies")
    print("\n[+]Succesfuly created")
except:
    print("\n[-]There was an error while creating a folder")

try:
    second = float(input("\nPer how much second do you want to take pic? "))
    print("\n[+]Succesfully changed the second")
except:
    print("\n[-]There was an error while trying to take your input")

try:
    print("\nStarting the camera...")
    # Start the video capture
    cap = cv2.VideoCapture(0)
    print("\n[+]Succesfully started")
except:
    print("\n[-]There was an error while starting the camera")

last_saved_time = time.time()

while True:
    # Read the frame
    _, frame = cap.read()

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    # Detect body
    body = body_cascade.detectMultiScale(gray, 1.1, 4)

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        cv2.putText(frame, 'face', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)

        # Save the frame as an image file in the "faces" folder
        # only if at least 1 second has passed since the last time a face was saved
        if time.time() - last_saved_time >= second:
            #cv2.imwrite("faces/face_{}.jpg".format(len(os.listdir("faces"))), frame)
            print("\n==>Face object Saved")
            last_saved_time = time.time()

    # Draw a rectangle around the body
    for (x, y, w, h) in body:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 255), 2)
        cv2.putText(frame, 'body', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)

        # Save the frame as an image file in the "bodies" folder
        # only if at least 1 second has passed since the last time a body was saved
        if time.time() - last_saved_time >= second:
            #cv2.imwrite("bodies/body_{}.jpg".format(len(os.listdir("bodies"))), frame)
            print("\n==>Body object saved")
            last_saved_time = time.time()

    # Display the resulting frame
    cv2.imshow('SecuritySight', frame)

    # Stop the script when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

try:
    print("\nDeleting the haar. files...")
    os.remove("haarcascade_frontalface_default.xml")
    os.remove("haarcascade_fullbody.xml")
    print("\n[+]Succesfully removed")
except:
    print("\n[-]There was an error while removing the haar. files")

try:
    print("\nClosing app...")
    # Release the video capture
    cap.release()

    # Destroy all the windows
    cv2.destroyAllWindows()
    print("\n[+]App closed\n")
except:
    print("\n[-]There was an error while closing the app\n")