from flask import Flask, jsonify, request, redirect
from app.models import stored_urls, URLShortener
from app.utils import short_url, validate_url
from app.config import Config

app = Flask(__name__)

@app.route('/')
def health_check():
    return jsonify({
        "status": "healthy",
        "service": "URL Shortener API"
    })

@app.route('/api/health')
def api_health():
    return jsonify({
        "status": "ok",
        "message": "URL Shortener API is running"
    })

@app.route('/api/shorten', methods = ['POST'])
def shorten_url():
    long_url = request.json.get("url")

    if not long_url:
        return jsonify({"error":"Missing Url"}),404

    if not validate_url(long_url):
        return jsonify({"error": "Invalid Url"}),400

    else:
        shortened_code = short_url(long_url)
        shortened_link = f"{Config.backend_url}/{shortened_code}"

        stored_urls[shortened_code] = URLShortener(long_url)
        return jsonify({
            "short_code": shortened_code,
            "shortened_url":shortened_link}), 200

@app.route('/<short_code>', methods = ['GET'])
def redirect_to_long_url(short_code):
    url = stored_urls.get(short_code)
    if url:
        url.clicks += 1
        return  redirect(url.long_url, code = 302)
    else:
        return jsonify({"error":"Not found"}), 404

@app.route('/api/stats/<short_code>', methods = ['GET'])
def stats(short_code):
    obj = stored_urls.get(short_code)
    if obj :
        return obj.to_dict()
    return jsonify({'error': 'Not found'}), 404



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
