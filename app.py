from flask import Flask, request, jsonify

app = Flask(__name__)

# Store the live location
live_location = None

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/location', methods=['POST'])
def location():
    global live_location
    data = request.json
    live_location = data.get('location')
    return jsonify({'message': 'Location updated successfully'})

@app.route('/live_location')
def get_live_location():
    global live_location
    if live_location:
        latitude = live_location.get('latitude')
        longitude = live_location.get('longitude')
        # Construct Google Maps URL with latitude and longitude
        map_url = f'https://www.google.com/maps?q={latitude},{longitude}'
        return jsonify({'map_url': map_url})
    else:
        return jsonify({'message': 'No live location available'})

if __name__ == '__main__':
    app.run(debug=True, ssl_context=('cert.pem', 'key.pem'))
