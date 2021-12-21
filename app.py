from flask import Flask , request , jsonify
from flask_cors import CORS
import find
app = Flask(__name__)
# CORS(app)

@app.route('/' ,)
def index():
    return "use :- /amazon?url=<url>"

@app.route('/amazon', methods=['GET', 'POST'])
def amazon():
    url = request.args.get('url')
    state = request.args.get('html')
    if (state == None):
        state = False
    data =  find.get_data(url , state)
    return jsonify(data) 
if __name__ == '__main__':
    app.run(debug=True)