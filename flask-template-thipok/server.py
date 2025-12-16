from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    title = 'Home Page'
    return render_template('index.html', title=title)

@app.route('/about')
def about():
    title = 'About Page'
    name = 'Thipok salthirat'
    email = 'std.67122420209@ubru.ac.th'
    mobile = '0617050165'
    age = 19

    return render_template(
        'about.html',
        title=title,
        name=name,
        email=email,
        mobile=mobile,
        age=age
     )
@app.route('/favorite_food')
def favorite_food():
  title= 'Favorite Foods'
  food = ('หมูทอด','ไก่ทอด','ไข่เจียว')
  return render_template(
        'Favorite Foods',
        หมูทอด=หมูทอด,ไก่ทอด=ไก่ทอด,ไข่เจียว=ไข่เจียว
     )
if __name__ == '__main__':
    app.run(debug=True)
