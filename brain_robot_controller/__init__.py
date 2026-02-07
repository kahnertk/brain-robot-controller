"""
Brain Robot Controller - A hackathon project for controlling robots using brain signals/AI.

This package provides interfaces for brain signal processing and robot control.
"""

__version__ = "0.1.0"
__author__ = "Hack-Nation AI Hackathon"

from .controller import RobotController
from .brain_interface import BrainInterface
from .command_processor import CommandProcessor

__all__ = [
    "RobotController",
    "BrainInterface",
    "CommandProcessor",
]
