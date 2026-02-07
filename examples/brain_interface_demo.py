"""
Example: Brain Interface Demo

Demonstrates the brain interface for reading and processing signals.
"""

import logging
import time
from brain_robot_controller import BrainInterface

# Setup logging
logging.basicConfig(level=logging.INFO)

# Create brain interface
brain = BrainInterface()

print("Brain Interface Demo")
print("=" * 50)

# Connect to the brain signal device
print("\nConnecting to brain signal device...")
if brain.connect():
    print("Successfully connected!")
    
    # Read and process some signals
    print("\nReading signals...")
    for i in range(5):
        signal = brain.read_signal()
        if signal:
            print(f"\nSignal {i+1}:")
            print(f"  Timestamp: {signal['timestamp']}")
            print(f"  Channels: {len(signal['channels'])}")
            print(f"  Quality: {signal['quality']}")
            
            # Process the signal
            command = brain.process_signal(signal)
            if command:
                print(f"  Detected command: {command}")
            else:
                print("  No command detected")
        
        time.sleep(0.5)
    
    # Get status
    status = brain.get_status()
    print(f"\nBrain interface status: {status}")
    
    # Disconnect
    print("\nDisconnecting...")
    brain.disconnect()
    print("Disconnected successfully!")
else:
    print("Failed to connect to brain signal device")

print("\nExample complete!")
