Magenta has six pretrained performance rnn models that generate sequences. Provide an interface similar to https://magenta.tensorflow.org/demos/performance_rnn/index.html
This project is a WIP.

To run app:
1. export FLASK_APP=app.py
2. flask run

Documentation for Magenta:
https://github.com/magenta/magenta/tree/master/magenta/models/performance_rnn

Pretrained Models Methodology Details:
https://arxiv.org/pdf/1808.03715v1.pdf
Keywords: beam search, LSTM

References
Good Practices for Deployment: https://flask.palletsprojects.com/en/1.1.x/deploying/#deployment
Flask Tutorial https://rollout.io/blog/python-feature-flag-guide/


Todo:
Test model selection in form
Embed Bokeh into HTML
Play sequence upon model selection

 
