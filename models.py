from flask import jsonify, request, session, redirect, url_for
from passlib.hash import pbkdf2_sha256
import uuid
from user.db import get_db
import datetime

class User:
    def start_session(self, user):
        del user['Password']
        session['logged_in'] = True
        session['user'] = user
        return jsonify(user), 200

    def login(self):
        email = request.form.get('email')
        password = request.form.get('password')

        user = get_db().your_db.find_one({"Email": email})

        if user and pbkdf2_sha256.verify(password, user['Password']):
            del user['Password']
            session['logged_in'] = True
            session['user'] = user
            return redirect('/dashboard')
        else:
            return jsonify({"error": "Invalid email or password"}), 401

    def signup(self):
        user_data = {
            "_id": uuid.uuid4().hex,
            "Name": request.form.get('name'),
            "Surname": request.form.get('surname'),
            "Email": request.form.get('email'),
            "Password": request.form.get('password'),
            "TCKNO": request.form.get('tckimlik'),
            "DateOfBirth": request.form.get('birthday'),
            "PhoneNumber": request.form.get('phone')
        }
        existing_user = get_db().your_db.find_one({
            "$or": [
                {"Email": user_data["Email"]},
                {"TCKNO": user_data["TCKNO"]},
                {"PhoneNumber": user_data["PhoneNumber"]}
            ]
        })

        if existing_user:
            existing_field = next(field for field in ["Email", "TCKNO", "PhoneNumber"] if existing_user.get(field) == user_data[field])
            return jsonify({"error": f"{existing_field} already exists"}), 400
        
        user_data['Password'] = pbkdf2_sha256.encrypt(user_data['Password'])
        db = get_db()
        if db.your_db.insert_one(user_data):
            return self.start_session(user_data)
    
    def signout(self):
        session.clear()
        return redirect('/')

    def create_post(self):
        if 'user' not in session:
            return jsonify({"error": "Unauthorized access"}), 403

        post_data = {
            "_id": uuid.uuid4().hex,
            "title": request.form.get('title'),
            "description": request.form.get('description'),
            "content": request.form.get('content'),
            "author": session['user']['Email'],
            "created_at": datetime.datetime.utcnow()
        }

        db = get_db()
        if db.blog_db.insert_one(post_data):  # Save to blog_db collection
            return redirect(url_for('dashboard'))  # Redirect to the dashboard
        else:
            return jsonify({"error": "Failed to create post"}), 500
