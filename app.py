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
    title , data =  find.get_data(url)
    return jsonify({'title':title , 'data':data})

app.run(debug=True)