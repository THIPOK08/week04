from flask import Flask, render_template

app = Flask(__name__)

# --- Route หลัก ---
@app.route('/')
def index():
    title = 'Home Page'
    return render_template('index.html', title=title)

# --- Route เกี่ยวกับฉัน ---
@app.route('/about')
def about():
    title = 'About Page'
    name = 'Thipok salthirat'
    email = 'std.67122420209@ubu.ac.th'
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

# --- Route อาหารโปรด (แก้ไขการส่งตัวแปร) ---
@app.route('/favorite_food')
def favorite_food():
    title = 'Favorite Foods'
    # รายการอาหาร
    foods = ['หมูทอด', 'ไก่ทอด', 'ไข่เจียว'] 
    
    return render_template(
        'favorite_food.html',
        title=title,
        foods=foods  # ส่งตัวแปรเป็น 'foods' เพื่อให้ใช้ใน template ได้
    )

# --- Route ภาพยนตร์โปรด (เพิ่มใหม่ตามโจทย์) ---
@app.route('/favorite_movies')
def favorite_movies():
    title = 'Favorite Movies'
    # ภาพยนตร์/ละครที่ชื่นชอบ 5 เรื่อง
    movies = [
        'The Shawshank Redemption',
        'Inception',
        'Parasite (ชนชั้นปรสิต)',
        'Game of Thrones (Series)',
        'Breaking Bad (Series)'
    ]
    
    return render_template(
        'favorite_movies.html',
        title=title,
        movies=movies
    )


if __name__ == '__main__':
    app.run(debug=True)