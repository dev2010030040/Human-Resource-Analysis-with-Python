from flask import Flask, render_template
from flask_assets import Bundle, Environment
import pandas as pd
import json
import plotly
import plotly.express as px

app = Flask(__name__)

js = Bundle('style.css')

assets = Environment(app)

assets.register('main_js',js)

test = pd.read_csv('aug_test.csv')
train = pd.read_csv('aug_train.csv')
missing_value = 100 * train.isnull().sum()/len(train)
missing_value = missing_value.reset_index()
missing_value.columns = ['variables','missing values in percentage']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/chart1')
def chart1():

    fig = px.imshow(train.isnull().T)
    fig.update_layout(title='Missing values in data set')
    #fig.show()
    
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    header="chart1"
    description = "temp1"
    return render_template('notdash2.html', graphJSON=graphJSON, header=header,description=description)

@app.route('/chart2')
def chart2():
    plot_city = train['city'].value_counts()[0:50].reset_index()
    plot_city.columns = ['City','Count']
    px.bar(plot_city,x='City',y='Count',title='City',color='Count')
    fig = px.bar(plot_city,x='City',y='Count',template='gridon',title='City',color='Count')
    fig.update_layout(title_text='plot_city',title_y=0.5)

    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    header="chart2"
    description = "temp2"
    return render_template('notdash2.html', graphJSON=graphJSON, header=header,description=description)


@app.route('/chart3')
def chart3():
    plot_cdi =train['city_development_index'].value_counts().reset_index()[0:50] 
    plot_cdi.columns = ['cdi','Count']
    plot_cdi['cdi'] = plot_cdi['cdi'].astype('str')
    fig = px.bar(plot_cdi,y="Count", x="cdi",color='Count',title='City development index')

    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    header="chart3"
    description = "temp3"
    return render_template('notdash2.html', graphJSON=graphJSON, header=header,description=description)


@app.route('/chart4')
def chart4():
    plot_gender = train['enrolled_university'].value_counts().reset_index()
    plot_gender.columns = ['enrolled_university','count']
    fig = px.pie(plot_gender,values='count',names='enrolled_university',title='enrolled_university')

    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    header="chart4"
    description = "temp4"
    return render_template('notdash2.html', graphJSON=graphJSON, header=header,description=description)

@app.route('/chart5')
def chart5():
    plot_gender = train['education_level'].value_counts().reset_index()
    plot_gender.columns = ['education_level','count']
    fig = px.pie(plot_gender,values='count',names='education_level',title='education_level')

    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    header="chart5"
    description = "temp5"
    return render_template('notdash2.html', graphJSON=graphJSON, header=header,description=description)


@app.route('/chart6')
def chart6():
    plot_gender = train['major_discipline'].value_counts().reset_index()
    plot_gender.columns = ['major_discipline','count']
    fig = px.pie(plot_gender,values='count',names='major_discipline',title='Major discipline')

    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    header="chart6"
    description = "temp6"
    return render_template('notdash2.html', graphJSON=graphJSON, header=header,description=description)

@app.route('/chart7')
def chart7():
    plot_gender = train['company_size'].value_counts().reset_index()
    plot_gender.columns = ['company_size','count']
    fig = px.pie(plot_gender,values='count',names='company_size',title='company_size is determined by no. of people employees')

    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    header="chart7"
    description = "temp7"
    return render_template('notdash2.html', graphJSON=graphJSON, header=header,description=description)


if __name__ == "__main__":
    app.run(debug=True)



    