from django.shortcuts import render
from django.views.generic import View,CreateView
from django.http import JsonResponse
from .forms import RoomForm
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.forms.models import model_to_dict
from .models import HotelRoom



class  RoomList(View):
    def  get(self, *args, **kwargs):
        rooms = HotelRoom.objects.all()
        context = {
            'rooms':rooms
        }  
        return render(self.request, "rooms/index.html", context)

class  RoomDetail(View):
    def  get(self, request, pk):
        room = get_object_or_404(HotelRoom, pk=pk)
        data =  dict()
        data['room'] = model_to_dict(room)
        return JsonResponse(data)

@method_decorator(csrf_exempt, name='dispatch')
class  CreateRoom(CreateView):
    def get(self, *args, **kwargs):
        form=RoomForm()
        context={
            'create_rooms':form
        }
        return render(self.request, "rooms/create.html", context)

    def  post(self, request):
        form = RoomForm(request.POST)
        if form.is_valid():
            room = form.save()
            data['room'] = model_to_dict(room)
        else:
            data['error'] =  "form not valid!"
        return JsonResponse(data)

class  RoomUpdate(View):
    def  post(self, request, pk):
        data =  dict()
        room = HotelRoom.objects.get(pk=pk)
        form = RoomForm(instance=room, data=request.POST)
        if form.is_valid():
            room = form.save()
            data['room'] = model_to_dict(room)
        else:
            data['error'] =  "form not valid!"
        return JsonResponse(data)

class  RoomDelete(View):
    def  post(self, request, pk):
        data =  dict()
        room = HotelRoom.objects.get(pk=pk)
        if room:
            room.delete()
            data['message'] =  "Room deleted!"
        else:
            data['message'] =  "Error!"
        return JsonResponse(data)


