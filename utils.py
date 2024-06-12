# utils.py
import os
from werkzeug.utils import secure_filename
from flask import current_app

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def save_file(file):
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
        return filename
    return None


def delete_file(filename):
    if os.path.exists(os.path.join(current_app.config['UPLOAD_FOLDER'], filename)):
        os.remove(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
