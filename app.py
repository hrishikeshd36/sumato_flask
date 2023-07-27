from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    data =[
        ("01-01-2020", 1597),
        ("02-01-2020", 1456),
        ("03-01-2020", 1908),
        ("04-01-2020", 896),
        ("05-01-2020", 755),
        ("06-01-2020", 453),
        ("07-01-2020", 1100),
        ("08-01-2020", 1235),
        ("09-01-2020", 1478),
    ]

    labels = [] 
    values = []
    for row in data:
        labels.append(row[0])
        values.append(row[1])

    return render_template("graph.html", labels=labels, values=values)

if __name__ == '__main__':
    # Run the application on the local development server ##
    app.run(debug=True)