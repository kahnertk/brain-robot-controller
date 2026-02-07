"""
Robot Controller Module

Provides the main controller class for managing robot operations.
"""

import logging
from typing import Dict, Any, Optional

logger = logging.getLogger(__name__)


class RobotController:
    """
    Main controller class for the robot.
    
    This class manages robot state, processes commands, and coordinates
    between brain signals and robot actions.
    """
    
    def __init__(self, config: Optional[Dict[str, Any]] = None):
        """
        Initialize the robot controller.
        
        Args:
            config: Configuration dictionary for the robot controller
        """
        self.config = config or {}
        self.is_running = False
        self.current_state = "idle"
        logger.info("RobotController initialized")
    
    def start(self):
        """Start the robot controller."""
        self.is_running = True
        self.current_state = "active"
        logger.info("Robot controller started")
    
    def stop(self):
        """Stop the robot controller."""
        self.is_running = False
        self.current_state = "idle"
        logger.info("Robot controller stopped")
    
    def move_forward(self, distance: float = 1.0):
        """
        Move the robot forward.
        
        Args:
            distance: Distance to move (in meters)
        """
        if not self.is_running:
            logger.warning("Cannot move: controller not running")
            return False
        
        logger.info(f"Moving forward {distance}m")
        # Actual robot movement would be implemented here
        return True
    
    def move_backward(self, distance: float = 1.0):
        """
        Move the robot backward.
        
        Args:
            distance: Distance to move (in meters)
        """
        if not self.is_running:
            logger.warning("Cannot move: controller not running")
            return False
        
        logger.info(f"Moving backward {distance}m")
        # Actual robot movement would be implemented here
        return True
    
    def turn_left(self, degrees: float = 90.0):
        """
        Turn the robot left.
        
        Args:
            degrees: Degrees to turn
        """
        if not self.is_running:
            logger.warning("Cannot turn: controller not running")
            return False
        
        logger.info(f"Turning left {degrees} degrees")
        # Actual robot turning would be implemented here
        return True
    
    def turn_right(self, degrees: float = 90.0):
        """
        Turn the robot right.
        
        Args:
            degrees: Degrees to turn
        """
        if not self.is_running:
            logger.warning("Cannot turn: controller not running")
            return False
        
        logger.info(f"Turning right {degrees} degrees")
        # Actual robot turning would be implemented here
        return True
    
    def execute_command(self, command: str, **kwargs):
        """
        Execute a command on the robot.
        
        Args:
            command: Command name (e.g., "forward", "backward", "left", "right")
            **kwargs: Additional arguments for the command
        """
        command_map = {
            "forward": self.move_forward,
            "backward": self.move_backward,
            "left": self.turn_left,
            "right": self.turn_right,
        }
        
        if command in command_map:
            return command_map[command](**kwargs)
        else:
            logger.error(f"Unknown command: {command}")
            return False
    
    def get_state(self) -> Dict[str, Any]:
        """
        Get the current state of the robot.
        
        Returns:
            Dictionary containing robot state information
        """
        return {
            "is_running": self.is_running,
            "current_state": self.current_state,
        }
