from flask import Flask, jsonify, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/soils', methods=['GET'])
def get_tasks():
    return jsonify({'soils': soils})


if __name__ == '__main__':
    a = "черноземы и все такое"
    soils = [
        {
            'id': 1,
            'title': 'Черноземы',
            'description': 'обладают хорошими водно-воздушными свойствами, отличаются комковатой или зернистой структурой',
            'done': False
        },
        {
            'id': 2,
            'title': 'Болотистая',
            'description': 'Чтобы улучшить плодородие болотистых почв необходимо насытить землю песком',
            'done': False
        }
    ]

    app.run(debug=True)
