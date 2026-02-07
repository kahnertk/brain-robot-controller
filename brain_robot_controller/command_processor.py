"""
Command Processor Module

Processes commands from brain signals and coordinates with the robot controller.
"""

import logging
from typing import Optional, Callable
from .brain_interface import BrainInterface
from .controller import RobotController

logger = logging.getLogger(__name__)


class CommandProcessor:
    """
    Processes commands from brain signals and executes them on the robot.
    
    This class acts as the bridge between the brain interface and robot controller.
    """
    
    def __init__(
        self,
        brain_interface: BrainInterface,
        robot_controller: RobotController,
    ):
        """
        Initialize the command processor.
        
        Args:
            brain_interface: BrainInterface instance for reading signals
            robot_controller: RobotController instance for executing commands
        """
        self.brain_interface = brain_interface
        self.robot_controller = robot_controller
        self.is_processing = False
        self.command_callback: Optional[Callable] = None
        logger.info("CommandProcessor initialized")
    
    def set_command_callback(self, callback: Callable):
        """
        Set a callback function to be called when a command is processed.
        
        Args:
            callback: Function to call with (command, success) parameters
        """
        self.command_callback = callback
    
    def start_processing(self):
        """Start processing brain signals."""
        if not self.brain_interface.is_connected:
            logger.error("Cannot start processing: brain interface not connected")
            return False
        
        if not self.robot_controller.is_running:
            logger.error("Cannot start processing: robot controller not running")
            return False
        
        self.is_processing = True
        logger.info("Started command processing")
        return True
    
    def stop_processing(self):
        """Stop processing brain signals."""
        self.is_processing = False
        logger.info("Stopped command processing")
    
    def process_next_signal(self) -> bool:
        """
        Process the next brain signal and execute the corresponding command.
        
        Returns:
            True if a command was processed, False otherwise
        """
        if not self.is_processing:
            return False
        
        # Read signal from brain interface
        signal = self.brain_interface.read_signal()
        if not signal:
            return False
        
        # Process signal to extract command
        command = self.brain_interface.process_signal(signal)
        if not command:
            return False
        
        # Execute command on robot
        logger.info(f"Executing command: {command}")
        success = self.robot_controller.execute_command(command)
        
        # Call callback if set
        if self.command_callback:
            self.command_callback(command, success)
        
        return success
    
    def get_status(self):
        """
        Get the current status of the command processor.
        
        Returns:
            Dictionary containing processor status
        """
        return {
            "is_processing": self.is_processing,
            "brain_interface_status": self.brain_interface.get_status(),
            "robot_controller_status": self.robot_controller.get_state(),
        }
