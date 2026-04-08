import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Data pekerjaan
jobs = pd.DataFrame({
    'job_id': [1, 2, 3, 4],
    'job_title': [
        'Backend Developer',
        'Frontend Developer',
        'Data Analyst',
        'UI UX Designer'
    ],
    'description': [
        'laravel php mysql backend api',
        'react javascript frontend html css',
        'python data analysis machine learning statistics',
        'figma design user interface user experience'
    ]
})

# Data alumni (user)
alumni = {
    'name': 'Bagas',
    'profile': 'laravel php backend mysql frontend react dan css'
}

# Gabungkan data job + user
all_text = jobs['description'].tolist()
all_text.append(alumni['profile'])

# Vectorisasi teks menggunakan TF-IDF
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(all_text)

# similarity antara semua data
cosine_sim = cosine_similarity(tfidf_matrix)

# ambil similarity user (data terakhir)
user_sim = cosine_sim[-1][:-1]

# masukkan similarity ke dataframe
jobs['similarity'] = user_sim

# urutkan dari terbesar
recommendations = jobs.sort_values(by='similarity', ascending=False)

print("Rekomendasi pekerjaan untuk:", alumni['name'])
print("----------------------------------------")

for index, row in recommendations.iterrows():
    print(f"{row['job_title']} (Score: {row['similarity']:.4f})")