# ============================================================
# K-Means - Auto Naming Cluster
# Sistem otomatis beri nama cluster berdasarkan skill dominan
# ============================================================

import pandas as pd
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.cluster import KMeans

# ============================================================
# KAMUS NAMA CLUSTER
# Ini yang kamu set SEKALI di koding — tidak perlu diubah lagi
# Sistem akan cocokkan skill dominan cluster dengan kamus ini
# ============================================================

KAMUS_CLUSTER = {
    # keyword skill       : nama cluster yang akan muncul di dashboard
    "React":              "Frontend & Design",
    "Vue":                "Frontend & Design",
    "CSS":                "Frontend & Design",
    "Figma":              "Frontend & Design",
    "JavaScript":         "Frontend & Design",
    "HTML":               "Frontend & Design",
    "Illustrator":        "Frontend & Design",

    "Laravel":            "Backend & DevOps",
    "PHP":                "Backend & DevOps",
    "MySQL":              "Backend & DevOps",
    "Docker":             "Backend & DevOps",
    "API":                "Backend & DevOps",
    "Linux":              "Backend & DevOps",

    "Python":             "Data & Analytics",
    "SQL":                "Data & Analytics",
    "Tableau":            "Data & Analytics",
    "Excel":              "Data & Analytics",
    "Machine Learning":   "Data & Analytics",

    "Flutter":            "Mobile Developer",
    "Dart":               "Mobile Developer",
    "Kotlin":             "Mobile Developer",
    "Android":            "Mobile Developer",
    "Firebase":           "Mobile Developer",
    "Swift":              "Mobile Developer",
}

# ============================================================
# FUNGSI AUTO NAMING
# Baca skill dominan cluster → cocokkan ke kamus → dapat nama
# ============================================================

def beri_nama_cluster(skill_dominan):
    skor = {}
    for skill in skill_dominan:
        if skill in KAMUS_CLUSTER:
            nama = KAMUS_CLUSTER[skill]
            skor[nama] = skor.get(nama, 0) + 1

    if not skor:
        return "Lainnya"

    # Ambil nama dengan skor tertinggi
    nama_terpilih = max(skor, key=skor.get)
    return nama_terpilih

# ============================================================
# DATA ALUMNI (simulasi — nanti dari database Laravel)
# ============================================================

data_alumni = [
    {"nama": "Rizky",   "skill": ["React", "Vue", "CSS", "Figma"]},
    {"nama": "Siti",    "skill": ["Figma", "CSS", "Illustrator", "React"]},
    {"nama": "Bagas",   "skill": ["React", "JavaScript", "CSS", "HTML"]},
    {"nama": "Dewi",    "skill": ["Laravel", "MySQL", "PHP", "Docker"]},
    {"nama": "Andi",    "skill": ["Laravel", "MySQL", "API", "PHP"]},
    {"nama": "Fauzi",   "skill": ["MySQL", "Docker", "Linux", "Laravel"]},
    {"nama": "Rini",    "skill": ["Python", "SQL", "Tableau", "Excel"]},
    {"nama": "Hendra",  "skill": ["Python", "Machine Learning", "SQL"]},
    {"nama": "Mega",    "skill": ["SQL", "Excel", "Tableau", "Python"]},
    {"nama": "Yusuf",   "skill": ["Flutter", "Dart", "Firebase", "Android"]},
    {"nama": "Laras",   "skill": ["Kotlin", "Android", "Firebase"]},
    {"nama": "Dimas",   "skill": ["React", "Figma", "CSS", "JavaScript"]},
]

# ============================================================
# PROSES K-MEANS
# ============================================================

df = pd.DataFrame(data_alumni)
mlb = MultiLabelBinarizer()
skill_matrix = mlb.fit_transform(df["skill"])

kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)
kmeans.fit(skill_matrix)
df["cluster_id"] = kmeans.labels_

# ============================================================
# AUTO NAMING — sistem yang tentukan nama, bukan kamu manual
# ============================================================

skill_df = pd.DataFrame(skill_matrix, columns=mlb.classes_)
skill_df["cluster_id"] = df["cluster_id"]

nama_cluster = {}
for i in df["cluster_id"].unique():
    cluster_data = skill_df[skill_df["cluster_id"] == i].drop("cluster_id", axis=1)
    skill_dominan = cluster_data.mean().sort_values(ascending=False)
    top_5_skill = skill_dominan[skill_dominan > 0].head(5).index.tolist()
    nama_cluster[i] = beri_nama_cluster(top_5_skill)

df["nama_cluster"] = df["cluster_id"].map(nama_cluster)

# ============================================================
# OUTPUT — ini yang dikirim ke Laravel sebagai JSON
# ============================================================

print("=== HASIL CLUSTER (yang akan dikirim ke Laravel) ===\n")
for i in sorted(df["cluster_id"].unique()):
    anggota = df[df["cluster_id"] == i]
    nama = nama_cluster[i]
    print(f"Cluster {i} → '{nama}' ({len(anggota)} alumni)")
    for _, row in anggota.iterrows():
        print(f"   - {row['nama']}")
    print()

# Format JSON untuk dikirim ke Laravel
import json
hasil_json = []
for _, row in df.iterrows():
    hasil_json.append({
        "nama": row["nama"],
        "cluster_id": int(row["cluster_id"]),
        "nama_cluster": row["nama_cluster"]
    })

print("=== FORMAT JSON → LARAVEL ===")
print(json.dumps(hasil_json, indent=2))