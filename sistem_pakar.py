def hitung_mbti(jawaban: list[str]) -> dict:
    skor = {
        "E": 0, "I": 0,
        "S": 0, "N": 0,
        "T": 0, "F": 0,
        "J": 0, "P": 0
    }

    for j in jawaban:
        j_upper = j.upper()
        if j_upper in skor:
            skor[j_upper] += 1

    total_ei = skor["E"] + skor["I"]
    total_sn = skor["S"] + skor["N"]
    total_tf = skor["T"] + skor["F"]
    total_jp = skor["J"] + skor["P"]

    persen_e = (skor["E"] / total_ei * 100) if total_ei > 0 else 0
    persen_i = (skor["I"] / total_ei * 100) if total_ei > 0 else 0
    persen_s = (skor["S"] / total_sn * 100) if total_sn > 0 else 0
    persen_n = (skor["N"] / total_sn * 100) if total_sn > 0 else 0
    persen_t = (skor["T"] / total_tf * 100) if total_tf > 0 else 0
    persen_f = (skor["F"] / total_tf * 100) if total_tf > 0 else 0
    persen_j = (skor["J"] / total_jp * 100) if total_jp > 0 else 0
    persen_p = (skor["P"] / total_jp * 100) if total_jp > 0 else 0

    dimensi_1 = "E" if skor["E"] >= skor["I"] else "I"
    dimensi_2 = "S" if skor["S"] >= skor["N"] else "N"
    dimensi_3 = "T" if skor["T"] >= skor["F"] else "F"
    dimensi_4 = "J" if skor["J"] >= skor["P"] else "P"

    tipe_dominan = f"{dimensi_1}{dimensi_2}{dimensi_3}{dimensi_4}"

    return {
        "tipe_dominan": tipe_dominan,
        "skor": skor,
        "persentase": {
            "E": round(persen_e, 2), "I": round(persen_i, 2),
            "S": round(persen_s, 2), "N": round(persen_n, 2),
            "T": round(persen_t, 2), "F": round(persen_f, 2),
            "J": round(persen_j, 2), "P": round(persen_p, 2)
        }
    }
