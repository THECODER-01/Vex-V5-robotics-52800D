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

1_1_2 = Motor(Ports.PORT3, GearSetting.RATIO_18_1, False)
1_1_2 = Motor(Ports.PORT8, GearSetting.RATIO_18_1, False)
controller_1 = Controller(PRIMARY)
1_1_2 = Motor(Ports.PORT1, GearSetting.RATIO_18_1, False)
1_1_2 = Motor(Ports.PORT10, GearSetting.RATIO_18_1, True)

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
