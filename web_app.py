from flask import Flask
from flask import request
from PIL import Image
import CharPicture
import uuid


app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():

    return'''<form method="POST" enctype="multipart/form-data" action="/upload">
      <input type="file" name="file">
      <input type="submit" value="转换">
      </form>'''


@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    print(file)
    im = Image.open(file)
    im = CharPicture.contrast_enhance(im, 10)
    result = CharPicture.convert_to_charpic(im, 1)
    file.save(uuid.uuid4() + 'jpg')
    # return '''<h1>上传成功</h1>'''
    return result

if __name__ == '__main__':
    app.run('0.0.0.0', 5432)
