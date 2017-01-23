from breezycreate2 import Robot
import time

# This is what the API actually exposes
outerBot = Robot()

# This is an inner reference that allows me to do
# some more fine tuned work
bot = outerBot.robot

# The commands are non-blocking, so I have to
# block manually with some well placed sleeps
bot.turn_clockwise(100)
time.sleep(1)
bot.turn_clockwise(0)
time.sleep(0.1)
bot.drive_straight(300)
time.sleep(3.3) # Gotta last as long as the action
bot.drive_straight(0)
time.sleep(0.1)

# Close the connection because we're not heathens
outerBot.close()

