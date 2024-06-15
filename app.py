from flask import Flask, render_template, request, redirect, url_for
from tester import bfs_shortest_path, d

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def home():
    locations = list(d.keys())  # Get list of available locations from graph

    if request.method == 'POST':
        try:
            location = request.form['location']
            destination = request.form['destination']
            print(f"Location: {location}, Destination: {destination}")  # Debug statement
            shortest_path = bfs_shortest_path(location, destination)
            if isinstance(shortest_path, str):  # Check if an error message was returned
                return redirect(url_for('error', error_message=shortest_path))
            return redirect(url_for('result', arr=shortest_path))
        except ValueError as e:
            print(f"Error: {e}")  # Debug statement for invalid input
            return render_template("index.html", error="Please enter valid integers.")
    return render_template("index.html", locations=locations)

@app.route('/result')
def result():
    arr = request.args.getlist('arr')
    return render_template("result.html", arr=arr)

@app.route('/error')
def error():
    e = request.args.get('error_message')
    return render_template("error.html", e=e)


if __name__ == "__main__":
    app.run(debug=True)
