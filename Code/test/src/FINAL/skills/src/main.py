# ---------------------------------------------------------------------------- #
#                                                                              #
# 	Module:       main.py                                                      #
# 	Author:       Nolan N                                                      #
# 	Description:  V5 project (R2.D2)  V.Latest  V.skills                       #
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
IMPORTNAT NOTES:
- IF ANY PORTS BURN OUT OR CHANGE, UPDATE THE PORT NUMBERS IN THE FOLLOWING LINES TO MATCH THE NEW CONFIGURATION:
    - 36-37:: left motors, DEFAULT: PORT1, PORT11
    - 44-45:: right motors, DEFAULT: PORT9, PORT20
    - 65-72:: intake and goal motors, DEFAULT: intake-motor_PORT12, middle/top-goal-motor_PORT13, jail-motor_PORT14
    - 80:: pneumatic flap, DEFAULT: three_wire_port.f
    - 
- IMPORTANT: DO NOT CHANGE THE PORT NUMBERS IN THE PREVIOUS LINES UNTIL YOU FIRST UPDATE THE CABLES ON THE ROBOT TO MATCH THE NEW PORT NUMBERS AND TEST THEM.
- IMPORTANT LINES FOR DRIVER CONTROL CODE:
    - 312-354:: Driver control loop: controller input reading and button control
    - 356-362:: Top goal: button L1
    - 363-369:: Bottom goal: button L2
    - 370-387:: Intake: button R1 (start), R2 (stop), Y (reverse)
    - 388-395:: All motors stop: button B
    - 396-409:: Pneumatic flap open/close: button Right/Left
    - 410-417:: Keep_Code: button X
'''

# Brain should be defined by default
brain=Brain()

# Define Primary Controller (  Add Controller 2 if needed with: controller_2 = Controller(PARTNER)  )
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
# brain_inertial = Inertial(brain.three_wire_port.h)
# (Optional) Create an Gyro Sensor for a SmartDrive
#Gyro_sensor = None # Gyro(brain.three_wire_port.h)
# Gyro_sensor.quality(100)

# Construct a 4-Motor Drivetrain (SmartDrive is used with an Inertial Sensor)
# The values (wheel travel, track width, etc.) should be adjusted for your specific robot
#drivetrain = SmartDrive(left_motors, right_motors, 319.19, 309.88, 317.5, MM, 1)
drivetrain = DriveTrain(left_motors, right_motors, 319.19, 309.88, 317.5, MM, 1)

# Example usage:
# drivetrain.drive_for(FORWARD, 12, INCHES)

# Calibrate the drivetrain
# calibrate_drivetrain()

# intake motor
motor_12 = Motor(Ports.PORT12, GearSetting.RATIO_18_1, False)

# Middle/top goal motor
motor_13 = Motor(Ports.PORT13, GearSetting.RATIO_18_1, False)

# jail motor
motor_14 = Motor(Ports.PORT14, GearSetting.RATIO_18_1, False)

# Define a 3-wire digital output on port F
# Supported ports are Brain.three_wire_port.a through h
# pneumatic_flap = DigitalOut(brain.three_wire_port.f)

# Define a 3-wire digital output Pneumatic on port F
pneumatic_flap = Pneumatics(brain.three_wire_port.f)

# Define a 3-wire Bumper on port A
# bumper_a = Bumper(brain.three_wire_port.a)

# To set the device to high (on)
#pneumatic_flap.set(True)

# To set the device to low (off)
#pneumatic_flap.set(False)

#1_1_2 = Motor(Ports.PORT10, GearSetting.RATIO_18_1, True)

# Get joystick values (Axis 3 for forward/reverse, Axis 1 for turning)
# You can also use other axes for arcade or split arcade control
# left_power = controller_1.axis3.position()
# right_power = controller_1.axis2.position() # Or axis3 and axis4 for specific styles
# add something here

'''!!!DON'T CHANGE THE NEXT 35 LINES UNLESS YOU KNOW WHAT YOU'RE DOING!!!'''
time01 = 0 #adds 1 every 8 milliseconds in the pre-autonomous loop to allow for a timer to be used for autonomous mode selection and other time-based functions during the pre-autonomous period

# Default Autonomous mode for pre-autonomous period. Initial value:: 3: skills
A01 = 3

# Autonomous mode selection time variable for pre-autonomous period. Initial value:: 1:3000 (24 seconds)
T = 80

# Autonomous movement distances (in mm) for skills. Initial values:: 1:600, 2:300

# Autonomous movement distances (in mm) for both left and right for top goal. Initial values:: 1:400, 2:756, 3:250
auto_at_start = None # Set to False to disable the autonomous code in the Automonus event

ND1 = 45
ND2 = 46
NF1 = 400
NF2 = 780
NF3 = 230

Top = Event()
O12B = Event()
Bottom = Event()
O12F = Event()
O12S = Event()
AStop = Event()
PH = Event()
PL = Event()
Keep_Code = Event()
AUTOP = Event()
Automonus = Event()
place_Holder = Event()

#result1 = start_a00(a=1, b="Calibration Complete")
#result0 = start_a00(a=-1, b="Calibration Complete")
'''!!!DON'T CHANGE THE PREVIOUS 35 LINES UNLESS YOU KNOW WHAT YOU'RE DOING!!!'''


'''  !!!  ALL MAIN FUNCTIONS, EVENTS, AND CODE FOR OUR ROBOT ARE BELOW THIS LINE  !!!  '''


'''
    !!! IGNORE THE ALL FOLLOWING LINES IN THE NEXT 3 FUNCTIONS BELOW UNLESS: !!!
    - YOU KNOW WHAT THEY DO
    - WANT TO CHANGE: autonomous movement functions or the pre-autonomous events

    - !!! OR WANT KILL OUR CHANCES FOR STATES !!!

