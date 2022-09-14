from crypt import methods
from operator import methodcaller
from tkinter.messagebox import RETRY
from flask import jsonify
from . import event_blueprint
from . models import Event



@event_blueprint.route('/<int:id>', methods= ['GET'])
def get_event_details(id):
    event_details =Event.getEventById(id)
    details_list ={}
    details_list['id'] = event_details.id
    details_list['title'] = event_details.title
    details_list['time'] = event_details.time
    details_list['address'] = event_details.address 
    return jsonify([details_list])


@event_blueprint.route('/list', methods = ['GET'])
def get_all_event_details ():
    event_details = Event.getAllEvent()
    detalis_list =[]
    if (event_details):
        for row in event_details:
            detalis_list.append({})
            detalis_list[-1]['id'] = row.id
            detalis_list[-1]['title'] = row.title
            detalis_list[-1]['time'] = row.time
            detalis_list[-1]['address'] = row.address
        return jsonify (detalis_list)
    else:
        return jsonify([])



