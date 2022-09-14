from datetime import datetime
from os import rename
from flask import url_for, redirect, request, abort
from flask_security import current_user
from flask_admin.contrib import sqla
from flask_admin import BaseView, expose, form
from sqlalchemy import func
from sqlalchemy.orm import joinedload
from .. import app, ClubMembers, db
import PIL
import os.path as op
from werkzeug.utils import secure_filename
from wtforms.validators import DataRequired,InputRequired
# Create customized model view class
from flask_admin.form import ImageUploadField
import time

class MyModelView(sqla.ModelView):

    def is_accessible(self):
        if not current_user.is_active or not current_user.is_authenticated:
            return False

        if current_user.has_role('superuser'):
            return True

        return False

    def _handle_view(self, name, **kwargs):
        """
        Override builtin _handle_view in order to redirect users when a view is not accessible.
        """
        if not self.is_accessible():
            if current_user.is_authenticated:
                # permission denied
                abort(403)
            else:
                # login
                return redirect(url_for('security.login', next=request.url))

    # can_edit = True
    edit_modal = True
    create_modal = True
    can_export = False
    can_view_details = True
    details_modal = True


class UserView(MyModelView):
    # column_editable_list = ['email', 'first_name', 'last_name']
    # column_searchable_list = column_editable_list
    # column_exclude_list = ['user_created_at','updated_at']
    form_excluded_columns = ['user_created_at', 'updated_at']
    # column_details_exclude_list = column_exclude_list
    # column_filters = column_editable_list


class ClubView(MyModelView):
    form_excluded_columns = ['created_at', 'updated_at']


class ClubMemberView(MyModelView):
    form_excluded_columns = ['created_at', 'updated_at']

################################################################
#                       ADD COSTUM FIELD
################################################################
    
    def prefix_name(obj, file_data):
        timestr = time.strftime("%Y%m%d-%H%M%S")
        parts = op.splitext(file_data.filename)
        return secure_filename(f"clubmember_{obj.club_member_id}")
    form_extra_fields = {
        'profile_picture': form.ImageUploadField('Profile Image (Please Upload file with .jpg, .jpeg, .png )',
                                      base_path=app.config['PROFILE_IMAGES_UPLOADS_DIR'],
                                      thumbnail_size=(100, 100, True), namegen=prefix_name,validators=[DataRequired(),InputRequired()])
    }


class AuthorView(MyModelView):
    form_excluded_columns = ['created_at', 'updated_at']


class RoleView(MyModelView):
    form_excluded_columns = ['role_created_at', 'updated_at']


class TagView(MyModelView):
    form_excluded_columns = ['tag_created_at', 'updated_at']


class PostView(MyModelView):
    form_excluded_columns = ['post_created_at', 'updated_at']


class PostImagesView(MyModelView):
    form_excluded_columns = ['post_image_created_at', 'updated_at']


class CustomView(BaseView):
    @expose('/')
    def index(self):
        return self.render('admin/custom_index.html')
