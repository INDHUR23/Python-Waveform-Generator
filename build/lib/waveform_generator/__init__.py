#Package Initialization
#makes waveform_generator a package

from .generator import generate_waveform
from .plotter import plot_waveform
from .file_handler import save_to_csv

__all__=["generate_waveform", "plot_waveform", "save_to_csv"]
