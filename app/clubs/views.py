from flask import jsonify, make_response
from . import club_blueprint
from .models import Club, ClubMembers


# club api for individual culb
@club_blueprint.route('/<int:id>/', methods=['GET'])
def get_club_details(id):
    club_details = Club.getClubById(id)
    details_list = []
    if (club_details):
        details_list.append({})
        details_list[-1]['id'] = club_details.id
        details_list[-1]['name'] = club_details.name
        details_list[-1]['address'] = club_details.address
        details_list[-1]['about'] = club_details.about
        details_list[-1]['email_id'] = club_details.email_id
        details_list[-1]['location'] = club_details.location
        details_list[-1]['district_code'] = club_details.district_code
        details_list[-1]['chartered'] = club_details.chartered
        details_list[-1]['phone_no'] = club_details.phone_no
        details_list[-1]['fax_no'] = club_details.fax_no
        details_list[-1]['vendors'] = club_details.vendors
        details_list[-1]['website'] = club_details.website
        details_list[-1]['rotary_langauge'] = club_details.rotary_langauge
        details_list[-1]['club_ids'] = club_details.club_ids
        details_list[-1]['club_type'] = club_details.club_type
        details_list[-1]['mailing_address'] = club_details.mailing_address
        details_list[-1]['assistant_governor'] = club_details.assistant_governor
        club_members_details = []
        for row in club_details.club_members:
            club_members_details.append({})
            club_members_details[-1]['club_id'] = row.club_id
            club_members_details[-1]['club_member_id'] = row.club_member_id
            club_members_details[-1]['member_first_name'] = row.member_first_name
            club_members_details[-1]['member_last_name'] = row.member_last_name
            club_members_details[-1]['member_from'] = row.member_from
            club_members_details[-1]['profile'] = row.profile
            club_members_details[-1]['club_member_email'] = row.club_member_email
            club_members_details[-1]['member_till'] = row.member_till
            club_members_details[-1]['is_active'] = row.club_memb_is_active
        details_list[-1]['club_members'] = club_members_details
        return jsonify(details_list)

    else:
        return jsonify([])


# club api for list of clubs
@club_blueprint.route('/list/', methods=['GET'])
def get_all_club_details():
    club_details = Club.getAllClub()
    details_list = []
    if (club_details):
        for row in club_details:
            details_list.append({})
            details_list[-1]['id'] = row.id
            details_list[-1]['name'] = row.name
            details_list[-1]['address'] = row.address
            details_list[-1]['about'] = row.about
            details_list[-1]['email_id'] = row.email_id
            details_list[-1]['location'] = row.location
            details_list[-1]['district_code'] = row.district_code
            details_list[-1]['chartered'] = row.chartered
            details_list[-1]['phone_no'] = row.phone_no
            details_list[-1]['fax_no'] = row.fax_no
            details_list[-1]['vendors'] = row.vendors
            details_list[-1]['website'] = row.website
            details_list[-1]['rotary_langauge'] = row.rotary_langauge
            details_list[-1]['club_ids'] = row.club_ids
            details_list[-1]['club_type'] = row.club_type
            details_list[-1]['mailing_address'] = row.mailing_address
            details_list[-1]['assistant_governor'] = row.assistant_governor
            club_members_details = []
            for club_member in row.club_members:
                club_members_details.append({})
                club_members_details[-1]['club_id'] = club_member.club_id
                club_members_details[-1]['club_member_id'] = club_member.club_member_id
                club_members_details[-1]['member_first_name'] = club_member.member_first_name
                club_members_details[-1]['member_last_name'] = club_member.member_last_name
                club_members_details[-1]['member_from'] = club_member.member_from
                club_members_details[-1]['profile'] = club_member.profile
                club_members_details[-1]['club_member_email'] = club_member.club_member_email
                club_members_details[-1]['member_till'] = club_member.member_till
                club_members_details[-1]['is_active'] = club_member.club_memb_is_active
            details_list[-1]['club_members'] = club_members_details
    response = make_response(jsonify(details_list))
    # response.headers['ngrok-skip-browser-warning'] = 'skipbrowser'
    return response



@club_blueprint.route('/summary')
def get_total_of_all():
    total_club = Club.getTotalClub()
    total_member = ClubMembers.getTotalMember()
    temp = {}
    temp['total_club'] = total_club
    temp['total_projects'] = 15
    temp['total_project_cost'] = 4800000 
    temp['total_member'] = total_member
    temp['total_beneficiaries'] = 22345
    return jsonify([temp])
    