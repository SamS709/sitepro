from pyniryo2 import *

ned = NiryoRobot("10.10.10.10")

ned.arm.calibrate_auto()

ned.arm.move_joints([0.2, -0.3, 0.1, 0.0, 0.5, -0.8])