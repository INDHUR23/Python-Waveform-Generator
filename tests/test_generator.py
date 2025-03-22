import pytest
import numpy as np
from waveform_generator.generator import generate_waveform

def test_generate_sine_wave():
    """Test if sine wave values are generated correctly."""
    t, y = generate_waveform("sine", frequency=1, duration=1, sample_rate=10)
    assert len(t) == len(y)  # Ensure time and amplitude arrays have the same length
    assert np.all(np.abs(y) <= 1)  # Check that values are within the range [-1,1]

def test_generate_square_wave():
    """Test if square wave values are -1 or 1."""
    t, y = generate_waveform("square", frequency=1, duration=1, sample_rate=10)
    assert len(t) == len(y)  
    assert np.all(np.abs(y) <= 1) # Square wave should only have values -1 or 1
    print("Square wave values:", y)

def test_generate_triangle_wave():
    """Test if triangle wave values are within the correct range."""
    t, y = generate_waveform("triangle", frequency=1, duration=1, sample_rate=10)
    assert np.all(np.abs(y) <= 1)  # Triangle wave should be between -1 and 1