'''

def start_a00(a, b):
    global A01
    A01= A01 + a
    if A01 == 0:
        return "Autonomous Disabled :: " + b
    if A01 == 1:
        return "Autonomous Left :: " + b
    if A01 == 2:
        return "Autonomous Right :: " + b
    if A01 == 3:
        return "Autonomous Skills :: " + b
    if A01 == 4:
        A01= 0
        return "Autonomous Disabled :: " + b
    if A01 == -1:
        A01= 3
        return "Autonomous Skills :: " + b
    
def drive00(dNF1, drive00d1, dND1, dNF2, drive00d2, dND2, dNF3):
    drivetrain.drive_for(FORWARD, dNF1, MM, wait=True)
    drivetrain.turn_for(drive00d1, dND1, DEGREES, wait=True)
    drivetrain.drive_for(FORWARD, dNF2, MM, wait=True)
    drivetrain.turn_for(drive00d2, dND2, DEGREES, wait=True)
    drivetrain.drive_for(FORWARD, dNF3, MM, wait=False)

def pre_auton():
    global time01, A01, auto_at_start
    '''
    !!! IGNORE THE ALL FOLLOWING RED LINES IN THIS FUNCTION UNLESS: !!!
    - YOU KNOW WHAT THEY DO
    - WANT TO CHANGE THE CALIBRATION PROCESS

    - !! OR WANT KILL OUR CHANCES FOR STATES !!    
    
    drivetrain.set_turn_threshold(0.01) # Adjust the turn threshold for more precise turning (default is 1 degree)
    # Calibrate the Gyro_sensor Sensor
    brain.screen.print("Calibrating Gyro_sensor Sensor...")
    Gyro_sensor.calibrate() # Calibrates the sensor
    while Gyro_sensor.is_calibrating():
        sleep(50) # Wait for calibration to complete
    brain.screen.clear_screen(Color.BLACK)
    brain.screen.clear_line()
    wait(10, MSEC) # Short delay after clear screen to ensure the message is visible before it disappears
    brain.screen.print("Calibration Complete")
    wait(80, MSEC)
    drivetrain.set_turn_threshold(0.01) # Adjust the turn threshold for more precise turning (default is 1 degree)
    Gyro_sensor.set_heading(0.1) # Set a small non-zero heading to ensure the sensor is responding and to prevent issues with a zero heading
    if Gyro_sensor.heading() == 0 or Gyro_sensor.heading() < 0: # Check if the Gyro_sensor is connected and responding
        brain.screen.clear_screen(Color.RED)
        brain.screen.clear_line()
        brain.screen.print("FATAL ERROR: Gyro_sensor Sensor FAULTY not detected.", Color.WHITE)
        brain.screen.new_line()
        brain.screen.print("Please check the connection.", Color.WHITE)
        return
    Gyro_sensor.set_heading(0, DEGREES) # Set the robot's Gyro_sensor heading to zero
    # drivetrain.turn_for(self, direction, angle, units=RotationUnits.DEG, velocity=None, units_v:VelocityPercentUnits=VelocityUnits.RPM, wait=True)
    # drivetrain.turn_to_heading(self, angle, units=RotationUnits.DEG, velocity=None, units_v:VelocityPercentUnits=VelocityUnits.RPM, wait=True)
    # drivetrain.turn_for(self, angle, units=RotationUnits.DEG, velocity=None, units_v:VelocityPercentUnits=VelocityUnits.RPM, wait=True)
    # drivetrain.set_turn_threshold(self, value)
    # drivetrain.set_turn_constant(self, value)
    '''
    brain.screen.print("DON'T PRESS ANYTHING") # Press Up/Down to select Autonomous Mode'
    brain.screen.new_line()
    brain.screen.print(start_a00(a=0, b="Calibration Complete"))
    while time01 < T: # Allow 'T' seconds for the user to see the calibration complete message before it disappears
        '''
        if controller_1.buttonUp.pressing():
            brain.screen.clear_screen(Color.BLACK)
            wait(5, MSEC) # Short delay after clear screen to ensure the message is visible before it disappears
            brain.screen.new_line()
            brain.screen.print(start_a00(a=1, b="Calibration Complete"))
        if controller_1.buttonDown.pressing():
            brain.screen.clear_screen(Color.BLACK)
            wait(5, MSEC) # Short delay after clear screen to ensure the message is visible before it disappears
            brain.screen.new_line()
            brain.screen.print(start_a00(a=-1, b="Calibration Complete"))
        '''
        if A01 == 0: # Autonomous Disabled
            auto_at_start = False
        if A01 == 1: # Autonomous Left
            auto_at_start = True
        if A01 == 2: # Autonomous Right
            auto_at_start = True
        if A01 == 3: # Autonomous Skills
            auto_at_start = True
        if A01 == 4: # ERROR: This case should never be reached due to the reset in the start_a00 function, but is included as a safety measure
            A01= 0
            auto_at_start = False
        if A01 == -1: # ERROR: This case should never be reached due to the reset in the start_a00 function, but is included as a safety measure
            A01= 3
            auto_at_start = True
        wait(100, MSEC) # Check every 100 milliseconds
        time01 = time01 + 1
        # pre_autonomous control function above


'''
!MAIN AUTONOMOUS SETUP CODE BELOW!
- This code sets ups the autonomous period constants and initial conditions and runs the autonomous code during the autonomous period.
- You can also use this section to setup any code that should be active during the autonomous period.
'''
def onauton_autonomous_0():
    global Automonus, Bottom, Top, O12B, O12F, O12S, AStop, PH, PL, place_Holder, Keep_Code
    # \/ Autonomous SETUP code here \/
    drivetrain.set_drive_velocity(48, PERCENT)
    drivetrain.set_turn_velocity(48, PERCENT)
    motor_12.set_velocity(120, PERCENT)
    motor_13.set_velocity(120, PERCENT)
    motor_14.set_velocity(120, PERCENT)
    pneumatic_flap.open() # Intentional: close then open quickly to straighten the flap and move any linked parts into their starting positions
    pneumatic_flap.close() # Intentional: close then open quickly to straighten the flap and move any linked parts into their starting positions
    Automonus.broadcast() # Broadcast to the MAIN Automonus code to start


'''
!!!MAIN AUTONOMOUS CODE BELOW!!!
- This code runs (!!NOT IN A LOOP!!) during the autonomous period and is where you will control your robot's autonomous actions based on the selected autonomous mode and any time-based functions you want to use.
- You can also use this section to run any code that should be active during the autonomous period.
'''
def Automonus_callback_0():
    global Automonus, Bottom, Top, O12B, O12F, O12S, AStop, PH, PL, place_Holder, Keep_Code, auto_at_start, A01, NF1, NF2, NF3, SF1, SB1
    if auto_at_start == True:
        if A01 == 2:
            # right side
            drive00(NF1, RIGHT, ND1, NF2, LEFT, ND2, NF3)
            AUTOP.broadcast()
            # Intake on
            # Top goal
            wait(4, SECONDS)
        if A01 == 1:
            # left side
            drive00(NF1, LEFT, ND1, NF2, RIGHT, ND2, NF3)
            AUTOP.broadcast()
            # Intake on
            # Top goal
            wait(4, SECONDS)
        if A01 == 3:
            drive00(NF1, RIGHT, ND1, NF2, LEFT, ND2, NF3)
            AUTOP.broadcast()
            wait(5, SECONDS)
            drivetrain.drive_for(REVERSE, 450, MM, wait=True)
            drivetrain.turn_for(RIGHT, 40, DEGREES, wait=False)
            wait(2, SECONDS)
            drivetrain.set_turn_velocity(100, PERCENT)
            drivetrain.drive_for(REVERSE, 1600, MM, wait=True, velocity=100)
            AUTOP.broadcast()
            # skills
    else: # If auto_at_start is False, skip the autonomous code and do nothing in the Automonus event
        return


'''
!!!MAIN DRIVER CONTROL CODE IN FUNCTION BELOW!!!
- This code runs in a loop during the driver control period and is where you will read controller inputs and control your robot accordingly.
- You can also use this section to run any code that should be active during the driver control period.
'''
def ondriver_drivercontrol_0():
    global Bottom, Top, O12B, O12F, O12S, AStop, PH, PL, place_Holder, Keep_Code

    # \/ MAIN drivercontrol code SETUP code here \/
    pneumatic_flap.open() # Intentional: close then open quickly to straighten the flap and move any linked parts into their starting positions
    pneumatic_flap.close() # Intentional: close then open quickly to straighten the flap and move any linked parts into their starting positions
    drivetrain.set_drive_velocity(80, PERCENT)
    drivetrain.set_turn_velocity(80, PERCENT)
    motor_12.set_velocity(120, PERCENT)
    motor_13.set_velocity(120, PERCENT)
    motor_14.set_velocity(120, PERCENT)

    # \/ MAIN drivercontrol code here \/
    while True:
        # \/ Read controller axes each loop so values update continuously (You can also use other axes for arcade or split arcade control) \/
        left_power = controller_1.axis3.position() # Get joystick values and use axis3 for left power
        right_power = controller_1.axis2.position()  # Get joystick values and use axis2 for right power
        left_motors.spin(FORWARD, left_power, PERCENT) # Spin motor groups based on controller input
        right_motors.spin(FORWARD, right_power, PERCENT) # Spin motor groups based on controller input

        # \/ Button controls for motors and pneumatics + events \/
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
        
        # \/ A very small delay to prevent runaway errors and allow for more responsive controls \/
        wait(5, MSEC)


def Top_callback_0():
    global Bottom, Top, O12B, O12F, O12S, AStop, PH, PL, place_Holder, Keep_Code
    motor_13.spin(FORWARD)
    motor_14.spin(FORWARD)
    # Top goal
    # button: L1

def Bottom_callback_0():
    global Bottom, Top, O12B, O12F, O12S, AStop, PH, PL, place_Holder, Keep_Code
    motor_13.spin(REVERSE)
    motor_14.stop()
    # Bottom goal
    # button: L2

def O12F_callback_0():
    global Bottom, Top, O12B, O12F, O12S, AStop, PH, PL, place_Holder, Keep_Code
    motor_12.spin(FORWARD)
    # This only moves M12
    # button: R1

def O12S_callback_0():
    global Bottom, Top, O12B, O12F, O12S, AStop, PH, PL, place_Holder, Keep_Code
    motor_12.stop()
    # This only stops M12
    # button: R2

def O12B_callback_0():
    global Bottom, Top, O12B, O12F, O12S, AStop, PH, PL, place_Holder, Keep_Code
    motor_12.spin(REVERSE)
    # This only moves M12
    # button: Y

def AStop_callback_0():
    global Bottom, Top, O12B, O12F, O12S, AStop, PH, PL, place_Holder, Keep_Code
    motor_12.stop()
    motor_13.stop()
    motor_14.stop()
    # This stops All motors
    # button: B

def PH_callback_0():
    global Bottom, Top, O12B, O12F, O12S, AStop, PH, PL, place_Holder, Keep_Code
    pneumatic_flap.open()
    wait(0.3, SECONDS)
    # Pneumatic High/open (Goal)
    # button: Right

def PL_callback_0():
    global Bottom, Top, O12B, O12F, O12S, AStop, PH, PL, place_Holder, Keep_Code
    pneumatic_flap.close()
    wait(0.3, SECONDS)
    # Pneumatic Low/close (Jail)
    # button: Left

def Keep_Code_callback_0():
    global Bottom, Top, O12B, O12F, O12S, AStop, PH, PL, place_Holder, Keep_Code
    motor_12.spin(FORWARD)
    motor_13.spin(FORWARD)
    motor_14.stop()
    # Keep_Code
    # button: X

def AUTOP_callback_0():
    global Bottom, Top, O12B, O12F, O12S, AStop, PH, PL, place_Holder, Keep_Code
    motor_12.spin(FORWARD)
    motor_13.spin(FORWARD)
    motor_14.spin(FORWARD)
    # For auntom code

def place_Holder_callback_0():
    global Bottom, Top, O12B, O12F, O12S, AStop, PH, PL, place_Holder, Keep_Code
    # This is a place holder for any future events or code you may want to add
    # You can also use this event for testing or development purposes with out being tied to a specific button or action
    pass


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
Top(Top_callback_0)
PL(PL_callback_0)
O12F(O12F_callback_0)
Bottom(Bottom_callback_0)
O12B(O12B_callback_0)
PH(PH_callback_0)
O12S(O12S_callback_0)
Keep_Code(Keep_Code_callback_0)
AStop(AStop_callback_0)
AUTOP(AUTOP_callback_0)
place_Holder(place_Holder_callback_0)

pre_auton()
# add 15ms delay to make sure events are registered correctly.
wait(15, MSEC)
