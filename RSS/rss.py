from flask import  Flask,Request,render_template,flash,request
app = Flask(__name__)
app.config['SECRET_KEY'] = 'any secret string'
import feedparser
feednews=feedparser.parse('http://feeds.bbci.co.uk/news/rss.xml')
f=feednews.keys()
entry=feednews.entries[2]
print(entry)
message = []
for index, entry in enumerate(feednews.entries):
    post={}
    post["rank"] = index + 1
    post["title"] = entry.title
    post["link"] = entry.link
    post["summary"] = entry.summary
    message.append(post)


@app.route('/')
def index():
    return render_template('rss.html',msg=message)




if __name__ == '__main__':
    app.run(debug=True)
