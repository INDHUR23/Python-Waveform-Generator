import os
import csv
from waveform_generator.file_handler import save_to_csv

def test_save_to_csv():
    """Test if waveform data is correctly written to a CSV file."""
    t = [0, 0.1, 0.2]
    y = [0, 1, -1]
    filename = "test_waveform.csv"

    # Save the test data
    save_to_csv(t, y, filename)

    # Check if the file is created
    assert os.path.exists(filename)

    # Read and verify contents
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        rows = list(reader)

    assert rows[0] == ["Time (s)", "Amplitude"]  # Check header
    assert rows[1] == ["0", "0"]  # Check first data row
    assert rows[2] == ["0.1", "1"]  # Check second data row
    assert rows[3] == ["0.2", "-1"]  # Check third data row

    # Cleanup: Remove test file
    os.remove(filename)
