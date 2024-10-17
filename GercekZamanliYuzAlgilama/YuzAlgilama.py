import cv2

#Haar Cascade dosyasını yükle
yuz_tespiti = cv2.CascadeClassifier("haarcascade_frontalcatface.xml")


cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Görüntüyü griye çevir
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Yüzleri tespit et
    faces = yuz_tespiti.detectMultiScale(gray, 1.1, 4)

    # Yüzleri dijdörtgen içinde göster
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)


    cv2.imshow("Gercek Zamanli Yuz Algilama", frame)

    # 'd' tuşuna basıldığında pencereyi kapat.
    if cv2.waitKey(1) & 0xFF == ord('d'):
        break

#
cap.release()
cv2.destroyAllWindows()
