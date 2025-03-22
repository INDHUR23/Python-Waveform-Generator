import csv  # Import CSV module for file handling

def save_to_csv(t, y, filename="waveform_data.csv"):
    """
    Saves time and amplitude data to a CSV file.

    Parameters:
        t (array): Time values
        y (array): Amplitude values
        filename (str): Name of the CSV file (default: 'waveform_data.csv')
    """
    
    # Open a file in write mode
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)  # Create a CSV writer object
        
        # Write header row
        writer.writerow(["Time (s)", "Amplitude"])
        
        # Write data (time and corresponding amplitude values)
        writer.writerows(zip(t, y))
    
    print(f"Data saved to {filename}")  # Print confirmation message
