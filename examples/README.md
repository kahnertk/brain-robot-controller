# Examples

This directory contains example scripts demonstrating different aspects of the Brain Robot Controller system.

## Available Examples

### 1. basic_control.py
Demonstrates basic robot control operations without brain interface.

**Usage:**
```bash
python examples/basic_control.py
```

**What it shows:**
- Initializing the robot controller
- Starting and stopping the controller
- Executing basic movement commands
- Getting robot state

### 2. brain_interface_demo.py
Shows how to work with the brain interface to read and process signals.

**Usage:**
```bash
python examples/brain_interface_demo.py
```

**What it shows:**
- Connecting to brain signal device
- Reading brain signals
- Processing signals to extract commands
- Getting interface status

### 3. full_system.py
Complete demonstration of all components working together.

**Usage:**
```bash
python examples/full_system.py
```

**What it shows:**
- Initializing all system components
- Setting up command callbacks
- Processing brain signals in real-time
- System status monitoring
- Proper shutdown sequence

## Running Examples

All examples can be run directly with Python:

```bash
# From the project root
python examples/<example_name>.py

# Or with Python module syntax
python -m examples.<example_name>
```

## Creating Your Own Examples

Feel free to create your own examples! Use these as templates for your specific use case.
