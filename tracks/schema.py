from datetime import datetime
from ninja import Schema, ModelSchema
from ninja.orm import create_schema
from tracks.models import Track


TrackSchema = create_schema(Track, fields=['title', 'last_play', 'artist', 'duration'])

# class TrackSchema(ModelSchema):
#     class Config:
#         model = Track
#         model_fields = ['title', 'last_play', 'artist', 'duration']

class NotFoundSchema(Schema):
    message: str

# class TrackSchema(Schema):
#     title: str
#     artist: str
#     duration: float
#     last_play: datetime