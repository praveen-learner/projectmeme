import requests
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont
from flask import Flask, render_template, request

app = Flask(__name__)


RAPIDAPI_KEY = 'e87f5df8ddmshd4fdb9907c93964p1462d5jsn145babb65148'
RAPIDAPI_BASE_URL = 'https://ronreiter-meme-generator.p.rapidapi.com/meme'

@app.route('/', methods=['GET', 'POST'])
def meme_generator():
    if request.method == 'POST':
        top_text = request.form['top_text']
        bottom_text = request.form['bottom_text']
        meme_url = generate_meme(top_text, bottom_text)
        return render_template('meme.html', meme_url=meme_url)
    return render_template('index.html')

def generate_meme(top_text, bottom_text):
    headers = {
        'X-RapidAPI-Key': RAPIDAPI_KEY,
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    data = {
        'font': 'impact',
        'font_size': '50',
        'meme': 'Condescending-Wonka',
        'top': top_text,
        'bottom': bottom_text
    }
    response = requests.post(RAPIDAPI_BASE_URL, headers=headers, data=data)
    if response.status_code == 200:
        return response.json()['data']['url']
    return None

if __name__ == '__main__':
    app.run(debug=True)
