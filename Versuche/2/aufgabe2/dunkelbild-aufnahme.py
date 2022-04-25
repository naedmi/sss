import numpy as np
import cv2

# Tutorial
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 600)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 400)
durchlauf = 0
dunkelbilder = []

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame', gray)
    if cv2.waitKey(1) & 0xFF == ord('f'):
        cv2.imwrite("../../BilderV2/dunkel" + str(durchlauf) + ".png", gray)
        image = cv2.imread("../../BilderV2/dunkel" + str(durchlauf) + ".png")
        dunkelbilder.append(image.astype('float32'))
        durchlauf = durchlauf + 1
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    if durchlauf == 10:
        dub = np.mean(dunkelbilder, axis=0)
        break


cv2.imwrite("../../BilderV2/dunkelbild.png", dub.astype('uint8'))
dub = (dub / dub.max()) * 255
cv2.imwrite("../../BilderV2/dunkelbild_HOCHKONTRAST.png", dub.astype('uint8'))
cap.release()
cv2.destroyAllWindows()