import matplotlib.pyplot as plt  # Import Matplotlib for plotting

def plot_waveform(t, y, wave_type, display=True):
    """
    Plots the given waveform using Matplotlib.

    Parameters:
        t (array): Time values
        y (array): Amplitude values
        wave_type (str): Type of waveform to label the plot
    """
    
    # Create a new figure
    plt.figure(figsize=(8, 4))  # Set figure size
    
    # Plot the waveform
    plt.plot(t, y, label=f"{wave_type.capitalize()} Wave", color="b")
    
    # Add labels and title
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.title(f"{wave_type.capitalize()} Waveform")
    plt.legend()  # Show the legend
    plt.grid()  # Enable the grid for better visibility
    
    # Display the plot
    if display:
        plt.show() #only display if not in test mode
