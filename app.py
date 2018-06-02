from flask import Flask, render_template, request
import json


# заглушка, получает данные из файла, имитует бд
def get_data_from_file():
    file = open("output.json", 'r')
    file_data = file.read()
    return json.loads(file_data)


# ещё одна заглушка, имитирующая получение данных из бд
def get_data_by_author(author_name):
    author_posts = []
    for post in data:
        if post['author'] == author_name:
            author_posts.append(post)
    return author_posts


app = Flask(__name__)
data = get_data_from_file()  # заменить изначальной инициализацией бд


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/author')
def author():
    author_name = request.args.get("author")
    author_posts = get_data_by_author(author_name)  # нужно заменить на получение аналогичных данных из бд
    year = 2016
    visualisation_data = {}
    while year <= 2018:
        visualisation_data[str(year)] = 0
        for post in author_posts:
            if str(year) in post['date']:
                visualisation_data[str(year)] += 1
        print(str(year), visualisation_data[str(year)])
        year += 1
    return render_template("author.html",
                           author=author_name,
                           data=author_posts,
                           visualisation_data=visualisation_data)


if __name__ == '__main__':
    app.run()
