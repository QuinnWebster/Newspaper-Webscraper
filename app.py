from flask import Flask, render_template

app = Flask(__name__)

# Static sample summary for testing
sample_summary = "This is a sample summary."

@app.route('/')
def index():
    # Render the HTML template and pass the sample summary to it
    return render_template('index.html', summary=sample_summary)

if __name__ == '__main__':
    app.run(debug=True)
