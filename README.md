# 🚁 Isparta Acil Durum Drone Rota Optimizasyonu (ACO)

Bu proje, **Karınca Kolonisi Algoritması (Ant Colony Optimization - ACO)** kullanılarak  
**Isparta’daki acil toplanma alanları arasında en kısa drone rota planlamasını** yapar.

Streamlit tabanlı bir web arayüzü ile kullanıcı, karınca sayısı ve iterasyon sayısını ayarlayarak  
en iyi rotayı, yakınsama grafiğini ve harita üzerindeki rota çizimini görüntüleyebilir.

---

## 📌 Kullanılan Teknolojiler
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


