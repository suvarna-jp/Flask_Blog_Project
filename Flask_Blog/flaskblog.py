from flask import Flask, render_template

app = Flask(__name__)

posts = [
    {
        'author' : 'Suvarna Joshi',
        'title' : 'Blog Post 1',
        'content' : '1st post content',
        'date_posted' : 'October 6th, 2019'
    },
    {
        'author' : 'Jai Phookan',
        'title' : 'Blog Post #1',
        'content' : "Jai's 1st post content",
        'date_posted' : 'October 8th, 2019'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html", posts=posts)


@app.route('/about')
def about():
    return render_template("about.html", title="About Page")


if __name__ == '__main__':
    app.run(debug=True)