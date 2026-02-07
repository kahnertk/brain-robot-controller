"""
Example: Basic Robot Control

Demonstrates basic robot control without brain interface.
"""

import logging
from brain_robot_controller import RobotController

# Setup logging
logging.basicConfig(level=logging.INFO)

# Create robot controller
controller = RobotController()

# Start the controller
print("Starting robot controller...")
controller.start()

# Execute some basic commands
print("\nExecuting commands:")
print("- Moving forward...")
controller.move_forward(distance=2.0)

print("- Turning right...")
controller.turn_right(degrees=90)

print("- Moving forward...")
controller.move_forward(distance=1.5)

print("- Turning left...")
controller.turn_left(degrees=45)

print("- Moving backward...")
controller.move_backward(distance=1.0)

# Get robot state
state = controller.get_state()
print(f"\nRobot state: {state}")

# Stop the controller
print("\nStopping robot controller...")
controller.stop()

print("Example complete!")
