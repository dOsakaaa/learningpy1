import time, sys, shutil, textwrap

def get_term_width(default=80):
    try:
        cols = shutil.get_terminal_size((default, 20)).columns
        return max(cols, 40)
    except:
        return default

def animate_text(text, delay=0.12):  
    width = get_term_width()
    wrapped_lines = textwrap.wrap(text, width=width - 4)
    for line in wrapped_lines:
        padding = max((width - len(line)) // 2, 0)
        sys.stdout.write(" " * padding)
        for ch in line:
            sys.stdout.write(ch)
            sys.stdout.flush()
            time.sleep(delay)
        sys.stdout.write("\n")
        sys.stdout.flush()

def print_title(title):
    width = get_term_width()
    sep = "=" * (len(title) + 10)
    print("\n" + sep.center(width))
    animate_text(title.upper(), delay=0.10)
    print(sep.center(width) + "\n")

judul_lagu = "On Bended Knee"
# Mulai lagu dari detik 0.54
bridge_lyrics = [
    ("And I know I just need one more chance", 0.40, 0.10),
    ("To prove my love to you", 1.5, 0.10),
    ("And if you come back to me", 0.8, 0.09),
    ("I'll guarantee", 0.28, 0.10),
    ("That I'll never let you go", 1.0, 0.11),

    ("Can we go back to the days our love was strong?", 2.9, 0.09),
    ("Can you tell me how a perfect love goes wrong?", 2.7, 0.13),
    ("Can somebody tell me how to get things back", 1.4, 0.09),
    ("The way they used to be?", 1.5, 0.11),

    ("Oh God give me a reason", 1.9, 0.09),
    ("I'm down on bended knee", 2.5, 0.10)
]

def sing_bridge():
    print_title(judul_lagu)
    time.sleep(1.5)
    for lyric, gap, speed in bridge_lyrics:
        animate_text(lyric, delay=speed)
        if gap > 0:
            time.sleep(gap)

if __name__ == "__main__":
    sing_bridge()
