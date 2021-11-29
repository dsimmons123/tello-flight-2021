from djitellopy import Tello
from time import sleep

# Initialize and Connect
tello = Tello()
tello.connect()

# Takeoff and move up to 6 feet (183cm)
tello.takeoff()
tello.move_up(101)

# Move forward (east) 5 feet (152cm)
tello.move_forward(152)
sleep(.5)

# rotate 90 degrees CCW
tello.rotate_counter_clockwise(90)

# move forward (north) 6 feet (183cm)
tello.move_forward(183)
sleep(.5)

# rotate CW 90 degrees
tello.rotate_clockwise(90)

# move down to 3 feet (91cm)
tello.move_down(91)

# move forward (east)
tello.move_forward(91)
sleep(.5)

# rotate 90 degrees CW
tello.rotate_clockwise(90)

# move up 1 foot (to 4 feet, 121cm)
tello.move_up(30)

# move forward 3 feet (91cm)
tello.move_forward(91)
sleep(.5)

# rotate CCW 90 degrees
tello.rotate_counter_clockwise(90)

# move forward 6 feet (183cm)
tello.move_forward(183)
sleep(.5)


tello.land()
