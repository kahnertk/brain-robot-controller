"""
Main Entry Point

Command-line interface for the brain-robot-controller application.
"""

import argparse
import logging
import sys
import time

from .brain_interface import BrainInterface
from .controller import RobotController
from .command_processor import CommandProcessor
from .config import Config


def setup_logging(level: str = "INFO"):
    """
    Set up logging configuration.
    
    Args:
        level: Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    """
    logging.basicConfig(
        level=getattr(logging, level.upper()),
        format=Config.LOGGING["format"],
    )


def main():
    """Main entry point for the application."""
    parser = argparse.ArgumentParser(
        description="Brain Robot Controller - Control robots with brain signals"
    )
    parser.add_argument(
        "--mode",
        choices=["demo", "live"],
        default="demo",
        help="Operation mode: demo (simulated) or live (actual device)",
    )
    parser.add_argument(
        "--duration",
        type=int,
        default=10,
        help="Duration to run in seconds (for demo mode)",
    )
    parser.add_argument(
        "--log-level",
        choices=["DEBUG", "INFO", "WARNING", "ERROR"],
        default="INFO",
        help="Logging level",
    )
    
    args = parser.parse_args()
    
    # Setup logging
    setup_logging(args.log_level)
    logger = logging.getLogger(__name__)
    
    logger.info("=" * 60)
    logger.info("Brain Robot Controller v0.1.0")
    logger.info("Hack-Nation AI Hackathon Challenge")
    logger.info("=" * 60)
    
    try:
        # Initialize components
        logger.info("Initializing components...")
        brain_interface = BrainInterface(Config.BRAIN_INTERFACE)
        robot_controller = RobotController(Config.ROBOT_CONTROLLER)
        command_processor = CommandProcessor(brain_interface, robot_controller)
        
        # Connect and start
        logger.info("Connecting to brain signal device...")
        if not brain_interface.connect():
            logger.error("Failed to connect to brain signal device")
            return 1
        
        logger.info("Starting robot controller...")
        robot_controller.start()
        
        logger.info("Starting command processing...")
        if not command_processor.start_processing():
            logger.error("Failed to start command processing")
            return 1
        
        # Run based on mode
        if args.mode == "demo":
            logger.info(f"Running in demo mode for {args.duration} seconds...")
            logger.info("Simulating brain signal commands...")
            
            start_time = time.time()
            command_count = 0
            
            while time.time() - start_time < args.duration:
                # Process signals at configured rate
                if command_processor.process_next_signal():
                    command_count += 1
                time.sleep(1.0 / Config.COMMAND_PROCESSOR["processing_rate"])
            
            logger.info(f"Demo completed. Processed {command_count} commands.")
        
        else:  # live mode
            logger.info("Running in live mode. Press Ctrl+C to stop.")
            
            try:
                while True:
                    command_processor.process_next_signal()
                    time.sleep(1.0 / Config.COMMAND_PROCESSOR["processing_rate"])
            except KeyboardInterrupt:
                logger.info("Interrupted by user")
        
        # Cleanup
        logger.info("Shutting down...")
        command_processor.stop_processing()
        robot_controller.stop()
        brain_interface.disconnect()
        
        logger.info("Shutdown complete.")
        return 0
    
    except Exception as e:
        logger.error(f"Error: {e}", exc_info=True)
        return 1


if __name__ == "__main__":
    sys.exit(main())
