from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sistem_pakar import hitung_mbti

app = FastAPI(title="API Sistem Pakar MBTI")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class PermintaanDiagnosa(BaseModel):
    jawaban: list[str]

@app.post("/api/diagnosa")
def diagnosa_mbti(permintaan: PermintaanDiagnosa):
    if not permintaan.jawaban:
        raise HTTPException(status_code=400, detail="Jawaban tidak boleh kosong")
    
    hasil = hitung_mbti(permintaan.jawaban)
    return {
        "status": "sukses",
        "data": hasil
    }

@app.get("/")
def baca_root():
    return {"pesan": "API Sistem Pakar MBTI Berjalan"}
