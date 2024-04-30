from flask import Flask, request, jsonify, url_for, redirect, render_template

app = Flask(__name__)

live_location = None

@app.route('/')
def index():
    return render_template('index.html')

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
        map_url = url_for('show_map', lat=latitude, lon=longitude, _external=True)
        return jsonify({'map_url': map_url})
    else:
        return jsonify({'message': 'No live location available'})

@app.route('/map')
def show_map():
    latitude = request.args.get('lat')
    longitude = request.args.get('lon')
    map_url = f'https://www.google.com/maps?q={latitude},{longitude}'
    return redirect(map_url)
