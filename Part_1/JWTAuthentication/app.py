from flask import Flask, render_template, request, redirect, url_for
from flask_jwt_extended import JWTManager, jwt_required, create_access_token

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.secret_key = 'your_secret_key' 


jwt = JWTManager(app)


users = {
    'your_username': 'your_password',
}

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

      
        access_token = create_access_token(identity=image_name)
        return render_template('result.html', image_name=image_name, access_token=access_token)


@app.route('/api/protected', methods=['GET'])
@jwt_required()  
def protected():
    return {'message': 'This is a protected API endpoint'}

if __name__ == '__main__':
    app.run(debug=True)
