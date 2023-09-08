from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

@app.route('/')
def upload_form():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return redirect(request.url)

    image = request.files['image']

    if image.filename == '':
        return redirect(request.url)

    if image:
        image_name = image.filename
        return render_template('result.html', image_name=image_name)

if __name__ == '__main__':
    app.run(debug=True)
