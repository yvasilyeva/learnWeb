from flask import Flask, render_template
from weather import weather_in_city
from python_org_news import get_python_news
app=Flask(__name__)
@app.route("/")
def index():
	page_title="Python news"
	weather=weather_in_city("Geneva,Switzerland")
	news=get_python_news()
	return render_template('index.html',title=page_title,weather=weather, news_list=news)

if __name__=="__main__":
	app.run(debug=True)
