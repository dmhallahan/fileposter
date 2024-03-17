# from flask import Flask

# # Create a Flask application instance
# app = Flask(__name__)

# # Define a route for the root URL
# @app.route('/')
# def index():
#     return "Hello, World! This is my web server."

# if __name__ == "__main__":
#     # Run the Flask app on localhost and port 5000
#     app.run(debug=True)



from flask import Flask, request

# Create a Flask application instance
app = Flask(__name__)

# Define a route for the file upload
@app.route('/upload', methods=['POST'])
def upload_file():
    # Check if the POST request has the file part
    if 'file' not in request.files:
        return 'No file part'

    file = request.files['file']

    # If the user does not select a file, the browser submits an empty file without a filename
    if file.filename == '':
        return 'No selected file'

    # Check if the file is allowed (you can add more extensions if needed)
    allowed_extensions = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
    if '.' in file.filename and file.filename.rsplit('.', 1)[1].lower() in allowed_extensions:
        file_type = file.filename.rsplit('.', 1)[1].lower()
        return f'The file type is: {file_type}'
    else:
        return 'File type not allowed'

if __name__ == "__main__":
    # Run the Flask app on localhost and port 5000
    app.run(debug=True)
