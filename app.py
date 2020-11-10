from flask import Flask, render_template, request, jsonify, render_template
import model
app = Flask(__name__) # use __name__

@app.route('/home', methods=['GET','POST'])
def show_sequence():
    selected_model = ''
    selected_music = ''
    display_txt = ''

    # TODO get user's selected_model
    models = [
        "density_conditioned_performance_with_dynamics"
        , "multiconditioned_performance_with_dynamics"
        , "performance"
        , "performance_with_dynamics"
        , "performance_with_dynamics_and_modulo_encoding"
        , "pitch_conditioned_performance_with_dynamics"
    ]

    music =[
        'chopin_nocturne.mid'
        , 'satie_gymnopedie_new.mid'
    ]

    if request.method == 'POST': # submit button was selected

        selected_model = request.form["modelDropdown"]
        selected_music = request.form["musicDropdown"]

        model.generate_sequence(selected_model, selected_music)
        display_txt = f"{selected_model} is currently deciding how to play {selected_music}"



    return render_template("landing.html", models=models, music=music, display_txt=display_txt)





if __name__  == 'main':
    # test if localhost can connect
    app.run(debug=True)