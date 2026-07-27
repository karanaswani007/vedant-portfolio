import cv2
import cvzone
from cvzone.HandTrackingModule import HandDetector
import time
import serial

cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.8, maxHands=2)
#ser = serial.Serial("com3", 9600)

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)

    hands, img = detector.findHands(img)

    cvzone.putTextRect(
        img, "Bulb 1 OFF", (15, 100),
        scale=2, thickness=2,
        colorT=(255, 255, 255),
        colorR=(0, 0, 255),
        font=1,
        offset=30,
        border=None,
        colorB=(0, 255, 0)
    )

    cvzone.putTextRect(
        img, "Bulb 2 OFF", (140, 100),
        scale=2, thickness=2,
        colorT=(255, 255, 255),
        colorR=(0, 255, 0),
        font=1,
        offset=10,
        border=None,
        colorB=(0, 255, 0)
    )

    cvzone.putTextRect(
        img, "FAN ON", (325, 100),
        scale=2, thickness=2,
        colorT=(255, 255, 255),
        colorR=(255, 0, 0),
        font=1,
        offset=10,
        border=None,
        colorB=(0, 255, 0)
    )

    if hands:
        hand = hands[0]
        lmList = hand['lmList']
        cor = lmList[8]

        cx = cor[0]
        cy = cor[1]

        print(cx, cy)

        cv2.circle(img, (cx, cy), 7, (0, 255, 0), cv2.FILLED)

        if cx > 5 and cx < 115 and cy > 65 and cy < 115:
            print("Touched")
            #ser.write(bytearray('a', 'ascii'))

            cvzone.putTextRect(
                img, "B1", (15, 100),
                scale=3, thickness=3,
                colorT=(0, 0, 255),
                colorR=(255, 255, 255),
                font=1,
                offset=10,
                border=None,
                colorB=(0, 255, 0)
            )

        if cx > 120 and cx < 300 and cy > 65 and cy < 115:
            print("Touched")
            #ser.write(bytearray('b', 'ascii'))

            cvzone.putTextRect(
                img, "B2", (140, 100),
                scale=3, thickness=3,
                colorT=(0, 255, 0),
                colorR=(255, 255, 255),
                font=1,
                offset=10,
                border=None,
                colorB=(0, 255, 0)
            )

        if cx > 315 and cx < 455 and cy > 65 and cy < 115:
            print("Touched")
            #ser.write(bytearray('c', 'ascii'))

            cvzone.putTextRect(
                img, "FAN", (325, 100),
                scale=3, thickness=3,
                colorT=(255, 0, 0),
                colorR=(255, 255, 255),
                font=1,
                offset=10,
                border=None,
                colorB=(0, 255, 0)
            )

    cv2.imshow("Image", img)
    cv2.waitKey(1)
