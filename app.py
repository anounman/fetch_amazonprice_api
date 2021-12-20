from flask import Flask , request , jsonify
from flask_cors import CORS
import find
app = Flask(__name__)
CORS(app)

@app.route('/' , methods=['GET' , 'POST'])
def index():
    return "use :- /amazon?url=<url>"

@app.route('/amazon', methods=['GET', 'POST'])
def amazon():
    url = request.args.get('url')
    state = request.args.get('html')
    if (state == None):
        state = False
    title , data , review , img , about , short_desc =  find.get_data(url , state)
    return jsonify({
        'title':title , 
        "img": img ,  
        'data':data , 
        "review": review , 
        "about": about,
        "short_desc" : short_desc
    
    })

app.run(debug=True)