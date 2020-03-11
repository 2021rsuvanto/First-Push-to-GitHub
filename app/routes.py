import os
from app import app
from flask import render_template, request, redirect
from app.models import model
from flask import Flask

import io
import random
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.image as mpimg
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
    print ("final result is", final_result)

    outputs = {
      "output": output,
      "output2": output2,
      "output3": output3,
      "output4": output4,
      "output5": output5,
      "output6": output6
    }

    print("Percentages for each value in the dictionary:")
    final_result_average = {}
    for num in outputs:
        final_result_average[num] = 100*(outputs[num]/final_result)
        # percentage = final_result_average[num]*100
    print (final_result_average)




    a = int(output); b = int(output2); c = int(output3); d = int(output4); e = int(output5); f = int(output6)
    if a>b and a>c and a>d and a>e and a>f:
        advice = "If you cut down on the number of miles you drive in a day, you will emit significantly less carbon into the atmosphere, based on your current habits."
    elif b>a and b>c and b>d and b>e and b>f:
        advice = "If you cut down on the amount you ride buses, cars, and/or airplanes in a day, you will emit significantly less carbon into the atmosphere, based on your current habits."
    elif c>a and c>b and c>d and c>e and c>f:
        advice = "If you cut down on the amount of beef you consume in a day, you will emit significantly less carbon into the atmosphere, based on your current habits."
    elif d>a and d>b and d>c and d>e and d>f:
        advice = "If you cut down on the number of hours you spend on a computer in a day, and/or change the type of computer you use to a more environmentally friendly product, you will emit significantly less carbon into the atmosphere, based on your current habits."
    elif e>a and e>b and e>c and e>d and e>f:
        advice = "If you make the switch to LED lightbulbs throughout your home, you will emit significantly less carbon into the atmosphere, based on your current habits."
    elif f>a and f>b and f>c and f>d and f>e:
        advice = "If you turn off the lights when you exit different rooms, you will emit significantly less carbon into the atmosphere, based on your current habits."


    # png = plot_png()
    return render_template('results.html', final_result = final_result, final_result_average = final_result_average, advice = advice)


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


@app.route('/products')
def products():
    return render_template('products.html')


#calling plastic quiz
@app.route('/plastic')
def plastic():
    return render_template('plastic_quiz.html')



#handling plastic quiz
@app.route('/plastic_quiz', methods=["GET", "POST"])
def plastic_quiz():
    user_input = dict(request.form)
    print(user_input)
    # return "These are plastic quiz results"


    plates_val = user_input["plates"]
    print(plates_val)
    platipus = plates_val


    cup_val = user_input["cup"]
    print(cup_val)
    platipus2 = cup_val


    shopping_bag_val = user_input["shopping bag"]
    print(shopping_bag_val)
    platipus3 = shopping_bag_val


    produce_bag_val = user_input["produce bag"]
    print(produce_bag_val)
    platipus4 = produce_bag_val


    straws_val = user_input["straws"]
    print(straws_val)
    platipus5 = straws_val


    wrapfoil_val = user_input["wrap/foil"]
    print(wrapfoil_val)
    platipus6 = wrapfoil_val


    fast_food_val = user_input["fast food"]
    print(fast_food_val)
    platipus7 = fast_food_val


    print ("platipus is", platipus)
    print ("platipus2 is", platipus2)
    print ("platipus3 is", platipus3)
    print ("platipus4 is", platipus4)
    print ("platipus5 is", platipus5)
    print ("platipus6 is", platipus6)
    print ("platipus7 is", platipus7)

    advice = ""

    if platipus == "plastic" or "paper":
        advice += "If you eat off of glass plates and cut down on the number of plastic or paper plates you buy, your negative impact on the environment will greatly decrease, based on your current plastic-usage habits. I know washing dishes is a pain, but in the end, it is worth it!"

    if platipus2 == "No":
        advice += "<br><br>If you cut down on the number of plastic and paper cups you use and instead bring portable beverage bottles when purchasing coffee and other drinks, your negative impact on the environment will greatly decrease, based on your current plastic-usage habits. I know washing dishes is a pain, but in the end, it is worth it!"

    if platipus3 == "No":
        advice += "<br><br>If you cut down on the number of plastic and paper bags you use and instead bring reusable shopping bags when shopping for food, etc., your negative impact on the environment will greatly decrease, based on your current plastic-usage habits."

    if platipus4 == "No":
        advice += "<br><br>If you cut down on the number of plastic and paper bags you use and instead bring reusable produce bags when grocery shopping, your negative impact on the environment will greatly decrease, based on your current plastic-usage habits."

    if platipus5 == "Plastic" or "Paper":
        advice += "<br><br>If you make the switch to stainless steel straws, silicon straws, or using no straws at all, your negative impact on the environment will greatly decrease, based on your current plastic-usage habits. I know washing reusable straws is a pain, but in the end, it is worth it!"

    if platipus6 == "Yes":
        advice += "<br><br>If you cut down on the amount you use parchment paper, alumnium foil, and plastic wrap, your negative impact on the environment will greatly decrease, based on your current plastic-usage habits."

    if platipus7 == "Yes" or "Sometimes":
        advice += "<br><br>If you cut down on the amount you eat at fast food restuarants, your negative impact on the environment will greatly decrease, based on your current plastic-usage habits."

    return render_template('results2.html', advice = advice)



# @app.route('/plot.png')
# def plot_png():
#     fig = create_figure()
#     output = io.BytesIO()
#     FigureCanvas(fig).print_png(output)
#     return Response(output.getvalue(), mimetype='image/png')
#
# def create_figure():
#     fig = Figure()
#     axis = fig.add_subplot(1, 1, 1)
#     xs = range(100)
#     ys = [random.randint(1, 50) for x in xs]
#     axis.plot(xs, ys)
#     return fig






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
