#Nesne Algılama

"""
#Haar Cascade

Haar cascade nesne tespiti yapan bir işlemdir.
Pozitif ve Negatif resim görüntü kullanılır.
"Pozitif Görüntü": İçinde tespit edilmek istenen nesnenin bulunduğu görüntülerdir.
"Negatif Görüntü": İçinde tespit edilmek nesnenin bulunmalıdğı görüntülerdir.
Model görüntüyü küçük bölgelere böler ve her bölgeyi inceleyerek nesneyi tespit eder.

-----------------------------------------------------------------------------------------------------

Yüz Tespiti:
Pozitif Görüntüler: Yüzlerin olduğu, farklı açılardan çekilmiş fotoğraflar.
Negatif Görüntüler: Yüz içermeyen manzara, nesne veya insan fotoğrafı.

-----------------------------------------------------------------------------------------------------

XML Dosyası: Haar Cascade algoritması için kullanılan XML dosyaları, önceden eğitilmiş
Haar özelliklerini ve model parametlerini içeren dosyalardır.
https://github.com/opencv/opencv/tree/master/data/haarcascades

-----------------------------------------------------------------------------------------------------

[ÖRNEK] Yüz tespiti için şu kodu kullanabilirsin:

### Haar Cascade dosya yolu belirtildi.
yuz_tespiti = "haarcascade.frontalface_default.xml"
yuz_tespiti = cv2.CascadeClassifier(yuz_tespiti)
### Haar Cascade yüklendi.

-----------------------------------------------------------------------------------------------------

Özetle "Haar Cascade" → Nesne tespiti için kullanılan bir makine öğrenimi algoritmasıdır. Belirli
nesnelerin tespiti için "Haar Özellikleri" verilen yoğunluk değişimlerini kullanarak model oluşturur.

-----------------------------------------------------------------------------------------------------

#Hog

Görüntü işleme ve bilgisayarla görme alanında yaygın olarak kullanılan bir özellik çıkarım yöntemidir.
Özellikle nesne algılama görevlerinde, nesnelerin yapısını ve konturlarını tanımak için kullanılır

5 Aşama ile çalışır:
1. Gradyan Hesaplama → Görüntüdeki piksellerin yoğunluk değişimleri hesaplanır.
2. Hücrelere Ayırma → Görüntü küçük hücrelere bölünür (8x8) gibi.
3. Histogram Oluşturma → Her güçre için gradyan yönlerinin histogramı oluşturulur.
4. Blok Normalizasyonu → Hücre histogramları, komşu hücrelerle normalleştirilir
5. Özellik Vekötür Oluşturma → Normalleştirilmiş histogramlar birleştirilerek genel bir özellik vektörü elde edilir.

Kısaca "HOG", görüntüdeki nesnelerin kenar ve yapısını analiz etmek için kullanılan bir özellik çıkarım yöntemidir. Görüntülerde nesneleri tanımak için güçlü bir araçtır.

-----------------------------------------------------------------------------------------------------

"Haar Cascade" , "HOG" arasındaki temel fark nedir:

Farklı yaklaşımlar kullanarak nesne algılama görevlerini gerçekleştirirler.
HOG, daha karmaşık ve detaylı yapılan yakalamada daha başarılı olabilirken,
Haar Cascade hızlı ve basit tespitler için idealdir.

-----------------------------------------------------------------------------------------------------






















"""