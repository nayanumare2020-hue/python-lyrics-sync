import pygame
import time
import sys

pygame.mixer.init()
pygame.mixer.music.load("Arz Kiya Hai - RaagWorld.mp3")

start_time = 127.0

lyrics = [
    (127.0, "Haathon ko sambhale mere haathon mein"),
    (130.0, "Kaise haathon ko sambhale mere haathon mein"),
    (131.0, "Jab tak neend na aaye, inn lakeeron mein..."),
]

def type_line(text, speed=0.10):
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(speed)
    print()

pygame.mixer.music.play(start=start_time)

song_start = time.time()
index = 0

while index < len(lyrics):

    # Original song time
    current_time = start_time + (time.time() - song_start)

    lyric_time, lyric_text = lyrics[index]

    if current_time >= lyric_time:
        type_line("🎵 " + lyric_text)
        index += 1

    time.sleep(0.01)

# Last lyric ke baad 3 second wait
time.sleep(3)

pygame.mixer.music.stop()
pygame.quit()

print("Music Stopped")