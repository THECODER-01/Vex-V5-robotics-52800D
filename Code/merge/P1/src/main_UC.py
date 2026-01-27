from vex import *
brain=Brain()
controller_1 = Controller(PRIMARY)
left_motor_f = Motor(Ports.PORT1, GearSetting.RATIO_18_1, False)
left_motor_b = Motor(Ports.PORT11, GearSetting.RATIO_18_1, False)
left_motors = MotorGroup(left_motor_f, left_motor_b)
right_motor_f = Motor(Ports.PORT9, GearSetting.RATIO_18_1, True)
right_motor_b = Motor(Ports.PORT20, GearSetting.RATIO_18_1, True)
right_motors = MotorGroup(right_motor_f, right_motor_b)
gps_sensor = Gps(brain.three_wire_port.h)
gps_sensor.calibrate()
gps_sensor.quality(100)
drivetrain = SmartDrive(left_motors, right_motors, gps_sensor, 101.6, 317.5, 431.8, MM, 1)
left_power = controller_1.axis3.position()
right_power = controller_1.axis2.position() # Or axis3 and axis4 for specific styles
calibrate_drivetrain()
motor_12 = Motor(Ports.PORT12, GearSetting.RATIO_18_1, False)
motor_13 = Motor(Ports.PORT13, GearSetting.RATIO_18_1, False)
motor_14 = Motor(Ports.PORT14, GearSetting.RATIO_18_1, False)
pneumatic_flap = Pneumatics(brain.three_wire_port.f)
bumper_a = Bumper(brain.three_wire_port.a)
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
myVariable = 0
S = 0
Automonus = Event()
def Automonus_callback_0():
    global myVariable, S, Automonus, Bottom, Top, O12B, Bottom, O12F, O12S, AStop, PH, PL, PM, Keep_Code
    if bumper_a.pressing():
        drivetrain.drive_for(FORWARD, 400, MM)
        drivetrain.turn_for(RIGHT, 90, DEGREES)
        drivetrain.drive_for(FORWARD, 756, MM)
        drivetrain.turn_for(LEFT, 90, DEGREES)
        drivetrain.drive_for(FORWARD, 250, MM, wait=False)
        AUTOP.broadcast()
        wait(8, SECONDS)
    else:
        drivetrain.drive_for(FORWARD, 400, MM)
        drivetrain.turn_for(LEFT, 90, DEGREES)
        drivetrain.drive_for(FORWARD, 756, MM)
        drivetrain.turn_for(RIGHT, 90, DEGREES)
        drivetrain.drive_for(FORWARD, 250, MM, wait=False)
        AUTOP.broadcast()
        wait(8, SECONDS)
def onauton_autonomous_0():
    global myVariable, S, Automonus, Bottom, Top, O12B, Bottom, O12F, O12S, AStop, PH, PL, PM, Keep_Code
    drivetrain.set_drive_velocity(46, PERCENT)
    drivetrain.set_turn_velocity(46, PERCENT)
    motor_12.set_velocity(120, PERCENT)
    motor_13.set_velocity(120, PERCENT)
    motor_14.set_velocity(120, PERCENT)
    pneumatic_flap.close()
    pneumatic_flap.open()
    Automonus.broadcast()
def ondriver_drivercontrol_0():
    global Bottom, Top, O12B, Bottom, O12F, O12S, AStop, PH, PL, PM, Keep_Code
    pneumatic_flap.close()
    pneumatic_flap.open()
    drivetrain.set_drive_velocity(80, PERCENT)
    drivetrain.set_turn_velocity(80, PERCENT)
    motor_12.set_velocity(120, PERCENT)
    motor_13.set_velocity(120, PERCENT)
    motor_14.set_velocity(120, PERCENT)
    while True:
        left_motors.spin(FORWARD, left_power, PERCENT)
        right_motors.spin(FORWARD, right_power, PERCENT)
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
def Bottom_callback_0():
    global Bottom, Top, O12B, Bottom, O12F, O12S, AStop, PH, PL, PM, Keep_Code
    motor_13.spin(REVERSE)
    motor_14.stop()
def O12F_callback_0():
    global Bottom, Top, O12B, Bottom, O12F, O12S, AStop, PH, PL, PM, Keep_Code
    motor_12.spin(FORWARD)
def O12S_callback_0():
    global Bottom, Top, O12B, Bottom, O12F, O12S, AStop, PH, PL, PM, Keep_Code
    motor_12.stop()
def O12B_callback_0():
    global Bottom, Top, O12B, Bottom, O12F, O12S, AStop, PH, PL, PM, Keep_Code
    motor_12.spin(REVERSE)
def AStop_callback_0():
    global Bottom, Top, O12B, Bottom, O12F, O12S, AStop, PH, PL, PM, Keep_Code
    motor_12.stop()
    motor_13.stop()
    motor_14.stop()
def PH_callback_0():
    global Bottom, Top, O12B, Bottom, O12F, O12S, AStop, PH, PL, PM, Keep_Code
    pneumatic_flap.open()
    wait(0.3, SECONDS)
def PL_callback_0():
    global Bottom, Top, O12B, Bottom, O12F, O12S, AStop, PH, PL, PM, Keep_Code
    pneumatic_flap.close()
    wait(0.3, SECONDS)
def Keep_Code_callback_0():
    global Bottom, Top, O12B, Bottom, O12F, O12S, AStop, PH, PL, PM, Keep_Code
    motor_12.spin(FORWARD)
    motor_13.spin(FORWARD)
    motor_14.stop()
def AUTOP_callback_0():
    global Bottom, Top, O12B, Bottom, O12F, O12S, AStop, PH, PL, PM, Keep_Code
    motor_12.spin(FORWARD)
    motor_13.spin(FORWARD)
    motor_14.spin(FORWARD)
def vexcode_auton_function():
    auton_task_0 = Thread( onauton_autonomous_0 )
    while( competition.is_autonomous() and competition.is_enabled() ):
        wait( 10, MSEC )
    auton_task_0.stop()
def vexcode_driver_function():
    driver_control_task_0 = Thread( ondriver_drivercontrol_0 )
    while( competition.is_driver_control() and competition.is_enabled() ):
        wait( 10, MSEC )
    driver_control_task_0.stop()
competition = Competition( vexcode_driver_function, vexcode_auton_function )
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
wait(15, MSEC)