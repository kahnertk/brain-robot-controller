"""
Configuration Module

Provides configuration management for the brain-robot-controller application.
"""

import os
from typing import Dict, Any


class Config:
    """Configuration class for the application."""
    
    # Brain Interface Configuration
    BRAIN_INTERFACE = {
        "device_type": "simulated",  # "simulated", "eeg", "bci"
        "sampling_rate": 256,  # Hz
        "channels": 8,
        "buffer_size": 100,
    }
    
    # Robot Controller Configuration
    ROBOT_CONTROLLER = {
        "movement_speed": 1.0,  # m/s
        "turn_speed": 45.0,  # degrees/s
        "safety_distance": 0.3,  # meters
        "max_distance": 10.0,  # meters
    }
    
    # Command Processor Configuration
    COMMAND_PROCESSOR = {
        "processing_rate": 10,  # Hz
        "command_threshold": 0.7,  # Confidence threshold
        "debounce_time": 0.5,  # seconds
    }
    
    # Logging Configuration
    LOGGING = {
        "level": os.getenv("LOG_LEVEL", "INFO"),
        "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    }
    
    @classmethod
    def get_config(cls) -> Dict[str, Any]:
        """
        Get the complete configuration as a dictionary.
        
        Returns:
            Dictionary containing all configuration settings
        """
        return {
            "brain_interface": cls.BRAIN_INTERFACE,
            "robot_controller": cls.ROBOT_CONTROLLER,
            "command_processor": cls.COMMAND_PROCESSOR,
            "logging": cls.LOGGING,
        }
    
    @classmethod
    def update_config(cls, updates: Dict[str, Any]):
        """
        Update configuration with new values.
        
        Args:
            updates: Dictionary of configuration updates
        """
        for section, values in updates.items():
            if hasattr(cls, section.upper()):
                config_section = getattr(cls, section.upper())
                if isinstance(config_section, dict):
                    config_section.update(values)
