# 🚁 Isparta Acil Durum Drone Rota Optimizasyonu (ACO)

Bu proje, **Karınca Kolonisi Algoritması (Ant Colony Optimization - ACO)** kullanılarak  
**Isparta merkezde bulunan acil durum toplanma alanları arasında en kısa drone rotasını** belirlemeyi amaçlamaktadır.

Mesafe hesaplamaları **Google Maps API** üzerinden alınan gerçek yol mesafeleri ile yapılmış,  
elde edilen en iyi rota **kuş uçuşu (drone senaryosu)** olacak şekilde harita üzerinde görselleştirilmiştir.

Proje, **Streamlit tabanlı etkileşimli bir web arayüzü** ile sunulmuştur.

---

## 🎯 Amaç Fonksiyonu

Bu projede amaç fonksiyonu, drone’un tüm acil toplanma alanlarını **birer kez ziyaret ederek**  
başlangıç noktasına geri döndüğü turun **toplam mesafesini minimize etmektir**.

Matematiksel olarak amaç fonksiyonu:

> **Toplam Rota Mesafesini Minimize Etmek**

ACO algoritması, iterasyonlar boyunca bu değeri azaltacak şekilde feromon güncellemeleri yapar.

---

## ⚙️ ACO Parametreleri

Kullanıcı arayüzü üzerinden aşağıdaki parametreler dinamik olarak ayarlanabilmektedir:

- **Karınca Sayısı**
- **İterasyon Sayısı**
- **Alpha (α):** Feromon bilgisinin etkisi
- **Beta (β):** Sezgisel bilginin (mesafe) etkisi
- **Buharlaşma Oranı (ρ):** Feromonların zamanla azalmasını kontrol eder

Bu sayede algoritmanın davranışı kullanıcı tarafından gözlemlenebilir.

---

## 🗺️ Kullanılan Teknolojiler

- **Python 3.10+**
- **Streamlit**
- **Google Maps API**
- **Folium (Harita görselleştirme)**
- **Matplotlib**
- **NumPy**
- **Pandas**

---

## 📁 Proje Klasör Yapısı

```text
aco_isparta_route/
│
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── data/
│   └── coordinates.py          # Isparta acil toplanma alanı koordinatları
│
├── core/
│   ├── ant_algorithm.py        # ACO algoritması
│   ├── matrix_utils.py         # Google Maps mesafe matrisi
│   └── visual/
│       ├── plotting.py         # Yakınsama grafiği
│       └── map_plotting.py     # Harita üzerinde rota çizimi
│
└── .streamlit/
    └── secrets.toml            # Google Maps API anahtarı (gizli)



✔ Proje Nasıl Çalıştırılır?
## 🚀 Projenin Çalıştırılması

Aşağıdaki adımları izleyerek projeyi lokalinizde çalıştırabilirsiniz:

1️⃣ Gerekli kütüphaneleri yükleyin:

pip install -r requirements.txt

2️⃣ Projeyi başlatın:

streamlit run main.py

3️⃣ Tarayıcı otomatik açılmazsa şu adrese gidin:
http://localhost:8501
## 📊 Çıktı Örnekleri

Uygulama aşağıdaki çıktıları üretmektedir:

En iyi rota (durak isimleriyle)

Toplam rota mesafesi

İyileşme oranı

ACO yakınsama grafiği

Harita üzerinde kuş uçuşu drone rotası

Detaylı rota tablosu

(Ekran görüntüleri aşağıda verilmiştir.)
<img width="1919" height="968" alt="image" src="https://github.com/user-attachments/assets/bdb0299d-8a55-4c47-813a-7418f1351b4a" />
<img width="1919" height="774" alt="image" src="https://github.com/user-attachments/assets/d28eef6a-1db4-41c5-9275-ac2020d7abd3" />
<img width="1474" height="580" alt="image" src="https://github.com/user-attachments/assets/57502b43-6853-43ba-97fe-d3da4b1a20cf" />

🔐 Gizlilik ve Güvenlik

Google Maps API anahtarı .streamlit/secrets.toml dosyasında tutulmaktadır
ve .gitignore ile GitHub’a yüklenmemektedir.

Her kullanıcı kendi API anahtarını kullanmalıdır.




👤 Öğrenci Bilgileri

Ad: Rabia
Soyad: Çolak
Öğrenci No: 2212721008
GitHub Repo Linki: https://github.com/rabiicolak/aco_isparta_route






