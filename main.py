import sys
import os

def clean_up_input(key_input):
    if key_input and key_input[0].isalnum():
        return key_input[0].upper() + key_input[1:]
    else:
        return key_input

def validate_input(args):
    if len(args) != 2:
        return False
    if len(args[1]) > 2:
        return False
    return True

def ensure_its_a_note(note):
    all_notes = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
    if note not in all_notes:
        return False
    else: 
        return True
 
def generate_chromatic_scale_from_root(note):
    all_notes = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
    note_position = all_notes.index(note)
    note_chromatic_scale = (all_notes[note_position:] + all_notes[: note_position])*2
    return note_chromatic_scale

def generate_major_scale_from_root(note):
    major_scale_position = [0, 2, 4, 5, 7, 9, 11]
    chromatic_scale = generate_chromatic_scale_from_root(note)
    major_scale = [chromatic_scale[i] for i in major_scale_position]
    return major_scale

def generate_number_system_chords_from_key(note):
    major_scale = (generate_major_scale_from_root(note))*2
    number_system_chords = []
    for i in range(len(major_scale)):
        chord = [major_scale[i], major_scale[(i + 2) % len(major_scale)], major_scale[(i+4) % len(major_scale)]]
        number_system_chords.append(chord)
    return number_system_chords[:7]

def get_chord_positions(note):
    chord_relative_positions = []
    chords = generate_number_system_chords_from_key(note)
    for chord in chords:
        root_chromatic = generate_chromatic_scale_from_root(chord[0])
        chord_position = [root_chromatic.index(i) for i in chord]
        chord_relative_positions.append(chord_position)
    return chord_relative_positions

def generate_output(note):
    reference = {
        0: "I",
        1: "II",
        2: "III",
        3: "IV",
        4: "V",
        5: "VI",
        6: "VII"
    }
    type_reference = {
        9: "dim",
        10: "minor",
        11: "major"
    }
    chords_with_notes = generate_number_system_chords_from_key(note)
    chords_with_positions = get_chord_positions(note)
    for i in range(len(chords_with_positions)):
        print(f"{reference[i]} {type_reference[sum(chords_with_positions[i])]} - {chords_with_notes[i]}")


if __name__ == "__main__":
    args = sys.argv
    if (validate_input(args)):
        key = clean_up_input(args[1])
        if ensure_its_a_note(key):
            generate_output(key)
        else:
            print("Invalid input. Please provide root/key only using sharps. ")
    else:
        print("Invalid input. Please provide root/key only using sharps. ")