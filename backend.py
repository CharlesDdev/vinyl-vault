from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('q')  # Get the user's search query
    # Example logic: Search your database for matching records
    results = db.collection.find({"title": {"$regex": query, "$options": "i"}})
    return jsonify(list(results))
