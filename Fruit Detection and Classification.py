import cv2

################ IMAGE ###############################
banana_cascade = 'banana.xml'
img = cv2.imread('Screenshot_1.png')
b_cascade = cv2.CascadeClassifier(banana_cascade)
######################################################

################ CAMERA ##############################
#banana_cascade = 'banana.xml'
#cap = cv2.VideoCapture(0)
#b_cascade = cv2.CascadeClassifier(banana_cascade)
#path = 'Images_Cascade/Orange/classifier/cascade.xml'
#cascade = cv2.CascadeClassifier(path)
######################################################

while True:

############# IMAGE ##################################
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    banana = b_cascade.detectMultiScale(gray, 3, 3)
######################################################

############# VIDEO ##################################
    #ret, img = cap.read()
    #gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #banana = b_cascade.detectMultiScale(gray, 4, 5)
    #apple  = cascade.detectMultiScale(gray, 1, 2)
######################################################
    i = 0

    for (x, y, w, h) in banana:
        rectangle = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

        area = (h*w)/1000

        if round(area) >= 100:
            cv2.putText(img, 'Grade A', (x, y), 2, 1, (0, 255, 0), 2)

        elif 50 <= round(area) <= 99:
            cv2.putText(img, 'Grade B', (x, y), 2, 1, (0, 255, 0), 2)

        elif 30 <= round(area) <= 49:
            cv2.putText(img, 'Grade C', (x, y), 2, 1, (0, 255, 0), 2)

        elif round(area) <= 29:
            cv2.putText(img, 'Grade D', (x, y), 2, 1, (0, 255, 0), 2)

        i = i + 1
        cv2.putText(img, 'banana : ' + str(i), (x - 20, y - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)


    cv2.imshow('fruits', img)
    k = cv2.waitKey(30) & 0xff
    if k == 1:
        break

cap.release()
cap.destroyallWindows()
