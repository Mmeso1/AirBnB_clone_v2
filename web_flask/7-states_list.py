from flask import Flask, render_template
from models import storage, State

app = Flask(__name__)

# Teardown app context method
@app.teardown_appcontext
def close_storage(exception):
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    states = storage.all(States).values()
    sorted_states = sorted(states, key=lambda s: s.name)
    return render_template('7-states_list.html', states=sorted_states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
