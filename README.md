# MidiToOneOctave
This Python script processes a MIDI file and restricts all notes to a single octave. The resulting MIDI file will have all its notes adjusted to fit within the single octave range.

## Usage

1. Place MidiToOneOctave.py in a folder with a midi file "input.mid"
2. Run MidiToOneOctave.py
3. "output.mid" is generated with all notes restricted to one octave.

## Customization

- You can change the octave_start parameter to specify the starting note of the desired octave. By default, it is set to 60 (Middle C, C4).

## Requirements

- Python 3.x
- mido library
