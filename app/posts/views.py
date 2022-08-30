from flask import jsonify
from . import post_blueprint
from .models import Post




@post_blueprint.route('/<int:id>/',methods=['GET'])
def get_post_details(id):
    post_details = Post.getPostById(id)
    details_list ={}
    if(post_details):
        details_list['id'] = post_details.id
        details_list['author_id'] = post_details.author_id
        details_list['title'] = post_details.title
        details_list['content'] = post_details.content
        details_list['cover_image_name'] = post_details.cover_image_name
        details_list['created_at'] = post_details.created_at
        post_images_details = {}
        for row in post_details.post_images:
            post_images_details[row.id] = {}
            post_images_details[row.id]['id'] = row.id
            post_images_details[row.id]['post_id'] = row.post_id
            post_images_details[row.id]['image_name'] = row.image_name
        details_list['post_images'] = post_images_details
        post_tags_details ={}
        for row in post_details.post_tags:
            post_tags_details[row.id] = {}
            post_tags_details[row.id]['id'] = row.id
            post_tags_details[row.id]['name'] = row.name
        details_list['post_tags'] = post_tags_details
        return jsonify(details_list)
    else:
        return jsonify([])



@post_blueprint.route('/list/',methods=['GET'])
def get_all_post_details():
    post_details = Post.getAllPost()
    print(post_details)
    details_list ={}
    if(post_details):
        for row in post_details:
            details_list[row.id] = {}
            details_list[row.id]['id'] = row.id
            details_list[row.id]['author_id'] = row.author_id
            details_list[row.id]['title'] = row.title
            details_list[row.id]['content'] = row.content
            details_list[row.id]['cover_image_name'] = row.cover_image_name
            details_list[row.id]['created_at'] = row.created_at
            post_images_details ={}
            for post_images in row.post_images:
                post_images_details[post_images.id] = {}
                post_images_details[post_images.id]['post_id'] = post_images.post_id
                post_images_details[post_images.id]['image_name'] = post_images.image_name
                post_images_details[post_images.id]['created_at'] = post_images.created_at
                post_images_details[post_images.id]['updated_at'] = post_images.updated_at
            details_list[row.id]['post_images'] = post_images_details
            post_tags_details = {}
            for post_tags in row.post_tags:
                post_tags_details[post_tags.id] = {}
                post_tags_details[post_tags.id]['id'] = post_tags.id
                post_tags_details[post_tags.id]['name'] = post_tags.name
                post_tags_details[post_tags.id]['created_at'] = post_tags.created_at
                post_tags_details[post_tags.id]['updated_at'] = post_tags.updated_at
            details_list[row.id]['post_tags'] = post_tags_details
        return jsonify(details_list)
    else:
        return jsonify([])
