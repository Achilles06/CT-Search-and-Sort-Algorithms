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

# Task 1: Implement Merge Sort Algorithm
def merge_sort(video_titles):
    if len(video_titles) > 1:
        mid = len(video_titles) // 2
        left_half = video_titles[:mid]
        right_half = video_titles[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                video_titles[k] = left_half[i]
                i += 1
            else:
                video_titles[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            video_titles[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            video_titles[k] = right_half[j]
            j += 1
            k += 1

    return video_titles

# Task 2: Binary search function (from previous assignment)
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

# Task 2: REST API for searching videos by title
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

# Task 3: REST API for sorting videos alphabetically using Merge Sort
@app.route('/sort_videos', methods=['GET'])
def sort_videos():
    sorted_videos = merge_sort(video_titles[:])  # Pass a copy of the list to avoid in-place sorting
    return jsonify({'sorted_videos': sorted_videos})

# Start the Flask application
if __name__ == '__main__':
    app.run(debug=True)
