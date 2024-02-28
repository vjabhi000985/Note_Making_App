from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)
app.static_folder = 'static'

notes = []

@app.route('/')
def index():
    # Load the data from the file
    load_notes()
    return render_template('home.html', notes=notes)

@app.route('/add_note', methods=['POST'])
def add_note():
    note_text = request.form['note']
    notes.append({'text': note_text})
    save_notes()
    return index()

@app.route('/delete_note/<int:notes_id>', methods=['GET','POST'])
def delete_note(notes_id):
    if request.method == 'POST':
        del notes[notes_id]
        save_notes()
    return redirect(url_for('index'))

def load_notes():
    global notes
    try:
        with open('notes.json','r') as file:
            notes = json.load(file)
    except FileNotFoundError:
        notes = []

def save_notes():
    with open('notes.json','w') as file:
        json.dump(notes, file, indent=4)

if __name__ == '__main__':
    app.run(debug=True)