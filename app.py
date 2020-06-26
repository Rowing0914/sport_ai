import os
from flask import Flask, request, redirect
from werkzeug.utils import secure_filename

from src.param import PARAMS
from src.video_combine import combine

# Create the storage directory if it doesn't exist yet.
if not os.path.exists(PARAMS.UPLOAD_FOLDER):
    os.makedirs(PARAMS.UPLOAD_FOLDER)

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = PARAMS.UPLOAD_FOLDER
app.config['SECRET_KEY'] = os.urandom(32)


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        left_view = request.files['left_view']
        right_view = request.files['right_view']
        if left_view and right_view:
            for file in [left_view, right_view]:
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            # combine the videos
            combine()
            return redirect("/")
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <p>Left View: <input type=file name=left_view></p>
      <p>Right View: <input type=file name=right_view></p>
      <input type=submit value=Upload>
    </form>
    '''


if __name__ == "__main__":
    app.run(debug=True)
