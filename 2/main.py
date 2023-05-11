import cv2

cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)

cap.set(11, 36)
cap.set(12, 20)
cap.set(10, 100)

print("frame width: " + str(cap.get(3)))
print("frame height: " + str(cap.get(4)))
print("--------------------------------")
print("brightness: " + str(cap.get(10)))
print("contrast: " + str(cap.get(11)))
print("saturation: " + str(cap.get(12)))
print("--------------------------------")
print("gain: " + str(cap.get(14)))
print("exposure: " + str(cap.get(15)))
print("--------------------------------")
print("white balance: " + str(cap.get(17)))

n = 0

path_grauwertkeil = r'data/grauwertkeil'
path_dunkelbild = r'data/dunkelbild'
path_weissbild = r'data/weissbild'

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame', gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        if n == 10:
            break
        else:
            cv2.imwrite(path_grauwertkeil + str(n) + '.png', gray)
            n += 1
cap.release()
cv2.destroyAllWindows()