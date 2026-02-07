"""Test initialization - ensures package is importable."""

import brain_robot_controller


def test_package_import():
    """Test that the package can be imported."""
    assert brain_robot_controller is not None


def test_version():
    """Test that version is defined."""
    assert hasattr(brain_robot_controller, "__version__")
    assert brain_robot_controller.__version__ == "0.1.0"


def test_public_api():
    """Test that public API is available."""
    assert hasattr(brain_robot_controller, "RobotController")
    assert hasattr(brain_robot_controller, "BrainInterface")
    assert hasattr(brain_robot_controller, "CommandProcessor")
