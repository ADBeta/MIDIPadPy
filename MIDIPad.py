import midi

midi.open(1);
print("Polling the MIDI Device. Press Control-C to exit.")

midi.poll();

