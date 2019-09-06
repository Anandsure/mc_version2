from flask import Flask, make_response, request
import webbrowser

app = Flask(__name__)

def transform(text_file_contents):
    return text_file_contents.replace("=", ",")


@app.route('/')
def form():
    return """
        <html>
            <body>
                <h1>File Uploading and downloading</h1>

                <form action="/transform" method="post" enctype="multipart/form-data">
                    <input type="file" name="data_file" />
                    <input type="submit" />
                </form>
            </body>
        </html>
    """

@app.route('/transform', methods=["POST"])
def transform_view():
    request_file = request.files['data_file']
    if not request_file:
        return "No file"

    file_contents = request_file.stream.read().decode("utf-8")

    result = transform(file_contents)

    response = make_response(result)
    response.headers["Content-Disposition"] = "attachment; filename=result.txt"
    return response

if __name__=='__main__':
    c=1
    intent=[]
    webbrowser.open('http://127.0.0.1:5000/')
    app.run(debug=False)