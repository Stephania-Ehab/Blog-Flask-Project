from flask_restful import fields


creator_serilizer ={
    "id": fields.Integer,
    "name": fields.String
}

posts_serializers = {
    'id' : fields.Integer,
    'title' : fields.String,
    'description' : fields.String,
    'image' : fields.String,
    'creator_id' : fields.Integer,
    "creator" :fields.Nested(creator_serilizer),

}