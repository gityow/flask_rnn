
import os
import ast # abstract syntax trees
import numpy as np
from mido import MidiFile



def generate_sequence(selected_model="performance", selected_music=None):
    # midi_file = "chopin_nocturne.mid" #TODO enable uploads of midi files or use defaults

    if selected_music :
        filepath = f"./midi_files/{selected_music}"
        mid = MidiFile(filepath)
        length = np.int(np.floor(mid.length*100))
        cmd = f"performance_rnn_generate \
        --config {selected_model} \
        --bundle_file ./models/{selected_model}.mag \
        --output_dir ./generated \
        --num_outputs 1 \
        --num_steps {length} \
        --primer_midi ./midi_files/{selected_music}"

    else:
        cmd = f"""cat no midil file given"""
    os.system(cmd)


def play_music(music_file):
    '''
    stream music with mixer.music module in blocking manner
    this will stream the sound from disk while playing
    '''
    clock = pg.time.Clock()
    try:
        pg.mixer.music.load(music_file)
        print("Music file {} loaded!".format(music_file))
    except pg.error:
        print("File {} not found! {}".format(music_file, pg.get_error()))
        return
    pg.mixer.music.play()
    # check if playback has finished
    while pg.mixer.music.get_busy():
        clock.tick(30)


def main():
    generate_sequence()
    play_music