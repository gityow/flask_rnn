Magenta has six pretrained performance rnn models that generate sequences. Provide an interface similar to 
https://magenta.tensorflow.org/demos/performance_rnn/index.html  
This project is a WIP.

To run app:
1. export FLASK_APP=app.py
2. flask run

Documentation for Magenta:  
https://github.com/magenta/magenta/tree/master/magenta/models/performance_rnn

Pretrained Models Methodology Details:
https://arxiv.org/pdf/1808.03715v1.pdf
The paper details that current state of art music generation techniques doesn't capture the expressive timing (tempo) and 
dynamics (how much louder/quieter the music gets) information. They created an LSTM based recurrent network model that
jointly predicts notes and also expressive timing and dynamic. 

Keywords: beam search, LSTM, teacher forcing



Twimlai: https://www.youtube.com/watch?v=8AARfVVrdXc
Some uses of the Performance RNN: https://www.youtube.com/watch?v=Ye0Geuo1Iu8
Good Practices for Deployment: https://flask.palletsprojects.com/en/1.1.x/deploying/#deployment
Flask Tutorial https://rollout.io/blog/python-feature-flag-guide/
working with midi files: https://www.twilio.com/blog/working-with-midi-data-in-python-using-mido
MIDI Editor: https://solmire.com/midieditor/editor.php (to speed up/slow down midi files)
MIDI Trimmer: http://midi.mathewvp.com/midiTrim.php (to make the midi files into shorter clips)
MIDI Timing Explanation: https://sites.uci.edu/camp2014/2014/05/19/timing-in-midi-files/

Todo:
Test model selection in form
Embed Bokeh into HTML
Play sequence upon model selection
Trim more 30 sec clips (Erik Satie Trois Gymnopedies , moonlight sonata)
Try out num steps argument <-- done -->
Find a midi player for flask 

 
