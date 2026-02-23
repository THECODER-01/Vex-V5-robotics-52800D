# ---------------------------------------------------------------------------- #
#                                                                              #
# 	Module:       main.py                                                      #
# 	Author:       Nolan N                                                      #
# 	Description:  V5 project (MINI-BOT, MECHANUM-DRIVE)  V.Latest  V.ALL       #
#                                                                              #
# ---------------------------------------------------------------------------- #
#   Additons to commit:                                                        #
#                                                                              #
#                Done?                                                         # 
#                                                                              #
#   Push to all branches                                                       # 
#                                                                              # 
# ---------------------------------------------------------------------------- #

# Library imports
from vex import *

'''
ROBOT CONFIGURATION:
wheel_diameter: 2.75 in (220 MM)
track_width: 
wheel_base: 
externalGearRatio: 1:1
internalGearRatio: 1:1
inertial_sensor: V5 Inertial Sensor (PORT21)
left_motor_b: Motor (PORT78)
right_motor_b: Motor (PORT10)
motor_11: Motor (PORT11) (Ladder Motor)
'''

# Brain should be defined by default
brain=Brain()

# Define Primary Controller (  Add Controller 2 if needed with: controller_2 = Controller(PARTNER)  )
controller_1 = Controller(PRIMARY)

# Create the left Motors and group them under the MotorGroup "left_motors"
# The 'True' argument in a Motor definition reverses its direction if needed
left_motor_f = Motor(Ports.PORT21, GearSetting.RATIO_18_1, False)
left_motor_b = Motor(Ports.PORT19, GearSetting.RATIO_18_1, False)
left_motors = MotorGroup(left_motor_f, left_motor_b)

# Create the right Motors and group them under the MotorGroup "right_motors"
# Motors on opposite sides often need to be reversed to spin in the same direction for forward movement
right_motor_f = Motor(Ports.PORT18, GearSetting.RATIO_18_1, True)
right_motor_b = Motor(Ports.PORT12, GearSetting.RATIO_18_1, True)
right_motors = MotorGroup(right_motor_f, right_motor_b)

# (Optional) Create an Inertial Sensor for a SmartDrive
# brain_inertial = Inertial(brain.three_wire_port.h)
Inertial_sensor = Inertial(Ports.PORT21)
# (Optional) Create an Gyro Sensor for a SmartDrive
#Gyro_sensor = None # Gyro(brain.three_wire_port.h)
#Inertial_sensor.quality(100)

# Construct a 4-Motor Drivetrain (SmartDrive is used with an Inertial Sensor)
# The values (wheel travel, track width, etc.) should be adjusted for your specific robot
drivetrain = SmartDrive(left_motors, right_motors, Inertial_sensor, 200, 200, 220, MM, 1)
#drivetrain = DriveTrain(left_motors, right_motors, 319.19, 309.88, 317.5, MM, 1)

"""
Create a drivetrain with the following values:
- wheelTravel = 319.19
- trackWidth = 309.88
- wheelBase = 317.5
- units = MM (Millimeters)
- externalGearRatio - 1
drivetrain = SmartDrive(left_motors, right_motors, Inertial_sensor, 319.19, 309.88, 317.5, MM, 1)
"""
"""
Create a drivetrain with the following values:
- wheelTravel = 200
- trackWidth = 200
- wheelBase = 220
- units = MM (Millimeters)
- externalGearRatio - 1
drivetrain = SmartDrive(left_motors, right_motors, Inertial_sensor, 200, 200, 220, MM, 1)
"""

# Example usage:
# drivetrain.drive_for(FORWARD, 12, INCHES)

# Calibrate the drivetrain
# calibrate_drivetrain()

# ladder_motor
motor_11 = Motor(Ports.PORT11, GearSetting.RATIO_18_1, False)

Automonus = Event()
place_Holder = Event()
start_Calibration = Event()

def pre_auton():
    global pre_auton, Automonus, start_Calibration
    # \/ Any autonomous drivetrain movement uses are here \/
    # drivetrain.turn_for(self, direction, angle, units=RotationUnits.DEG, velocity=None, units_v:VelocityPercentUnits=VelocityUnits.RPM, wait=True)
    # drivetrain.turn_to_heading(self, angle, units=RotationUnits.DEG, velocity=None, units_v:VelocityPercentUnits=VelocityUnits.RPM, wait=True)
    # drivetrain.turn_for(self, angle, units=RotationUnits.DEG, velocity=None, units_v:VelocityPercentUnits=VelocityUnits.RPM, wait=True)
    # drivetrain.set_turn_threshold(self, value)
    # drivetrain.set_turn_constant(self, value)
    start_Calibration.broadcast() # Broadcast to the MAIN Calibration code to start
    
def onauton_autonomous_0():
    global Automonus, place_Holder
    # \/ Autonomous SETUP code here \/
    drivetrain.set_drive_velocity(48, PERCENT)
    drivetrain.set_turn_velocity(48, PERCENT)
    Automonus.broadcast() # Broadcast to the MAIN Automonus code to start

