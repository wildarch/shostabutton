from vlc import MediaPlayer
import RPi.GPIO as GPIO
import time
import os
import random

def play(player):
    player = random.choice(players)
    player.play()
    # Wait till the current sound is done
    while player.is_playing() or player.will_play():
        pass
    player.stop()


# Configure button pin
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Create players by find all mp3 files in the working dir
files = os.listdir('.')
players = [ MediaPlayer(file_name) for file_name in files if file_name.endswith('.mp3') ]
print("Loaded {} sounds".format(len(players)))

play(random.choice(players))

while True:
    input_state = GPIO.input(18)
    if input_state == False:
        time.sleep(0.1)
        input_state = GPIO.input(18)
        if input_state == False:
            play(random.choice(players))
            print("Done")
        else:
            print("Debounce caught invalid press")
    time.sleep(0.05)
