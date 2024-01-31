from flask import Flask, render_template, request, redirect

import random
import string

app = Flask(__name__)

def generate_short_url():
    characters = string.ascii_letters + string.digits
    short_url = ''.join(random.choice(characters) for _ in range(6))
    return short_url

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        long_url = request.form['user_input']
        short_url = generate_short_url()
        tiny_url = f"https://tinyrage.com/{short_url}"
        return render_template('result.html', tiny_url=tiny_url)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
