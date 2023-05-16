
def generate_fretboard():
    open_note_positions = ["E", "A", "D", "G", "B", "E"]
    fretboard = []
    for note in open_note_positions:
        fretboard.append(generate_string_matrix(note))
    return fretboard

def generate_string_matrix(open_note):
    all_notes = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
    note_position = all_notes.index(open_note)
    template = (all_notes[note_position:] + all_notes[:note_position])*3;
    string_matrix = []
    for index, note in enumerate(template):
        string_matrix.append((index, note))
    return string_matrix


FRETBOARD = generate_fretboard()