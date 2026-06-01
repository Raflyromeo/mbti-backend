<div align="center">

# ⚙️ Sistem Pakar MBTI - Backend API

**Layanan API bertenaga Python untuk inferensi sistem pakar MBTI yang cepat dan akurat.**

[![Framework](https://img.shields.io/badge/Framework-FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Language](https://img.shields.io/badge/Language-Python_3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)

</div>

---

## 📌 Latar Belakang

Repositori ini berisi kode *Backend* dari aplikasi Sistem Pakar MBTI. Sistem ini bertanggung jawab penuh sebagai mesin inferensi (*inference engine*) yang menerima data observasi (jawaban pengguna), memprosesnya berdasarkan aturan basis pengetahuan psikologi MBTI, dan mengembalikan hasil analisis berupa **Tipe Kepribadian Dominan** serta probabilitas/persentase untuk tiap dimensi.

Dibangun dengan arsitektur **FastAPI**, *backend* ini dirancang untuk menyajikan performa tinggi (*high performance*) saat dihubungkan dengan *frontend* React/Next.js.

---

## ✨ Fitur Utama

| Fitur | Keterangan |
|---|---|
| 🧠 **Mesin Inferensi** | Algoritma perhitungan yang memetakan kecenderungan 4 dimensi MBTI |
| ⚡ **Performa Tinggi** | Waktu respons API secepat kilat berkat framework FastAPI |
| 🛡️ **Validasi Data** | Pengecekan *payload* otomatis menggunakan Pydantic |
| 🌐 **CORS Setup** | Middleware yang disesuaikan untuk integrasi aman dengan antarmuka web |
| 📖 **Auto-Docs** | Dokumentasi interaktif (Swagger UI) yang otomatis dihasilkan |

---

## 🚀 Quick Start

### Prerequisites

- [Python](https://www.python.org/) v3.10+
- pip (Python Package Installer)

### Clone & Install

```bash
# Clone repository
git clone <url-repo-backend-anda>
cd backend-pakar

# (Opsional) Buat dan aktifkan Virtual Environment
python -m venv venv
# Windows: .\venv\Scripts\activate
# Mac/Linux: source venv/bin/activate

# Install dependencies
pip install fastapi uvicorn pydantic
```

### Menjalankan Secara Lokal

**Terminal:**
```bash
uvicorn utama:app --reload --port 8000
```

Pastikan Anda menggunakan parameter `--port 8000` agar URL sesuai dengan yang dibutuhkan oleh *frontend* (`http://localhost:8000`). Buka dokumentasi API interaktif di [http://localhost:8000/docs](http://localhost:8000/docs).

---

## 🏗️ Struktur Folder

```text
backend-pakar/
│
├── utama.py               # Entry-point server FastAPI & Konfigurasi CORS
├── sistem_pakar.py        # Logika inti komputasi algoritma MBTI
├── README.md              # Dokumentasi proyek
└── venv/                  # (Generated) Virtual Environment
```

---

## 🛠️ Tech Stack

### Backend API
| Teknologi | Kegunaan |
|---|---|
| [Python 3](https://www.python.org/) | Bahasa Pemrograman Utama |
| [FastAPI](https://fastapi.tiangolo.com/) | Web Framework API |
| [Uvicorn](https://www.uvicorn.org/) | ASGI Web Server |
| [Pydantic](https://docs.pydantic.dev/) | Validasi Data Input/Output |

---

## 🎓 Informasi Tugas Mata Kuliah

Proyek ini merupakan bagian dari Tugas dari Mata Kuliah **Sistem Berbasis Pengetahuan** di Universitas Gunadarma yang dibuat oleh:

**Nama:** Muhammad Rafly Romeo Nasution  
**NPM:** 10123875  
**Kelas:** 3KA25  
**Program Studi:** Sistem Informasi  
**Semester:** 6  

🔗 **Portfolio:** [rafly romeo portfolio](https://raflyromeo-portfolio.vercel.app/)

---

## 👤 Pembuat

<div align="center">

**Muhammad Rafly Romeo Nasution**

<p align="center">
  <a href="https://linkedin.com/in/muhammadraflyromeonasution">
    <img src="https://img.shields.io/badge/LinkedIn-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" height="30"/>
  </a>
  <a href="https://instagram.com/rfly.romeo_">
    <img src="https://img.shields.io/badge/Instagram-%23E4405F.svg?style=for-the-badge&logo=Instagram&logoColor=white" alt="Instagram" height="30"/>
  </a>
  <a href="mailto:raflyromeonasution07@gmail.com">
    <img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="Email" height="30"/>
  </a>
</p>

</div>

---

<div align="center">

Made with ❤️ by Rafly Romeo · 2026

</div>

