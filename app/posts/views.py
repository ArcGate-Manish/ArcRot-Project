from flask import jsonify
from . import post_blueprint
from .models import Post


@post_blueprint.route('/<int:id>/', methods=['GET'])
def get_post_details(id):
    post_details = Post.getPostById(id)
    details_list = []
    if (post_details):
        details_list.append({})
        details_list[-1]['id'] = post_details.id
        details_list[-1]['author_id'] = post_details.author_id
        details_list[-1]['title'] = post_details.title
        details_list[-1]['content'] = post_details.content
        details_list[-1]['cover_image_name'] = post_details.cover_image_name
        details_list[-1]['created_at'] = post_details.post_created_at
        post_images_details = []
        for row in post_details.post_images:
            post_images_details.append({})
            post_images_details[-1]['id'] = row.id
            post_images_details[-1]['post_id'] = row.post_id
            post_images_details[-1]['image_name'] = row.image_name
        details_list[-1]['post_images'] = post_images_details
        post_tags_details = []
        for row in post_details.post_tags:
            post_tags_details.append({})
            post_tags_details[-1]['id'] = row.id
            post_tags_details[-1]['name'] = row.name
        details_list[-1]['post_tags'] = post_tags_details
        return jsonify(details_list)
    else:
        return jsonify([])


@post_blueprint.route('/list/', methods=['GET'])
def get_all_post_details():
    post_details = Post.getAllPost()
    print(post_details)
    details_list = []
    if (post_details):
        for row in post_details:
            details_list.append({})
            details_list[-1]['id'] = row.id
            details_list[-1]['author_id'] = row.author_id
            details_list[-1]['title'] = row.title
            details_list[-1]['content'] = row.content
            details_list[-1]['cover_image_name'] = row.cover_image_name
            details_list[-1]['created_at'] = row.post_created_at
            post_images_details = []
            for post_images in row.post_images:
                post_images_details.append({})
                post_images_details[-1]['post_id'] = post_images.post_id
                post_images_details[-1]['image_name'] = post_images.image_name
                post_images_details[-1]['created_at'] = post_images.post_image_created_at
                post_images_details[-1]['updated_at'] = post_images.updated_at
            details_list[-1]['post_images'] = post_images_details
            post_tags_details = []
            for post_tags in row.post_tags:
                post_tags_details.append({})
                post_tags_details[-1]['id'] = post_tags.id
                post_tags_details[-1]['name'] = post_tags.name
                post_tags_details[-1]['created_at'] = post_tags.tag_created_at
                post_tags_details[-1]['updated_at'] = post_tags.updated_at
            details_list[-1]['post_tags'] = post_tags_details
        return jsonify(details_list)
    else:
        return jsonify([])
