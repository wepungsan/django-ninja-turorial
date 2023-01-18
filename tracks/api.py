from typing import List, Optional
from ninja import NinjaAPI
from tracks.models import Track
from tracks.schema import TrackSchema, NotFoundSchema

api = NinjaAPI()

@api.get("/tracks", response=List[TrackSchema])
def tracks(request, title: Optional[str] = None):
    if title:
        return Track.objects.filter(title__icontains=title)
    return Track.objects.all()


@api.get("/track/{track_id}", response={200: TrackSchema, 404: NotFoundSchema})
def track(request, track_id: int):
    try:
        track = Track.objects.get(pk=track_id)
        return 200, track
    except Track.DoesNotExist as e:
        return 404, {"message":"Track does not exist"}

# @api.get("/test")
# def test(request):
#     return {'test':'success'}