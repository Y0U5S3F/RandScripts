from midiutil import MIDIFile

chords = {
    "M": {},
    "m": {},
    "M7": {},
    "m7": {},
    "Dim": {},
    "aug": {},
    "sus2": {},
    "sus4": {}
}

# Generate chords for all 88 keys
for key in range(21, 109):  # MIDI note numbers for the piano keys range from 21 to 108
    note_name = {0: 'C', 1: 'C#', 2: 'D', 3: 'D#', 4: 'E', 5: 'F', 6: 'F#', 7: 'G', 8: 'G#', 9: 'A', 10: 'A#', 11: 'B'}[key % 12]
    octave = (key // 12) - 1
    note = key
    chords["M"][f"{note_name}{octave}"] = [note + i for i in [0, 4, 7]]
    chords["m"][f"{note_name}{octave}"] = [note + i for i in [0, 3, 7]]
    chords["M7"][f"{note_name}{octave}"] = [note + i for i in [0, 4, 7, 11]]
    chords["m7"][f"{note_name}{octave}"] = [note + i for i in [0, 3, 7, 10]]
    chords["Dim"][f"{note_name}{octave}"] = [note + i for i in [0, 3, 6, 9]]
    chords["aug"][f"{note_name}{octave}"] = [note + i for i in [0, 4, 8]]
    chords["sus2"][f"{note_name}{octave}"] = [note + i for i in [0, 2, 7]]
    chords["sus4"][f"{note_name}{octave}"] = [note + i for i in [0, 5, 7]]


def get_chord():
    chord_input = input("Enter chord (e.g., CM, Cm, Cm7, CM7, Cdim7, Csus2, Csus4): ")
    note = chord_input.rstrip('Mm7Dimaugus2us4')
    chord_type = chord_input[len(note):]
    chord_type = chord_type.upper() if chord_type.lower() == 'm' else chord_type.lower()

    if chord_type in chords and note.upper() in chords[chord_type]:
        return chords[chord_type][note.upper()]
    else:
        return "Error: Chord not found"

def create_midi(filename, track_name="Sample Track", tempo=120, chords=[[60, 64, 67]]):
    # Create a MIDIFile object with one track
    midi = MIDIFile(1)

    # Add track name and tempo
    track = 0
    time = 0
    midi.addTrackName(track, time, track_name)
    midi.addTempo(track, time, tempo)

    # Add some notes
    channel = 0
    volume = 100
    duration = 1  # in beats

    for chord in chords:
        for note in chord:
            midi.addNote(track, channel, note, time, duration, volume)
        time += 1  # Move to the next beat after adding all notes of the chord

    # Write the MIDI file to disk
    with open(filename, "wb") as f:
        midi.writeFile(f)

if __name__ == "__main__":
    chord_notes = get_chord()
    if isinstance(chord_notes, list):
        create_midi("output.mid", track_name="My Track", tempo=140, chords=[chord_notes])  # Corrected parameter name to 'chords'
    else:
        print(chord_notes)  # Print the error message
