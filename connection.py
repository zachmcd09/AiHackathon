@app.route('/content/fetch', methods=['GET'])
def fetchContent():
    # Retrieve study materials from the database
    
    user_preferences = request.args.get('user_preferences')
    criteria = request.args.getlist('criteria')

    content_data = Content.query.filter(*criteria).all()

    return jsonify(content_data)


@app.route('/register', methods=['POST'])
def registerUser():
    # Store user information in the database
    
    username = request.form.get('username')
    password = request.form.get('password')
    email = request.form.get('email')
    preferences = request.form.get('preferences')
    progress_data = { 'completed': [], 'favorites': [] }
    
    user = User(username, password, email, preferences)
    db.session.add(user)
    db.session.commit()

    return jsonify({'message': 'User registered successfully.'})

@app.route('/content/update', methods=['POST'])
def updateContent():
    # Modify existing study materials
