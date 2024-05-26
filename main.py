from flask import Flask , request,url_for,render_template

from markupsafe import escape
app = Flask(__name__)

# def login():
#     return "<a href="url_for('login')">login</a>"


@app.route('/')
def index():
    mylist=["apel","anggur","jeruk"]
    data = {"nama" : "andi" , "umur" : 20}
    return  render_template("index.html", nama = "andi" , umur = 20, list=mylist , mydata=data)

@app.route('/about')
def about():
    return '<h1>about us<h1>'

@app.route('/contact')
def contact():
    return '<h1>contact us<h1>'

@app.route('/profile' , defaults={"_route": "home", "nilai": 0})
@app.route('/profile/<int:nilai>',defaults={'_route': "profile"})
def profile_name(nilai,_route):
    if _route=="home":
        return '<h1>profile Home<h1>'
    elif _route == 'profile':
        nilai = nilai + 100
        return "<h1>hello %s<h1>" %nilai
    
@app.route("/htmlescape/<code>")
def htmlescape(code):
    return f"hello , {escape(code)}"


@app.route("/login", methods=['GET','POST'])
def login():
    if request.method == "GET":
        return request.args.get("nama") + request.args.get("alamat")
    elif request.method == "POST":
        return request.form["nama"]





# tidak perlu mematikan mesin ketika proses develop
app.run(debug=True)