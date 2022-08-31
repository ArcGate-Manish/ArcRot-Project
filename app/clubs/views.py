from http.client import responses
from flask import jsonify, make_response
from . import club_blueprint
from .models import Club




@club_blueprint.route('/<int:id>/',methods=['GET'])
def get_club_details(id):
    club_details = Club.getClubById(id)
    details_list ={}
    if(club_details):
        details_list['id'] = club_details.id
        details_list['name'] = club_details.name
        details_list['address'] = club_details.address
        details_list['about'] = club_details.about
        details_list['email_id'] = club_details.email_id
        details_list['location'] = club_details.location
        details_list['district_code'] = club_details.district_code
        details_list['chartered'] = club_details.chartered
        details_list['phone_no'] = club_details.phone_no
        details_list['fax_no'] = club_details.fax_no
        details_list['vendors'] = club_details.vendors
        details_list['website'] = club_details.website
        details_list['rotary_langauge'] = club_details.rotary_langauge
        details_list['mailing_address'] = club_details.mailing_address
        club_members_details = {}
        for row in club_details.club_members:
            club_members_details[row.id] = {}
            club_members_details[row.id]['club_id'] = row.club_id
            club_members_details[row.id]['club_id'] = row.club_id
            club_members_details[row.id]['club_member_id'] = row.club_member_id
            club_members_details[row.id]['member_first_name'] = row.member_first_name
            club_members_details[row.id]['member_last_name'] = row.member_last_name
            club_members_details[row.id]['member_from'] = row.member_from
            club_members_details[row.id]['profile'] = row.profile
            club_members_details[row.id]['club_member_email'] = row.club_member_email
            club_members_details[row.id]['member_till'] = row.member_till
            club_members_details[row.id]['is_active'] = row.is_active
        details_list['club_members'] = club_members_details
        return jsonify(details_list)
        
    else:
        return jsonify([])



@club_blueprint.route('/list/',methods=['GET'])
def get_all_club_details():
    club_details = Club.getAllClub()
    details_list ={}
    if(club_details):
        for row in club_details:
            details_list[row.id] = {}
            details_list[row.id]['id'] = row.id
            details_list[row.id]['name'] = row.name
            details_list[row.id]['address'] = row.address
            details_list[row.id]['about'] = row.about
            details_list[row.id]['email_id'] = row.email_id
            details_list[row.id]['location'] = row.location
            details_list[row.id]['district_code'] = row.district_code
            details_list[row.id]['chartered'] = row.chartered
            details_list[row.id]['phone_no'] = row.phone_no
            details_list[row.id]['fax_no'] = row.fax_no
            details_list[row.id]['vendors'] = row.vendors
            details_list[row.id]['website'] = row.website
            details_list[row.id]['rotary_langauge'] = row.rotary_langauge
            details_list[row.id]['mailing_address'] = row.mailing_address
            club_members_details = {}
            for club_member in row.club_members:
                club_members_details[club_member.id] = {}
                club_members_details[club_member.id]['club_id'] = club_member.club_id
                club_members_details[club_member.id]['club_member_id'] = club_member.club_member_id
                club_members_details[club_member.id]['member_first_name'] = club_member.member_first_name
                club_members_details[club_member.id]['member_last_name'] = club_member.member_last_name
                club_members_details[club_member.id]['member_from'] = club_member.member_from
                club_members_details[club_member.id]['profile'] = club_member.profile
                club_members_details[club_member.id]['club_member_email'] = club_member.club_member_email
                club_members_details[club_member.id]['member_till'] = club_member.member_till
                club_members_details[club_member.id]['is_active'] = club_member.is_active
            details_list[row.id]['club_members'] = club_members_details
    response = make_response(jsonify(details_list))
    # response.headers['ngrok-skip-browser-warning'] = 'skipbrowser'
    return response