def Automonus_callback_0():
    global Automonus, place_Holder
    return

def ondriver_drivercontrol_0():
    global place_Holder
    while True:
       # Read controller axes each loop so values update continuously.
       # Axis mapping for mecanum wheels:
       # axis1 (x) -> rotation (turn left/right)
       # axis3 (y) -> forward/back
       # axis4 (z) -> strafe left/right
        rot = controller_1.axis1.position()
        forward = controller_1.axis3.position()
        strafe = controller_1.axis4.position()

        # small deadband to ignore joystick noise
        deadband = 5
        if abs(rot) < deadband:
            rot = 0
        if abs(forward) < deadband:
            forward = 0
        if abs(strafe) < deadband:
            strafe = 0

        # Mecanum wheel mixing (robot-centric):
        # front_left = forward + strafe + rotation
        # front_right = forward - strafe - rotation
        # back_left = forward - strafe + rotation
        # back_right = forward + strafe - rotation
        fl = forward + strafe + rot
        fr = forward - strafe - rot
        bl = forward - strafe + rot
        br = forward + strafe - rot

        # Normalize values so none exceed 100%
        max_val = max(abs(fl), abs(fr), abs(bl), abs(br), 100)
        if max_val > 100:
            scale = 100.0 / max_val
            fl *= scale
            fr *= scale
            bl *= scale
            br *= scale

        # Send commands to individual motors
        left_motor_f.spin(FORWARD, fl, PERCENT)
        right_motor_f.spin(FORWARD, fr, PERCENT)
        left_motor_b.spin(FORWARD, bl, PERCENT)
        right_motor_b.spin(FORWARD, br, PERCENT)

        if controller_1.buttonA.pressing():
            place_Holder.broadcast()

        # small delay for responsiveness
        wait(5, MSEC)

def place_Holder_callback_0():
    global place_Holder
    # This is a place holder for any future events or code you may want to add
    # You can also use this event for testing or development purposes with out being tied to a specific button or action
    return

def start_Calibration_callback_0(a, b):
    global Automonus, place_Holder, start_Calibration
    brain.screen.print("Calibrating Inertial_sensor Sensor...")
    Inertial_sensor.calibrate() # Calibrates the sensor
    while Inertial_sensor.is_calibrating():
        sleep(50) # Wait for calibration to complete
    brain.screen.clear_screen(Color.BLACK)
    brain.screen.clear_line()
    wait(10, MSEC) # Short delay after clear screen to ensure the message is visible before it disappears
    brain.screen.print("Calibration Complete", Color.WHITE)
    wait(10, MSEC)
    drivetrain.set_turn_threshold(0.01) # Adjust the turn threshold for more precise turning (default is 1 degree)
    if not Inertial_sensor.installed(): # Check if the Inertial_sensor is connected and responding
        brain.screen.clear_screen(Color.RED)
        brain.screen.clear_line()
        brain.screen.print("FATAL ERROR: Inertial_sensor Sensor FAULTY not detected.", Color.WHITE)
        brain.screen.new_line()
        brain.screen.print("Please check the connection.", Color.WHITE)
        return
    # Inertial_sensor.gyro_rate(axis, units) 
    # Inertial_sensor.orientation(type, units) 
    Inertial_sensor.reset_rotation() # Reset the rotation of the Inertial_sensor
    Inertial_sensor.set_heading(0, DEGREES) # Set the robot's Inertial_sensor heading to zero


'''!!!NEVER CHANGE THESE LAST LINES!!!''''''!!!NEVER CHANGE THESE LAST LINES!!!''''''!!!NEVER CHANGE THESE LAST LINES!!!''''''!!!NEVER CHANGE THESE LAST LINES!!!''''''!!!NEVER CHANGE THESE LAST LINES!!!'''

'''!!!NEVER CHANGE THESE LAST LINES!!!''''''!!!NEVER CHANGE THESE LAST LINES!!!''''''!!!NEVER CHANGE THESE LAST LINES!!!''''''!!!NEVER CHANGE THESE LAST LINES!!!''''''!!!NEVER CHANGE THESE LAST LINES!!!'''

'''!!!NEVER CHANGE THESE LAST LINES!!!''''''!!!NEVER CHANGE THESE LAST LINES!!!''''''!!!NEVER CHANGE THESE LAST LINES!!!''''''!!!NEVER CHANGE THESE LAST LINES!!!''''''!!!NEVER CHANGE THESE LAST LINES!!!'''

'''!!!NEVER CHANGE THESE LAST LINES!!!''''''!!!NEVER CHANGE THESE LAST LINES!!!''''''!!!NEVER CHANGE THESE LAST LINES!!!''''''!!!NEVER CHANGE THESE LAST LINES!!!''''''!!!NEVER CHANGE THESE LAST LINES!!!'''

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
place_Holder(place_Holder_callback_0)
start_Calibration(start_Calibration_callback_0)
pre_auton()
# add 15ms delay to make sure events are registered correctly.
wait(15, MSEC)
