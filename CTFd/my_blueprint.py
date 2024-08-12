from flask import Blueprint, render_template, request, jsonify
from CTFd.utils.helpers import get_infos
from CTFd.utils.scores import get_standings
from CTFd.models import Users

import datetime

# Create a Blueprint instance
my_blueprint = Blueprint('my_blueprint', __name__)

# Define a new route within the Blueprint
@my_blueprint.route('/new_route')
def new_route():
    return render_template('test.html')


@my_blueprint.route('/get_data')
def get_Data():
    standings = get_standings()

    current_time = datetime.datetime.now()
    hours = (current_time.hour + 8)%24
    minutes = current_time.minute
    seconds = current_time.second
    
    data = {
        # 'standings': standings[0][3],
        'timestamp': f"{hours:02d}:{minutes:02d}:{seconds:02d}"
    }

    for i, item in enumerate(standings, start=1):
        # print("------------------------------------",str(item[3]))
        data[f'{item[2]}'] = str(item[3])
    # for i, item in enumerate(items_to_add, start=1):
    #     data[f'item_{i}'] = item
    
    
    return jsonify(data)