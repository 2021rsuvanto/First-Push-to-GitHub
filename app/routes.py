import os
from app import app
from flask import render_template, request, redirect
from app.models import model

import io
import random
from flask import Response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure


# from flask_pymongo import PyMongo

# name of database
# app.config['MONGO_DBNAME'] = 'database-name'

# URI of database
# app.config['MONGO_URI'] = 'mongo-uri'

# mongo = PyMongo(app)


# INDEX

@app.route('/')
@app.route('/index')

def index():
     return render_template('index.html')



@app.route('/carbon_quiz', methods=["GET", "POST"])
def carbon_quiz():
    # get information from form
    user_input = dict(request.form)
    print(user_input)

    mileage_val = user_input["mileage"]
    print(mileage_val)

    car_val = user_input["car"]
    print(car_val)
    output = model.car_emissions(car_val, mileage_val)

    timesperday_val = user_input["trans per day"]
    print(timesperday_val)

    trans_val = user_input["transportation"]
    print(trans_val)
    output2 = model.trans_emissions(trans_val, timesperday_val)

    beef_val = user_input["meat per meal"]
    print(beef_val)
    output3 = model.beef_emissions(beef_val)

    computer_val = user_input["computer"]
    print(computer_val)
    output4 = model.computer_emissions(computer_val)

    light_val = user_input["light"]
    print(light_val)
    output5 = model.light_emissions(light_val)

    power_val = user_input["power usage"]
    print(power_val)
    output6 = model.excess_power_emissions(power_val)

    print ("output is", output)
    print ("output2 is", output2)
    print ("output3 is", output3)
    print ("output4 is", output4)
    print ("output5 is", output5)
    print ("output6 is", output6)

    final_result = output+output2+output3+output4+output5+output6

    return render_template('results.html', output = final_result)

    return "Keep at it!"

@app.route('/results')
def results():
    output = model.car_emissions(car_type, mileage)
    return output
    output2 = model.trans_emissions(trans_type, times_per_day)
    return output2
    output3 = model.beef_emissions(number_meals)
    return output2
    output4 = model.computer_emissions(computer_type)
    return output2
    output5 = model.light_emissions(bulb_type)
    return output2
    output6 = model.excess_power_emissions(power_type)
    return output2


@app.route('/plot.png')
def plot_png():
    # plt = create_figure()
    labels = ['Cookies', 'Jellybean', 'Milkshake', 'Cheesecake']
    sizes = [38.4, 40.6, 20.7, 10.3]
    colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']
    patches, texts = plt.pie(sizes, colors=colors, shadow=True, startangle=90)
    plt.legend(patches, labels, loc="best")
    plt.axis('equal')
    plt.tight_layout()
    plt.show()
    # output = io.BytesIO()
    bytes_image = io.BytesIO()
    plt.savefig(bytes_image, format='png')
    bytes_image.seek(0)
    return bytes_image

    # FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

    # bytes_image = io.BytesIO()
    # plt.savefig(bytes_image, format='png')
    # bytes_image.seek(0)
    # return bytes_image

def create_figure():
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    xs = range(100)
    ys = [random.randint(1, 50) for x in xs]
    axis.plot(xs, ys)
    # labels = ['Cookies', 'Jellybean', 'Milkshake', 'Cheesecake']
    # sizes = [38.4, 40.6, 20.7, 10.3]
    # colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']
    # patches, texts = plt.pie(sizes, colors=colors, shadow=True, startangle=90)
    # fig.legend(patches, labels, loc="best")
    # fig.axis('equal')
    # fig.tight_layout()
    # plt.show()
    return fig

# CONNECT TO DB, ADD DATA

# @app.route('/add')
#
# def add():
#     # connect to the database
#
#     # insert new data
#
#     # return a message to the user
#     return ""
