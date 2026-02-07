"""Tests for CommandProcessor class."""

import pytest
from brain_robot_controller import (
    BrainInterface,
    RobotController,
    CommandProcessor,
)


class TestCommandProcessor:
    """Test cases for CommandProcessor."""
    
    def test_initialization(self):
        """Test command processor initialization."""
        brain = BrainInterface()
        robot = RobotController()
        processor = CommandProcessor(brain, robot)
        
        assert processor.is_processing is False
        assert processor.brain_interface is brain
        assert processor.robot_controller is robot
    
    def test_set_command_callback(self):
        """Test setting command callback."""
        brain = BrainInterface()
        robot = RobotController()
        processor = CommandProcessor(brain, robot)
        
        callback_called = False
        
        def callback(command, success):
            nonlocal callback_called
            callback_called = True
        
        processor.set_command_callback(callback)
        assert processor.command_callback is callback
    
    def test_start_processing(self):
        """Test starting command processing."""
        brain = BrainInterface()
        robot = RobotController()
        processor = CommandProcessor(brain, robot)
        
        # Should fail when components not ready
        assert processor.start_processing() is False
        
        # Should succeed when components ready
        brain.connect()
        robot.start()
        assert processor.start_processing() is True
        assert processor.is_processing is True
    
    def test_stop_processing(self):
        """Test stopping command processing."""
        brain = BrainInterface()
        robot = RobotController()
        processor = CommandProcessor(brain, robot)
        
        brain.connect()
        robot.start()
        processor.start_processing()
        
        processor.stop_processing()
        assert processor.is_processing is False
    
    def test_process_next_signal(self):
        """Test processing signals."""
        brain = BrainInterface()
        robot = RobotController()
        processor = CommandProcessor(brain, robot)
        
        # Should return False when not processing
        assert processor.process_next_signal() is False
        
        # Start components
        brain.connect()
        robot.start()
        processor.start_processing()
        
        # Should process (may or may not find a command)
        result = processor.process_next_signal()
        assert isinstance(result, bool)
    
    def test_get_status(self):
        """Test getting processor status."""
        brain = BrainInterface()
        robot = RobotController()
        processor = CommandProcessor(brain, robot)
        
        status = processor.get_status()
        assert "is_processing" in status
        assert "brain_interface_status" in status
        assert "robot_controller_status" in status
        assert status["is_processing"] is False
