import cv2
import numpy as np

canvas = np.zeros((512, 512, 3), dtype=np.uint8) + 255

#!!!!! renk kodunda ki -1 şeklin içini doldurmak içindir!!!!!

#çizgi
#cv2.line(resim, (başlangıç), (bitiş), (renk kodu), thickness=kalınlık)
cv2.line(canvas, (50, 50), (512, 512), (255, 0), thickness=5)
cv2.line(canvas, (100, 50), (200, 250), (0, 0, 255), thickness=7)

#kare
#cv2.rectangle(resim, (balangıç), (bitiş), (renk kodu), thickness=kalınlık)
cv2.rectangle(canvas, (20, 20), (50, 50), (0, 255, 0), thickness=1)
cv2.rectangle(canvas, (50, 50), (150, 150), (0, 255, 0), thickness=-1)

#çember
#cv2.circle(resim, (başlangıç), (bitiş), yarı çap, (renk kodu), thickness=-1)
cv2.circle(canvas, (250, 250), 100, (0, 0, 255), thickness=-1)

#Birden fazla çizgi için
#np.array([[[Çizgi 1], [Çizgi 2], [Çizgi 3], [Çizgi 4], ......]],np.int32)
points = np.array([[[110, 200], [330, 200], [290, 220], [100, 100]]], np.int32)
#cv2.polylines(resim, [Kordinatlar], False-True,(Renk Kodu), Kalınlık) ------ True = Şekil Kapalı Olsun ------ False = Şekil Açık Olsun (!!!Kordinatlar Yukarda Belirlilen Listedir!!!)
cv2.polylines(canvas, [points], False, (0, 0, 100), 5)

#elips
#cv2.ellipse(resim, (başlangıç), (bitiş), Yatay Eksenli Açısı, Başlangıç Açısı, Bitiş Açısı, (Renk Kodu), Kalınlık)
cv2.ellipse(canvas, (300, 300), (100, 50), 0, 0, 360, (255, 255, 9), -1)

cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()