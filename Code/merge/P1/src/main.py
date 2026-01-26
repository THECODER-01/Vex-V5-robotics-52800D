# ---------------------------------------------------------------------------- #
#                                                                              #
# 	Module:       main.py                                                      #
# 	Author:       Nolan N                                                      #
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
#brain_inertial = Inertial(Ports.PORT_NULL)

# Construct a 4-Motor Drivetrain (SmartDrive is used with an Inertial Sensor)
# The values (wheel travel, track width, etc.) should be adjusted for your specific robot
drivetrain = SmartDrive(left_motors, right_motors, brain_inertial, 101.6, 317.5, 431.8, MM, 1)

# Example usage:
# drivetrain.drive_for(FORWARD, 12, INCHES)

# intake motor
motor_12 = Motor(Ports.PORT12, GearSetting.RATIO_18_1, False)

# O12F/top goal motor
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

Top = Event()
O12B = Event()
Bottom = Event()
O12F = Event()
O12S = Event()
AStop = Event()
PH = Event()
PL = Event()
Keep_Code = Event()

myVariable = 0
S = 0
Automonus = Event()

def Automonus_callback_0():
    global myVariable, S, Automonus, Bottom, Top, O12B, Bottom, O12F, O12S, AStop, PH, PL, PM, Keep_Code
    if bumper_a.pressing():
        # Right side
        drivetrain.drive_for(FORWARD, 400, MM)
        drivetrain.turn_for(RIGHT, 90, DEGREES)
        drivetrain.drive_for(FORWARD, 756, MM)
        drivetrain.turn_for(LEFT, 90, DEGREES)
        drivetrain.drive_for(FORWARD, 250, MM, wait=False)
        AUTOP.broadcast()
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
        AUTOP.broadcast()
        # Intake on
        # Top goal
        wait(8, SECONDS)

def onauton_autonomous_0():
    global myVariable, S, Automonus, Bottom, Top, O12B, Bottom, O12F, O12S, AStop, PH, PL, PM, Keep_Code
    drivetrain.set_drive_velocity(46, PERCENT)
    drivetrain.set_turn_velocity(46, PERCENT)
    motor_12.set_velocity(120, PERCENT)
    motor_13.set_velocity(120, PERCENT)
    motor_14.set_velocity(120, PERCENT)
    Automonus.broadcast()


def ondriver_drivercontrol_0():
    global Bottom, Top, O12B, Bottom, O12F, O12S, AStop, PH, PL, PM, Keep_Code
    drivetrain.set_drive_velocity(80, PERCENT)
    drivetrain.set_turn_velocity(80, PERCENT)
    motor_12.set_velocity(120, PERCENT)
    motor_13.set_velocity(120, PERCENT)
    motor_14.set_velocity(120, PERCENT)
    while True:
        if controller_1.buttonL1.pressing():
            Top.broadcast()
        if controller_1.buttonL2.pressing():
            Bottom.broadcast()
        if controller_1.buttonR1.pressing():
            O12F.broadcast()
        if controller_1.buttonR2.pressing():
            O12S.broadcast()
        if controller_1.buttonB.pressing():
            AStop.broadcast()
        if controller_1.buttonRight.pressing():
            PH.broadcast()
        if controller_1.buttonLeft.pressing():
            PL.broadcast()
        if controller_1.buttonX.pressing():
            Keep_Code.broadcast()
        if controller_1.buttonY.pressing():
            O12B.broadcast()
        wait(0.1, SECONDS)
        wait(5, MSEC)

def Top_callback_0():
    global Bottom, Top, O12B, Bottom, O12F, O12S, AStop, PH, PL, PM, Keep_Code
    motor_13.spin(FORWARD)
    motor_14.spin(FORWARD)
    # Top goal

def Bottom_callback_0():
    global Bottom, Top, O12B, Bottom, O12F, O12S, AStop, PH, PL, PM, Keep_Code
    motor_13.spin(REVERSE)
    motor_14.stop()
    # Bottom goal

def O12F_callback_0():
    global Bottom, Top, O12B, Bottom, O12F, O12S, AStop, PH, PL, PM, Keep_Code
    motor_12.spin(FORWARD)
    # This only moves M12

def O12S_callback_0():
    global Bottom, Top, O12B, Bottom, O12F, O12S, AStop, PH, PL, PM, Keep_Code
    motor_12.stop()
    # This only stops M12

def O12F_callback_0():
    global Bottom, Top, O12B, Bottom, O12F, O12S, AStop, PH, PL, PM, Keep_Code
    motor_12.spin(REVERSE)
    # This only moves M12

def AStop_callback_0():
    global Bottom, Top, O12B, Bottom, O12F, O12S, AStop, PH, PL, PM, Keep_Code
    motor_12.stop()
    motor_13.stop()
    motor_14.stop()
    # This stops All motors

def PH_callback_0():
    global Bottom, Top, O12B, Bottom, O12F, O12S, AStop, PH, PL, PM, Keep_Code
    pneumatic_flap.set(True)
    wait(0.3, SECONDS)
    # Pneumatic High (Goal)

def PL_callback_0():
    global Bottom, Top, O12B, Bottom, O12F, O12S, AStop, PH, PL, PM, Keep_Code
    pneumatic_flap.set(False)
    wait(0.3, SECONDS)
    # Pneumatic Low (Jail)

def Keep_Code_callback_0():
    global Bottom, Top, O12B, Bottom, O12F, O12S, AStop, PH, PL, PM, Keep_Code
    motor_12.spin(FORWARD)
    motor_13.spin(FORWARD)
    motor_14.stop()
    # Keep_Code

def AUTOP_callback_0():
    global Bottom, Top, O12B, Bottom, O12F, O12S, AStop, PH, PL, PM, Keep_Code
    motor_12.spin(FORWARD)
    motor_13.spin(FORWARD)
    motor_14.spin(FORWARD)
    # For auntom code

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
Top(Top_callback_0)
PL(PL_callback_0)
O12F(O12F_callback_0)
Bottom(Bottom_callback_0)
O12B(O12B_callback_0)
PH(PH_callback_0)
O12S(O12S_callback_0)
Keep_Code(Keep_Code_callback_0)
AStop(AStop_callback_0)

# add 15ms delay to make sure events are registered correctly.
wait(15, MSEC)