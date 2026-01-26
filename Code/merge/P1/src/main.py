# ---------------------------------------------------------------------------- #
#                                                                              #
# 	Module:       main.py                                                      #
# 	Author:       codespace                                                    #
# 	Created:      1/23/2026, 5:43:40 PM                                        #
# 	Description:  V5 project                                                   #
#                                                                              #
# ---------------------------------------------------------------------------- #

# Library imports
from vex import *

# Brain should be defined by default
brain=Brain()

# Library imports
from vex import *

controller_1 = Controller(PRIMARY)

# Create the left Motors and group them under the MotorGroup "left_motors"
# The 'True' argument in a Motor definition reverses its direction if needed
left_motor_f = Motor(Ports.PORT1, GearSetting.RATIO_18_1, False)
left_motor_b = Motor(Ports.PORT11, GearSetting.RATIO_18_1, False)
left_motors = MotorGroup(left_motor_f, left_motor_b)

# Create the right Motors and group them under the MotorGroup "right_motors"
# Motors on opposite sides often need to be reversed to spin in the same direction for forward movement
right_motor_f = Motor(Ports.PORT9, GearSetting.RATIO_18_1, True)
right_motor_b = Motor(Ports.PORT20, GearSetting.RATIO_18_1, True)
right_motors = MotorGroup(right_motor_f, right_motor_b)

# (Optional) Create an Inertial Sensor for a SmartDrive
brain_inertial = Inertial(Ports.PORT_NULL)

# Construct a 4-Motor Drivetrain (SmartDrive is used with an Inertial Sensor)
# The values (wheel travel, track width, etc.) should be adjusted for your specific robot
drivetrain = SmartDrive(left_motors, right_motors, brain_inertial, 101.6, 295, 40, MM, 1)

# Example usage:
# drivetrain.drive_for(FORWARD, 12, INCHES)

# intake motor
motor_12 = Motor(Ports.PORT12, GearSetting.RATIO_18_1, False)

# middle/top goal motor
motor_13 = Motor(Ports.PORT13, GearSetting.RATIO_18_1, False)

# jail motor
motor_14 = Motor(Ports.PORT14, GearSetting.RATIO_18_1, False)

# Define a 3-wire digital output on port F
# Supported ports are Brain.three_wire_port.a through h
pneumatic_flap = DigitalOut(brain.three_wire_port.f)

# Define a 3-wire Bumper on port A
bumper_a = Bumper(brain.three_wire_port.a)

# To set the device to high (on)
#pneumatic_flap.set(True)

# To set the device to low (off)
#pneumatic_flap.set(False)

#1_1_2 = Motor(Ports.PORT10, GearSetting.RATIO_18_1, True)

myVariable = 0
S = 0
Automonus = Event()

def Automonus_callback_0():
    global myVariable, S, Automonus
    if bumper_a.pressing():
        # Right side
        drivetrain.drive_for(FORWARD, 400, MM)
        drivetrain.turn_for(RIGHT, 90, DEGREES)
        drivetrain.drive_for(FORWARD, 756, MM)
        drivetrain.turn_for(LEFT, 90, DEGREES)
        drivetrain.drive_for(FORWARD, 250, MM, wait=False)
        motor_13.spin(FORWARD)
        motor_14.spin(FORWARD)
        motor_12.spin(FORWARD)
        # Intake on
        # Top goal
        wait(8, SECONDS)
    else:
        # Left side
        drivetrain.drive_for(FORWARD, 400, MM)
        drivetrain.turn_for(LEFT, 90, DEGREES)
        drivetrain.drive_for(FORWARD, 756, MM)
        drivetrain.turn_for(RIGHT, 90, DEGREES)
        drivetrain.drive_for(FORWARD, 250, MM, wait=False)
        motor_13.spin(FORWARD)
        motor_14.spin(FORWARD)
        motor_12.spin(FORWARD)
        # Intake on
        # Top goal
        wait(8, SECONDS)

def onauton_autonomous_0():
    global myVariable, S, Automonus
    drivetrain.set_drive_velocity(46, PERCENT)
    drivetrain.set_turn_velocity(46, PERCENT)
    motor_12.set_velocity(120, PERCENT)
    motor_13.set_velocity(120, PERCENT)
    motor_14.set_velocity(120, PERCENT)
    Automonus.broadcast()

def ondriver_drivercontrol_0():
    global myVariable, S, Automonus
    drivetrain.set_drive_velocity(80, PERCENT)
    drivetrain.set_turn_velocity(80, PERCENT)
    motor_12.set_velocity(120, PERCENT)
    motor_13.set_velocity(120, PERCENT)
    motor_14.set_velocity(120, PERCENT)
    while True:
        if controller_1.buttonL1.pressing():
            motor_13.spin(FORWARD)
            motor_14.spin(FORWARD)
            # Top goal
        if controller_1.buttonL2.pressing():
            motor_13.spin(REVERSE)
            motor_14.stop()
            # Bottom goal
        if controller_1.buttonR1.pressing():
            motor_12.spin(FORWARD)
            # Intake on
        if controller_1.buttonR2.pressing():
            motor_12.stop()
            # Intake off
        if controller_1.buttonB.pressing():
            motor_12.stop()
            motor_13.stop()
            motor_14.stop()
            # Stop all
        if controller_1.buttonA.pressing():
            motor_14.spin(REVERSE)
            # Jail needs testing
        if controller_1.buttonRight.pressing():
            pneumatic_flap.set(True)
            # Pneumatic High (Goal)
            wait(0.3, SECONDS)
        if controller_1.buttonLeft.pressing():
            pneumatic_flap.set(False)
            wait(0.3, SECONDS)
            # Pneumatic Low (Jail)
        if controller_1.buttonX.pressing():
            motor_12.spin(FORWARD)
            motor_13.spin(FORWARD)
            motor_14.stop()
            # Keep Code
        if controller_1.buttonY.pressing():
            motor_12.spin(REVERSE)
            # Intake R
        wait(5, MSEC)

# create a function for handling the starting and stopping of all autonomous tasks
def vexcode_auton_function():
    # Start the autonomous control tasks
    auton_task_0 = Thread( onauton_autonomous_0 )
    # wait for the driver control period to end
    while( competition.is_autonomous() and competition.is_enabled() ):
        # wait 10 milliseconds before checking again
        wait( 10, MSEC )
    # Stop the autonomous control tasks
    auton_task_0.stop()

def vexcode_driver_function():
    # Start the driver control tasks
    driver_control_task_0 = Thread( ondriver_drivercontrol_0 )

    # wait for the driver control period to end
    while( competition.is_driver_control() and competition.is_enabled() ):
        # wait 10 milliseconds before checking again
        wait( 10, MSEC )
    # Stop the driver control tasks
    driver_control_task_0.stop()


# register the competition functions
competition = Competition( vexcode_driver_function, vexcode_auton_function )

# system event handlers
Automonus(Automonus_callback_0)
# add 15ms delay to make sure events are registered correctly.
wait(15, MSEC)
