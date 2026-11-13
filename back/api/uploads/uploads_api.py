from flask import Blueprint, request, send_from_directory, abort

uploads_api = Blueprint('uploads', __name__)

@uploads_api.route('/')
def get_upload():
   name = request.args.get("name")
   if not name:
      abort(400)
   return send_from_directory('uploads', name)
