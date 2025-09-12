import time, sys

def animate_text(text, delay=0.08):  
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

# (Lirik, jeda antar baris, kecepatan ketikan)
bridge_lyrics = [
    ("Aku ingin kau menerima seluruh hatiku", 1.3, 0.18),
    ("Aku ingin kau mengerti di jiwaku hanya kamu", 1.7, 0.12),
    ("Namun, bila kau tak bisa menerima aku", 1.5, 0.15),   # sedikit lebih lambat
    ("Lebih baik ku hidup tanpa cinta", 2.8, 0.10),         # penutup lebih panjang
]

def sing_bridge():
    for lyric, gap, speed in bridge_lyrics:
        animate_text(lyric, speed)
        if gap > 0:
            time.sleep(gap)

sing_bridge()
