import mido
from mido import MidiFile, MidiTrack, Message

def restrict_to_one_octave(note, octave_start=60):
    """Restrict a note to one octave range starting at octave_start (default is C4)."""
    octave_size = 12
    return (note % octave_size) + octave_start

def restrict_midi_to_one_octave(input_file, output_file, octave_start=60):
    """Restrict all notes in the MIDI file to one octave and save to output file."""
    mid = MidiFile(input_file)
    new_mid = MidiFile()

    for i, track in enumerate(mid.tracks):
        new_track = MidiTrack()
        new_mid.tracks.append(new_track)
        for msg in track:
            if msg.type == 'note_on' or msg.type == 'note_off':
                new_note = restrict_to_one_octave(msg.note, octave_start)
                new_msg = msg.copy(note=new_note)
                new_track.append(new_msg)
            else:
                new_track.append(msg)

    new_mid.save(output_file)
    print(f"Saved new MIDI file with restricted notes to {output_file}")

# Example usage
input_file = 'input.mid'
output_file = 'output.mid'
restrict_midi_to_one_octave(input_file, output_file)
