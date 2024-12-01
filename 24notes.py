# -*- coding: utf-8 -*-
"""24notes.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/14xId8BOt4Cm2gs9c6qHmpMXvxEzc3cAQ
"""

# 24-Notes: https://www.youtube.com/watch?v=lvmzgVtZtUQ
# Stanford CCRMA project: https://ccrma.stanford.edu/~arvindh/cmt/the_12_notes.html
import numpy as np
import IPython.display as ipd

# Taking tonic/shruti input
shruti = input("Enter the shruti(frequency value or Western Alphabets): ")
# all tonics considered are C3 -> B3 in https://www.szynalski.com/tone-generator/
tonic = {'C': 131.813,
         'C#': 138.591,
         'D': 146.832,
         'D#': 155.563,
         'E': 164.814,
         'F': 174.614,
         'F#': 184.997,
         'G': 195.998,
         'G#': 207.652,
         'A': 220.000,
         'A#': 233.082,
         'B': 246.942}

# variable 's' stores the actual freq value of input tonic
# Check if the input shruti is in the dictionary
if shruti in tonic:
    s = tonic[shruti]
else:
    s = float(shruti)  # If input is a frequency value
print(s)
s1 = s

# Parameters
# s = Frequency of the sine wave in Hz (A4 note)
duration = 4  # Duration of the sine wave in seconds
sample_rate = 44100  # Sample rate in Hz

# 12 Note Western System
# Dictionary to store octave info about all 12 notes
octave={'1) Shadja (S)': s*1,
        '2) Shudha Rishabha (R1)': s*1.0667,
        '3) Chatusruthi Rishabha aka Shudha Gandhara (R2/G1)': s*1.125,
        '4) Shatsruthi Rishabha aka Sadharana Gandhara (R3/G2)': s*1.200,
        '5) Antara Gandhara (G3)': s*1.250,
        '6) Shudha Madhyama (M1)': s*1.334,
        '7) Prati Madhyama (M2)': s*1.400,
        '8) Panchama (P)': s*1.500,
        '9) Shudha Daivata (D1)': s*1.600,
        '10) Chatusruthi Daivatha aka Shudha Nishada (D2/N1)': s*1.667,
        '11) Shatsruthi Dhaivatha aka Kaishiki Nishada (D3/N2)': s*1.800,
        '12) Kaakali Nishada (N3)': s*1.875,
        '13) Upper Shadja (s)': s*2}

# 24 Note Western System
# Dictionary to store octave info about all 24 notes
octave24={'1) S': s1*1,
        '2) S-R1': s1*1.03125,
        '3) R1': s1*1.0667,
        '4) R1-R2': s1*1.100,
        '5) R2': s1*1.125,
        '6) R2-R3/G2': s1*1.167,
        '7) R3/G2': s1*1.200,
        '8) R3/G2-G3': s1*1.2223,
        '9) G3': s1*1.250,
        '10) G3-M1': s1*1.2857,
        '11) M1': s1*1.334,
        '12) M1-M2': s1*1.375,
        '13) M2': s1*1.400,
        '14 M2-P': s1*1.4545,
        '15) Pa': s1*1.500,
        '16) P-D1': s1*1.55556,
        '17) D1': s1*1.600,
        '18) D1-D2/N1': s1*1.6363,
        '19) D2': s1*1.667,
        '20) D2/N1-D3/N2': s1*1.750,
        '21) D3/N2': s1*1.800,
        '22) D3/N2-N3': s1*1.8334,
        '23) N3': s1*1.875,
        '24) N3-s': s1*1.92857,
        '25) s': s1*2}

import matplotlib.pyplot as plt
# Function to play audio for a given frequency
def play_note(frequency, duration=4, sample_rate=44100):
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    note = np.sin(frequency * 2 * np.pi * t)
    print(f"Playing frequency {frequency} Hz")
    return ipd.Audio(note, rate=sample_rate)

# Function to visualize note ratios
def visualize_note_ratios(octave_dict, title):
    # Extract frequencies and normalize them
    frequencies = list(octave_dict.values())
    notes = list(octave_dict.keys())

    # Normalize frequencies
    min_freq = frequencies[0]
    max_freq = frequencies[-1]
    normalized_freq = [(f - min_freq) / (max_freq - min_freq) for f in frequencies]

    # Create the plot
    figure = plt.figure(figsize=(15, 5))
    figure.suptitle(title, fontsize=16)
    ax = figure.add_subplot(111)
    ax.set_xlabel('Relative Frequency Ratio', fontsize=12)
    ax.set_ylabel('Notes', fontsize=12)

    # Plot horizontal lines for each note
    for i, (note, ratio, freq) in enumerate(zip(notes, normalized_freq, frequencies)):
        ax.axhline(y=i, xmin=0, xmax=ratio, color='red', marker='o')
        ax.text(ratio, i, f' {note} ({freq:.2f} Hz)', verticalalignment='center')

    # Customize y-axis
    ax.set_yticks(range(len(notes)))
    ax.set_yticklabels([])
    ax.set_ylim(-1, len(notes))

    # Customize x-axis
    ax.set_xlim(0, 1)
    ax.grid(axis='x', linestyle='--', alpha=0.7)

    plt.tight_layout()
    plt.show()

import matplotlib.pyplot as plt
# Play notes and visualize for 12-note system
print("\n--- 12 Note Octave ---")
for note_name, frequency in octave.items():
    ipd.display(play_note(frequency))
visualize_note_ratios(octave, "12 Note Octave")

# Play notes and visualize for 24-note system
print("\n--- 24 Note Octave ---")
for note_name, frequency in octave24.items():
    ipd.display(play_note(frequency))

visualize_note_ratios(octave24, "24 Note Octave")