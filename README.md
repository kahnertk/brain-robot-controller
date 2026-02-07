# Brain Robot Controller

> Hack-Nation AI Hackathon Challenge

A Python-based system for controlling robots using brain signals and AI. This project provides a framework for processing brain signals (e.g., from EEG devices) and translating them into robot control commands.

## 🚀 Features

- **Brain Interface**: Connect to and process brain signal devices
- **Robot Controller**: Manage robot movements and actions
- **Command Processor**: Bridge between brain signals and robot commands
- **Configurable**: Easy-to-customize configuration system
- **Extensible**: Modular architecture for easy expansion
- **Well-Tested**: Comprehensive test suite included

## 📋 Requirements

- Python 3.8 or higher
- No external dependencies required for basic functionality

### Optional Dependencies

For enhanced functionality, you can install optional dependencies:

```bash
# For machine learning-based signal processing
pip install -e ".[ml]"

# For hardware integration
pip install -e ".[hardware]"

# For development
pip install -e ".[dev]"
```

## 🔧 Installation

### Basic Installation

```bash
# Clone the repository
git clone https://github.com/kahnertk/brain-robot-controller.git
cd brain-robot-controller

# Install the package
pip install -e .
```

### Development Installation

```bash
# Install with development dependencies
pip install -e ".[dev]"
```

## 🎯 Quick Start

### Running the Demo

Run the demo mode to see the system in action with simulated brain signals:

```bash
# Run for 10 seconds (default)
python -m brain_robot_controller.main --mode demo

# Run for 30 seconds with debug logging
python -m brain_robot_controller.main --mode demo --duration 30 --log-level DEBUG
```

### Using as a Library

```python
from brain_robot_controller import (
    BrainInterface,
    RobotController,
    CommandProcessor,
)

# Initialize components
brain = BrainInterface()
robot = RobotController()
processor = CommandProcessor(brain, robot)

# Connect and start
brain.connect()
robot.start()
processor.start_processing()

# Process signals
processor.process_next_signal()

# Cleanup
processor.stop_processing()
robot.stop()
brain.disconnect()
```

## 📖 Examples

The `examples/` directory contains several demonstration scripts:

### Basic Robot Control

```bash
python examples/basic_control.py
```

Demonstrates basic robot movements without brain interface.

### Brain Interface Demo

```bash
python examples/brain_interface_demo.py
```

Shows how to read and process brain signals.

### Full System Integration

```bash
python examples/full_system.py
```

Complete demonstration of the entire system working together.

## 🧪 Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=brain_robot_controller --cov-report=html

# Run specific test file
pytest tests/test_controller.py
```

## 🏗️ Architecture

The system consists of three main components:

### 1. Brain Interface (`BrainInterface`)

- Connects to brain signal devices (e.g., EEG)
- Reads and buffers signals
- Processes signals to extract commands
- Supports both simulated and real devices

### 2. Robot Controller (`RobotController`)

- Manages robot state and operations
- Executes movement commands (forward, backward, left, right)
- Provides safety controls and state monitoring
- Extensible for different robot platforms

### 3. Command Processor (`CommandProcessor`)

- Bridges brain interface and robot controller
- Processes signals in real-time
- Applies command filtering and debouncing
- Provides callback mechanism for monitoring

## ⚙️ Configuration

Configuration is managed through `brain_robot_controller/config.py`:

```python
from brain_robot_controller.config import Config

# View current configuration
config = Config.get_config()

# Update configuration
Config.update_config({
    "robot_controller": {
        "movement_speed": 2.0,
        "turn_speed": 60.0,
    }
})
```

### Configuration Sections

- **brain_interface**: Device settings, sampling rate, channels
- **robot_controller**: Movement speeds, safety distances
- **command_processor**: Processing rate, thresholds
- **logging**: Log level and format

## 🤝 Contributing

This is a hackathon project. Contributions, ideas, and improvements are welcome!

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 Development

### Code Quality

The project uses several tools for code quality:

```bash
# Format code with black
black brain_robot_controller tests examples

# Lint with flake8
flake8 brain_robot_controller tests examples

# Type checking with mypy
mypy brain_robot_controller
```

### Project Structure

```
brain-robot-controller/
├── brain_robot_controller/    # Main package
│   ├── __init__.py
│   ├── brain_interface.py     # Brain signal interface
│   ├── controller.py          # Robot controller
│   ├── command_processor.py   # Command processing
│   ├── config.py              # Configuration
│   └── main.py                # CLI entry point
├── tests/                     # Test suite
│   ├── test_controller.py
│   ├── test_brain_interface.py
│   └── test_command_processor.py
├── examples/                  # Example scripts
│   ├── basic_control.py
│   ├── brain_interface_demo.py
│   └── full_system.py
├── pyproject.toml            # Project metadata
├── requirements.txt          # Dependencies
└── README.md                 # This file
```

## 🎓 Hackathon Challenge

This project was created for the Hack-Nation AI Hackathon. The challenge involves:

- Processing brain signals in real-time
- Implementing intelligent robot control
- Creating a robust and extensible architecture
- Demonstrating practical applications of brain-computer interfaces

## 📄 License

MIT License - Feel free to use this project for learning and development!

## 🙏 Acknowledgments

- Hack-Nation AI Hackathon organizers
- Brain-computer interface research community
- Open source robotics community

## 📧 Contact

For questions or feedback about this hackathon project, please open an issue on GitHub.
