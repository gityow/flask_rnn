from flask import Flask, jsonify, render_template
import request
app = Flask(__name__) # use __name__
#
# normalday = {
#         'id': 1,
#         'title': u'Meh',
#         'description': u'Just another day',
#         'party': False
# }

@app.route('/', methods=['GET','POST'])
def show_sequence():
    global selected_model
    global model_check_message
    # TODO get user's selected_model
    def select_model(attr, old, new):
        if request.method == 'POST':
            #selected_model = 'performance_with_dynamics'
            selected_model = request.form["model"]

            # if selected_model != 'performance_with_dynamics':
            #     model_check_message = 'Model Not Found!'
            # else:
            #     model_check_message = f'Loading Model {selected_model}'
        return render_template("select_model.html")

    # import model
    # sequence = model.generate_sequence(selected_model)
    #
    # import note_seq
    # plot = note_seq.plot_sequence(sequence) # bokeh plot
    #
    # return jsonify({'today': normalday})

if __name__  == 'main':
    # test if localhost can connect
    app.run(debug=True)