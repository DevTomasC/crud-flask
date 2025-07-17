from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')

def index():
    tasks = ['tarefa 1', 'tarefa 2', 'Tarefa 3',]
    return render_template('index.html', tasks = tasks)




if __name__ == "__main__":
    app.run(debug=True, port= 5153)
