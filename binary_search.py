from flask import Flask, request, jsonify

app = Flask(__name__)

# Sorted list of video titles
video_titles = [
    "The Art of Coding",
    "Exploring the Cosmos",
    "Cooking Masterclass: Italian Cuisine",
    "History Uncovered: Ancient Civilizations",
    "Fitness Fundamentals: Strength Training",
    "Digital Photography Essentials",
    "Financial Planning for Beginners",
    "Nature's Wonders: National Geographic",
    "Artificial Intelligence Revolution",
    "Travel Diaries: Discovering Europe"
]

# Binary search function
def binary_search(video_titles, search_title):
    low = 0
    high = len(video_titles) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_title = video_titles[mid]

        if mid_title == search_title:
            return mid  # Found the video
        elif mid_title < search_title:
            low = mid + 1
        else:
            high = mid - 1

    return -1  # Not found

# REST API endpoint for searching videos by title
@app.route('/search_video', methods=['GET'])
def search_video():
    query = request.args.get('title')
    if not query:
        return jsonify({'error': 'No search query provided'}), 400

    index = binary_search(video_titles, query)
    
    if index != -1:
        return jsonify({'title': video_titles[index]})
    else:
        return jsonify({'error': 'Video not found'}), 404

# Start the Flask application
if __name__ == '__main__':
    app.run(debug=True)
