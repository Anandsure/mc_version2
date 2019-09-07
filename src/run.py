from flask import Flask, make_response, request, render_template
import webbrowser
import c2p
from flask_cors import CORS
import json,time



app = Flask(__name__)
CORS(app)

def transform(text_file_contents):
    return text_file_contents.replace("=", "=")


@app.route('/')
def form():
    return render_template('convert.html')
    #return render_template('gfile.html')

@app.route('/transform', methods=['POST','GET'])
def transform_view():
    request_file = request.files['data_file']
    if not request_file:
        return "No file"

    file_contents = request_file.stream.read().decode("utf-8")

    result = transform(file_contents)

    print(result)
    py_list = c2p.convert(result)
    pycode=''
    for i in py_list:
        print(i,end='')
        pycode+=i
    #print(pycode)
    response = make_response(pycode)
    response.headers["Content-Disposition"] = "attachment; filename=converted_py_code.py"
    return response

@app.route('/box', methods=['POST','GET'])
def box():
    if request.method == 'POST':
        resp_json = request.get_json()
        to_convert = resp_json['text']

        py_list = c2p.convert(to_convert)
        pycode=''
        for i in py_list:
            print(i,end='')
            pycode+=i
        time.sleep(2)
        return json.dumps({"response": pycode}), 200


if __name__=='__main__':
    webbrowser.open('http://127.0.0.1:5000/')
    app.run(debug=False)