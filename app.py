from flask import Flask, render_template, request, session
import test

app = Flask(__name__)
app.secret_key = 'secret_key'
app.static_folder = 'static'

@app.route("/")
def home():
    session.setdefault('chat_history', "")
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')

    if 'chat_history' not in session:
        session['chat_history'] = ""
    chat_history = session['chat_history']
    if chat_history is None:
        chat_history = ""

    bot_response, session['chat_history'] = test.bot(userText, chat_history)

    return bot_response


if __name__ == "__main__":
    app.run()