"""
Example: Full System Integration

Demonstrates the full brain-robot-controller system.
"""

import logging
import time
from brain_robot_controller import (
    BrainInterface,
    RobotController,
    CommandProcessor,
)

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)

print("Brain Robot Controller - Full System Demo")
print("=" * 60)

# Initialize components
print("\n1. Initializing components...")
brain_interface = BrainInterface()
robot_controller = RobotController()
command_processor = CommandProcessor(brain_interface, robot_controller)

# Setup callback for command execution
def on_command(command, success):
    status = "SUCCESS" if success else "FAILED"
    print(f"   Command '{command}' executed: {status}")

command_processor.set_command_callback(on_command)

# Connect brain interface
print("\n2. Connecting to brain signal device...")
if not brain_interface.connect():
    print("Failed to connect!")
    exit(1)

# Start robot controller
print("\n3. Starting robot controller...")
robot_controller.start()

# Start command processor
print("\n4. Starting command processing...")
if not command_processor.start_processing():
    print("Failed to start command processing!")
    exit(1)

# Run for a short duration
print("\n5. Processing brain signals for 5 seconds...")
print("   (In demo mode, commands are simulated)\n")

start_time = time.time()
command_count = 0

while time.time() - start_time < 5:
    if command_processor.process_next_signal():
        command_count += 1
    time.sleep(0.1)  # 10 Hz processing rate

print(f"\n6. Processed {command_count} commands in 5 seconds")

# Get system status
print("\n7. System status:")
status = command_processor.get_status()
print(f"   Processing: {status['is_processing']}")
print(f"   Brain Interface: {status['brain_interface_status']}")
print(f"   Robot Controller: {status['robot_controller_status']}")

# Cleanup
print("\n8. Shutting down...")
command_processor.stop_processing()
robot_controller.stop()
brain_interface.disconnect()

print("\n" + "=" * 60)
print("Full system demo complete!")
print("=" * 60)
