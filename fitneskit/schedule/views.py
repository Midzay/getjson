
from .models import Schedule
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ScheduleSerializer


@api_view(['GET'])
def get_group_lessons_v2(request):
    try:
        data = Schedule.objects.all()
    except Schedule.DoesNotExist:
        return HttpResponse(status=404)
    serializer = ScheduleSerializer(data, many=True)
    return Response(serializer.data)
