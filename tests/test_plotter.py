import numpy as np
import matplotlib.pyplot as plt
import pytest
import os
from waveform_generator.plotter import plot_waveform

@pytest.mark.mpl_image_compare
def test_plot_waveform():
    """Test if the plot function runs without errors and produces a valid plot."""
    t = np.linspace(0, 1, 100)
    y = np.sin(2 * np.pi * 5 * t)  # Example sine wave

    plt.switch_backend("Agg")  # Use non-interactive backend for testing
    plot_waveform(t, y, wave_type="sine", display=False)

    # Save the plot to verify
    plt.savefig("test_plot.png")
    
    # Check if the file was created
    assert os.path.exists("test_plot.png")  

    #Clean up after test
    os.remove("test_plot.png")  