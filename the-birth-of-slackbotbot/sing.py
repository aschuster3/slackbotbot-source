from breezycreate2 import Robot
import time

# Helper to form the notes the way the API wants them
def addNote(note, duration, eighths=12):
    return note + "," + str(int(duration * eighths))

# A classic
def createOdeToJoy():
    ode_to_joy = ""
    ode_to_joy += addNote('E4', 2) + ","
    ode_to_joy += addNote('E4', 2) + ","
    ode_to_joy += addNote('F4', 2) + ","
    ode_to_joy += addNote('G4', 2) + ","
    ode_to_joy += addNote('G4', 2) + ","
    ode_to_joy += addNote('F4', 2) + ","
    ode_to_joy += addNote('E4', 2) + ","
    ode_to_joy += addNote('D4', 2) + ","
    ode_to_joy += addNote('C4', 2) + ","
    ode_to_joy += addNote('C4', 2) + ","
    ode_to_joy += addNote('D4', 2) + ","
    ode_to_joy += addNote('E4', 2) + ","
    ode_to_joy += addNote('E4', 3) + ","
    ode_to_joy += addNote('D4', 1) + ","
    ode_to_joy += addNote('D4', 4)
    return ode_to_joy

# Set everything like last time
outerBot = Robot()
bot = outerBot.robot

# In the background, this puts the song into
# one of the Roomba's "registers" and then
# calls it up, but for our purposes it just
# plays the notes
bot.play_song(1, createOdeToJoy())

outerBot.close()

