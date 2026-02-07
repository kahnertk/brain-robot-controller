"""Tests for RobotController class."""

import pytest
from brain_robot_controller import RobotController


class TestRobotController:
    """Test cases for RobotController."""
    
    def test_initialization(self):
        """Test controller initialization."""
        controller = RobotController()
        assert controller.is_running is False
        assert controller.current_state == "idle"
    
    def test_start_stop(self):
        """Test starting and stopping the controller."""
        controller = RobotController()
        
        # Test start
        controller.start()
        assert controller.is_running is True
        assert controller.current_state == "active"
        
        # Test stop
        controller.stop()
        assert controller.is_running is False
        assert controller.current_state == "idle"
    
    def test_move_forward(self):
        """Test forward movement."""
        controller = RobotController()
        
        # Should fail when not running
        assert controller.move_forward() is False
        
        # Should succeed when running
        controller.start()
        assert controller.move_forward(distance=2.0) is True
    
    def test_move_backward(self):
        """Test backward movement."""
        controller = RobotController()
        controller.start()
        assert controller.move_backward(distance=1.5) is True
    
    def test_turn_left(self):
        """Test left turn."""
        controller = RobotController()
        controller.start()
        assert controller.turn_left(degrees=90) is True
    
    def test_turn_right(self):
        """Test right turn."""
        controller = RobotController()
        controller.start()
        assert controller.turn_right(degrees=45) is True
    
    def test_execute_command(self):
        """Test command execution."""
        controller = RobotController()
        controller.start()
        
        # Test valid commands
        assert controller.execute_command("forward", distance=1.0) is True
        assert controller.execute_command("backward", distance=1.0) is True
        assert controller.execute_command("left", degrees=90) is True
        assert controller.execute_command("right", degrees=90) is True
        
        # Test invalid command
        assert controller.execute_command("invalid") is False
    
    def test_get_state(self):
        """Test getting controller state."""
        controller = RobotController()
        
        state = controller.get_state()
        assert "is_running" in state
        assert "current_state" in state
        assert state["is_running"] is False
        
        controller.start()
        state = controller.get_state()
        assert state["is_running"] is True
