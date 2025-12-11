# 🚁 Isparta Acil Durum Drone Rota Optimizasyonu (ACO)

Bu proje, **Karınca Kolonisi Algoritması (Ant Colony Optimization - ACO)** kullanılarak  
**Isparta’daki acil toplanma alanları arasında en kısa drone rota planlamasını** yapar.

Streamlit tabanlı bir web arayüzü ile kullanıcı, karınca sayısı ve iterasyon sayısını ayarlayarak  
en iyi rotayı, yakınsama grafiğini ve harita üzerindeki rota çizimini görüntüleyebilir.

---

## Kullanılan Teknolojiler
- **Python 3.10+**
- **Streamlit**
- **Matplotlib**
- **NumPy**
- **Coğrafi koordinatlar ile mesafe hesaplama**

---

## 📁 Proje Klasör Yapısı
aco_isparta_route/
│ main.py
│ requirements.txt
│ README.md
│ .gitignore
│
├── data/
│ └── coordinates.py # Isparta toplanma alanı koordinatları
│
├── core/
│ ├── ant_algorithm.py # ACO algoritması
│ └── matrix_utils.py # Mesafe matrisi oluşturma
│
├── visual/
│ └── plotting.py # Rota çizimi & yakınsama grafiği
│
└── .streamlit/
└── secrets.toml # (Opsiyonel) API anahtarları

---


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

Aşağıda uygulamanın örnek çıktıları verilmiştir:

- En iyi rota (şehir indeksleri)
- ACO yakınsama grafiği
- Harita üzerinde en iyi rota çizimi
<img width="1919" height="590" alt="image" src="https://github.com/user-attachments/assets/ccf573be-5419-4242-b32e-b0359c9cf623" />
<img width="1550" height="518" alt="image" src="https://github.com/user-attachments/assets/939fa054-4705-4c1e-b76b-cb56958d3f70" />
<img width="1379" height="780" alt="image" src="https://github.com/user-attachments/assets/86ed394b-bd84-4ab1-ac3f-524a69fa04bb" />
<img width="1460" height="1453" alt="image" src="https://github.com/user-attachments/assets/6a8f38b4-c612-4ac0-9114-74352301b003" />

👤 Öğrenci Bilgileri

Ad: Rabia
Soyad: Çolak
Öğrenci No: 2212721008
GitHub Repo Linki: https://github.com/rabiicolak/aco_isparta_route






