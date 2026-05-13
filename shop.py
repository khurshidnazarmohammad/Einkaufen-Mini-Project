from flask import Flask, render_template_string, request

app = Flask(name)

products = [
    {"name": "Black Sneaker Backpack", "price": 120},
    {"name": "Red Handbag", "price": 90},
    {"name": "Blue Backpack", "price": 140},
    {"name": "Green Sports Bag", "price": 110},
    {"name": "Black Leather Wallet", "price": 60},
]

HTML_TEMPLATE = """
<h1>Search Results</h1>
<ul>
{% for p in products %}
<li>{{ p.name }} - ${{ p.price }}</li>
{% endfor %}
</ul>
"""

@app.route("/")
def home():
    return open("index.html").read()

@app.route("/search")
def search():
    q = request.args.get("q", "").lower()
    results = [p for p in products if q in p["name"].lower()]
    return render_template_string(HTML_TEMPLATE, products=results)

if name == "main":
    app.run(debug=True)
