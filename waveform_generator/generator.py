# Contains functions to generate sine, square, and triangular waves using NumPy.

import numpy as np

def generate_waveform(wave_type, frequency=5, duration=1, sample_rate=1000):
    """
    Generate a waveform based on the given type.

    Parameters:
        wave_type(str): 'sine', 'square' or 'triangle'
        frquency(int): Frequency in Hz
        duration(float): Duration in seconds
        Sample_rate(int): Number of samples per second

    Returns:
        tuple: (time array, amplitude array)

    """
    # Generate a time array from 0 to 'duration' with 'sample_rate' samples
    t= np.linspace(0, duration, int(sample_rate*duration), endpoint=False)

    if wave_type=="sine":
        y = np.sin(2*np.pi * frequency *t) # Sine wave formula: sin(2*pi*ft)
    
    elif wave_type=="square":
        y = np.sign(np.sin(2 * np.pi * frequency * t)) #Square wave

    elif wave_type== "triangle":
        y = 2* np.abs(2*(t*frequency - np.floor(t*frequency+0.5))) - 1 #Triangle wave
    
    else:
        raise ValueError(f"Invalid wave_type: {wave_type}")
    
    return t,y #return time and amplitude arrays

