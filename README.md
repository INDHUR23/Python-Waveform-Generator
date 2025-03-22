# Python Waveform Generator

A simple Python project to generate and visualize waveforms like **sine, square, and triangle waves**.

## Features
1. Generate **Sine, Square, and Triangle** waves  
2. Adjustable **frequency and amplitude**  
3. Plot waveforms using **Matplotlib**  
4. **Tested** with `pytest`  


## Installation

**Clone the Repository**
```bash
git clone https://github.com/INDHUR23/Python-Waveform-Generator.git
cd Python-Waveform-Generator
```

**Install Dependencies**
```bash
pip install -e .
```
## Usage

**Generate a Waveform**
```bash
from waveform_generator.generator import generate_waveform

t, y = generate_waveform(wave_type="sine", frequency=5, amplitude=1, duration=1, sample_rate=1000)
```
**Plot a Waveform**
```bash
from waveform_generator.plotter import plot_waveform

plot_waveform(t, y, wave_type="Sine Wave")
```

**Running Tests**

Run all tests using pytest:
```bash
pytest
```

## Example Output
Here’s a sample Sine Wave plot:
![Sine Waveform](sine.png)

## Contributing
Feel free to submit issues or contribute via pull requests! 