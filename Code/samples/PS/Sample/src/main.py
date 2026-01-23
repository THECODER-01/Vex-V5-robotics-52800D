# ----------------------------------------------------------------------------- #
#                                                                               #                                                                          
#    Project:        Clawbot Controller with Events                             #
#    Module:         main.py                                                    #
#    Author:         VEX                                                        #
#    Created:        Fri Aug 05 2022                                            #
#    Description:    This example will use Controller button events to          # 
#                    control the V5 Clawbot arm and claw                        #
#                                                                               #                                                                          
#    Configuration:  V5 Clawbot (Individual Motors)                             #
#                    Controller                                                 #
#                    Claw Motor in Port 3                                       #
#                    Arm Motor in Port 8                                        #
#                    Left Motor in Port 1                                       #
#                    Right Motor in Port 10                                     #
#                                                                               #                                                                          
# ----------------------------------------------------------------------------- #

# Library imports
from vex import *

# Brain should be defined by default
brain=Brain()

# Robot configuration code
claw_motor = Motor(Ports.PORT3, GearSetting.RATIO_18_1, False)
arm_motor = Motor(Ports.PORT8, GearSetting.RATIO_18_1, False)
controller_1 = Controller(PRIMARY)
left_motor = Motor(Ports.PORT1, GearSetting.RATIO_18_1, False)
right_motor = Motor(Ports.PORT10, GearSetting.RATIO_18_1, True)


# Begin project code
# Create callback functions for each controller button event
def controller_L1_Pressed():
    arm_motor.spin(FORWARD)
    while controller_1.buttonL1.pressing():
        wait(5, MSEC)
    arm_motor.stop()

def controller_L2_Pressed():
    arm_motor.spin(REVERSE)
    while controller_1.buttonL2.pressing():
        wait(5, MSEC)
    arm_motor.stop()

def controller_R1_Pressed():
    claw_motor.spin(REVERSE)
    while controller_1.buttonR1.pressing():
        wait(5, MSEC)
    claw_motor.stop()

def controller_R2_Pressed():
    claw_motor.spin(FORWARD)
    while controller_1.buttonR2.pressing():
        wait(5, MSEC)
    claw_motor.stop()

# Create Controller callback events - 15 msec delay to ensure events get registered
controller_1.buttonL1.pressed(controller_L1_Pressed)
controller_1.buttonL2.pressed(controller_L2_Pressed)
controller_1.buttonR1.pressed(controller_R1_Pressed)
controller_1.buttonR2.pressed(controller_R2_Pressed)
wait(15, MSEC)

# Configure Arm and Claw motor hold settings and velocity
arm_motor.set_stopping(HOLD)
claw_motor.set_stopping(HOLD)
arm_motor.set_velocity(60, PERCENT)
claw_motor.set_velocity(30, PERCENT)

# Main Controller loop to set motors to controller axis postiions
while True:
    left_motor.set_velocity(controller_1.axis3.position(), PERCENT)
    right_motor.set_velocity(controller_1.axis2.position(), PERCENT)
    left_motor.spin(FORWARD)
    right_motor.spin(FORWARD)
    wait(5, MSEC)
