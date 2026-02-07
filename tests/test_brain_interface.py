"""Tests for BrainInterface class."""

import pytest
from brain_robot_controller import BrainInterface


class TestBrainInterface:
    """Test cases for BrainInterface."""
    
    def test_initialization(self):
        """Test brain interface initialization."""
        interface = BrainInterface()
        assert interface.is_connected is False
        assert len(interface.signal_buffer) == 0
    
    def test_connect_disconnect(self):
        """Test connection and disconnection."""
        interface = BrainInterface()
        
        # Test connect
        assert interface.connect() is True
        assert interface.is_connected is True
        
        # Test disconnect
        interface.disconnect()
        assert interface.is_connected is False
    
    def test_read_signal(self):
        """Test reading signals."""
        interface = BrainInterface()
        
        # Should return None when not connected
        assert interface.read_signal() is None
        
        # Should return signal when connected
        interface.connect()
        signal = interface.read_signal()
        assert signal is not None
        assert "timestamp" in signal
        assert "channels" in signal
        assert "quality" in signal
        assert len(signal["channels"]) == 8
    
    def test_process_signal(self):
        """Test signal processing."""
        interface = BrainInterface()
        
        # Test with None signal
        assert interface.process_signal(None) is None
        
        # Test with empty signal
        assert interface.process_signal({}) is None
        
        # Test with valid signal
        signal = {
            "timestamp": 0,
            "channels": [0.0] * 8,
            "quality": 1.0,
        }
        result = interface.process_signal(signal)
        # Result can be None or a command string
        assert result is None or isinstance(result, str)
    
    def test_get_status(self):
        """Test getting interface status."""
        interface = BrainInterface()
        
        status = interface.get_status()
        assert "is_connected" in status
        assert "buffer_size" in status
        assert status["is_connected"] is False
        
        interface.connect()
        status = interface.get_status()
        assert status["is_connected"] is True
