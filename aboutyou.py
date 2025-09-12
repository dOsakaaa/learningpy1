import time, sys

def animate_text(text, delay=0.09):  # tempo dasar, lebih cepat dari sebelumnya
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

# (Lirik, jeda setelah baris, kecepatan ketik)
bridge_lyrics = [
    ("There was something about you that now I can't remember", 0, 0.08),
    ("It's the same damn thing that made my heart surrender", 0, 0.08),
    ("And I'll miss you on a train", 0, 0.08),
    ("I'll miss you in the morning", 0, 0.09),
    ("I never know what to think about", 0.6, 0.11),  # ⬅️ sedikit diperlambat
    ("I think about you....", 0.5, 0.10),
]

def sing_bridge():
    for lyric, gap, speed in bridge_lyrics:
        animate_text(lyric, speed)
        if gap > 0:
            time.sleep(gap)

sing_bridge()
