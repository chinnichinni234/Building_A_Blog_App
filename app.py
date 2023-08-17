from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Temporary data store for blog posts (replace this with a database later)
posts = [
    {"title": "First Post", "content": "This is the content of the first post."},
    {"title": "Second Post", "content": "This is the content of the second post."},
    # Add more posts as needed
]

# Routes
@app.route('/')
def home():
    return render_template('home.html', posts=posts)

@app.route('/post/<int:post_id>')
def post(post_id):
    post = posts[post_id - 1]
    return render_template('post.html', post=post)

@app.route('/create', methods=['GET', 'POST'])
def create_post():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        posts.append({"title": title, "content": content})
        return redirect(url_for('home'))
    return render_template('create_post.html')

if __name__ == '__main__':
    app.run(debug=True)
