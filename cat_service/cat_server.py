import random
from flask import Flask

app = Flask(__name__)

images = [
   "https://c.tenor.com/gIaioChTOloAAAAM/cat-cute.gif",
   "https://c.tenor.com/ZhfMGWrmCTcAAAAM/cute-kitty-best-kitty.gif",
   "https://hips.hearstapps.com/digitalspyuk.cdnds.net/16/21/1464342455-typing-cat-gif.gif?resize=480:*",
   "https://cdn.shopify.com/s/files/1/0252/5199/files/giphy_large.gif?15549719145083383900",
   "https://www.gifcen.com/wp-content/uploads/2021/03/cat-gif-6.gif"
]

@app.route('/')
def get_cat_gif():
    cat_url = random.choice(images)
    return { 'cat_url': cat_url }

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5001')