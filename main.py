from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///diary.db'
db = SQLAlchemy(app)

class DiaryEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, default=datetime.now)
    entry = db.Column(db.Text)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        entry_text = request.form['entry']

        new_entry = DiaryEntry(entry=entry_text)
        db.session.add(new_entry)
        db.session.commit()

        flash("日記エントリーが保存されました。")
        return redirect(url_for('index'))

    entries = DiaryEntry.query.order_by(DiaryEntry.date.desc()).all()
    return render_template('index.html', entries=entries)

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
