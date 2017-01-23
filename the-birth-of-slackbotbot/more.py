from breezycreate2 import Robot
import time
from datetime import datetime

# To elaborate a little more as to what this is,
# the note variable reflects the note that we want to
# play, the duration corresponds to how long we want
# the note to play, and the eighths variable tells
# us how long an eighth note is held (in some arbitrary
# unit). I found 12 to sound best, but feel free to
# disagree and do your own thing.
def addNote(note, duration, eighths=12):
    return note + "," + str(int(duration * eighths))

# Because this song is a little longer, I had to split
# it into 2 in order to play it all. This means we've got
# to sleep our Python process while the first part
# finishes.
def createMarioP1():
    mario = ""
    mario += addNote('E5', 1) + ","
    mario += addNote('E5', 1) + ","
    mario += addNote('rest', 1) + ","
    mario += addNote('E5', 1) + ","
    mario += addNote('rest', 1) + ","
    mario += addNote('C5', 1) + ","
    mario += addNote('E5', 1) + ","
    mario += addNote('rest', 1) + ","
    mario += addNote('G5', 1) + ","
    mario += addNote('rest', 3) + ","
    mario += addNote('G4', 2) + ","
    mario += addNote('rest', 3)
    return mario

def createMarioP2():
    mario = ""
    mario += addNote('C5', 1) + ","
    mario += addNote('rest', 2) + ","
    mario += addNote('G4', 1) + ","
    mario += addNote('rest', 2) + ","
    mario += addNote('E4', 1) + ","
    mario += addNote('rest', 2) + ","
    mario += addNote('A4', 1) + ","
    mario += addNote('rest', 1) + ","
    mario += addNote('B4', 1) + ","
    mario += addNote('rest', 1) + ","
    mario += addNote('A#4', 1) + ","
    mario += addNote('A4', 1) + ","
    mario += addNote('rest', 1) + ","
    mario += addNote('G4', 1.25) + ","
    mario += addNote('E5', 1.25) + ","
    mario += addNote('G5', 1.25) + ","
    mario += addNote('A5', 1) + ","
    mario += addNote('rest', 1) + ","
    mario += addNote('F5', 1) + ","
    mario += addNote('G5', 1) + ","
    mario += addNote('rest', 1) + ","
    mario += addNote('E5', 1) + ","
    mario += addNote('rest', 1) + ","
    mario += addNote('C5', 1) + ","
    mario += addNote('D5', 1) + ","
    mario += addNote('B4', 1) + ","
    mario += addNote('rest', 2)
    return mario

# The first glimpse of reading sensors!  I'll
# be honest in that I don't know why we get
# packet 100, but that's what the API does and
# I'm pretty sure the Open Interface tells you
# to do that too. We can put this in a tight
# loop so that we minimize lag between song
# parts
def blockForSong(bot):
    while True:
        bot.get_packet(100)
        if not bot.sensor_state['song playing']:
            break

# The Roomba has a small LED screen that displays
# numbers normally, but the writer of the Python
# API gave us some built in conversions so that
# we can print text! This is a helper method
# that flashes the letters 4 at a time because
# the buffer we have to work with is only 4 long.
def scrollText(bot, message):
    message = "    " + message + "    "
    length = len(message)
    messageDisplay = 0
    while messageDisplay + 3 < length:
        print(message[messageDisplay:messageDisplay+4])
        bot.digit_led_ascii(message[messageDisplay:messageDisplay+4])
        time.sleep(.5)
        messageDisplay += 1


outerBot = Robot()
bot = outerBot.robot

bot.play_song(0, createMarioP1())
# Because I'm not one to discourage failure, try uncommenting this
# line to see what happens when you try to run this without blocking.
blockForSong(bot)
bot.play_song(1, createMarioP2())
blockForSong(bot)

scrollText(bot, "Hello World!")

outerBot.close()

