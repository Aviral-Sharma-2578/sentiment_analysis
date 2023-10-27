from flask import Flask,render_template,request
from textblob import TextBlob

app = Flask(__name__)

@app.route('/',methods=['POST','GET'])

def main():
    if request.method == 'POST':
        inp = request.form.get("inp")
        blob=TextBlob(inp)
        if(blob.sentiment.polarity>0):
            return render_template('home.html',message="Positive😊")
        elif(blob.sentiment.polarity<0):
            return render_template('home.html',message="Negative 🙁")
        else :
            return render_template('home.html',message="Neutral 😑")
    return render_template('home.html')
