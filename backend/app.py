from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)

# Use "mongo" as the hostname, matching the Docker Compose service name.
client = MongoClient("mongodb://mongo_db:27017/")
db = client['resume_builder']
collection = db['resumes']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_resume', methods=['POST'])
def generate_resume():
    data = {
        'name': request.form.get('name'),
        'address': request.form.get('address'),
        'contact': request.form.get('contact'),
        'working_details': request.form.get('working_details'),  # "Profile"
        'current_details': request.form.get('current_details'),  # "Title" or "Position"
        'color': request.form.get('color'),
        'work_experience': request.form.getlist('work_experience[]'),
        'education': request.form.getlist('education[]'),
        'projects': request.form.getlist('projects[]')
    }
    resume_id = collection.insert_one(data).inserted_id
    return redirect(url_for('resume', resume_id=str(resume_id)))

@app.route('/resume/<resume_id>')
def resume(resume_id):
    resume_data = collection.find_one({'_id': ObjectId(resume_id)})
    return render_template('resume.html', resume=resume_data)

@app.route('/edit/<resume_id>')
def edit(resume_id):
    resume_data = collection.find_one({'_id': ObjectId(resume_id)})
    return render_template('edit.html', resume=resume_data)

@app.route('/update_resume/<resume_id>', methods=['POST'])
def update_resume(resume_id):
    updated_data = {
        'name': request.form.get('name'),
        'address': request.form.get('address'),
        'contact': request.form.get('contact'),
        'working_details': request.form.get('working_details'),
        'current_details': request.form.get('current_details'),
        'color': request.form.get('color'),
        'work_experience': request.form.getlist('work_experience[]'),
        'education': request.form.getlist('education[]'),
        'projects': request.form.getlist('projects[]')
    }
    collection.update_one({'_id': ObjectId(resume_id)}, {'$set': updated_data})
    return redirect(url_for('resume', resume_id=resume_id))

if __name__ == '__main__':
    # Listen on port 5000 by default
    app.run(debug=True, port=5000, host='0.0.0.0')
