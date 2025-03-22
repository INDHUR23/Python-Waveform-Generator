from generator import generate_waveform  # Import waveform generator function
from plotter import plot_waveform  # Import waveform plotting function
from file_handler import save_to_csv  # Import function to save data to CSV

def main():
    """
    Main function to execute waveform generation, saving, and plotting.
    """
    
    # Ask the user to enter a waveform type
    wave_type = input("Enter waveform type (sine/square/triangle): ").strip().lower()
    
    try:
        # Generate the selected waveform
        t, y = generate_waveform(wave_type)
        
        # Save the waveform data to a CSV file
        save_to_csv(t, y, f"{wave_type}_waveform.csv")
        
        # Plot the waveform
        plot_waveform(t, y, wave_type)
    
    except ValueError as e:
        print(f"Error: {e}")  # Print error if an invalid waveform type is entered

# Run the script only if executed directly (not when imported)
if __name__ == "__main__":
    main()
