from django.shortcuts import render, redirect
from .forms import MainForm
from .models import MainModel
from django.core.paginator import Paginator
from django.http import JsonResponse
from PIL import Image
import os
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings
from config.settings import BASE_DIR
# Create your views here.
def index_view(request) :
    form = MainForm(request.POST or None, request.FILES)
    done = MainModel.objects.filter(status=True)
    paginator = Paginator(list(MainModel.objects.all()), 4)
    try :
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
    except:
        page_obj = paginator.get_page(1)

    if request.method == "POST" :
        print(request.POST)
        if form.is_valid() :
            print("hello")
            # header = form.cleaned_data['header']
            # description = form.cleaned_data['description']

            # # if request.POST['image'] :
            # # print(request.POST["image 
            # # data = request.FILES['image'] # or self.files['image'] in your form
            # data = request.FILES['image']
            # path = default_storage.save(request.FILES['image'].__str__(), ContentFile(data.read()))
            # tmp_file = os.path.join(settings.MEDIA_ROOT, path) 
            # print("amongus")

            # try :
            #     if request.POST['status'] == "on" :
            #         status = True 
            # except:
            #     status = False
            # newtask = MainModel(header=header, description=description, status=status)
            form.save()
    return render(request, "index.html", context={"form": form, "db": page_obj, "page_obj": page_obj, "done": done}) 
def status_view(request, pk):
    done_task = MainModel.objects.get(id=pk)
    print(done_task.status)
    if done_task.status :
        done_task.status = False
        done_task.save()
    else:
        done_task.status = True
        done_task.save()
    return redirect(index_view)
def deleting_done_view(request):
    done = MainModel.objects.filter(status=True)
    return render(request, "delete_done.html", context={"done": done})
def goodbye_data_view(request):
    done = MainModel.objects.filter(status=True).delete()
    return redirect(index_view)
def edit_view(request, pk):
    editable = MainModel.objects.get(id=pk)
    form = MainForm(request.POST or None, initial={"header":editable.header, "description":editable.description})
    if request.method == "POST" :
        print(request.POST)
        if form.is_valid() :
            
            header = form.cleaned_data['header']
            description = form.cleaned_data['description']
            try :
                if request.POST['status'] == "on" :
                    status = True 
            except:
                status = False
            editable.header = header
            editable.description = description
            editable.status = status
            editable.save()
            return redirect("/")
    return render(request, "edit.html", context={"form":form, "status":editable.status})
    print(editable)
def ask_to_delete_view(request, pk) :
    deletable = MainModel.objects.get(id=pk)
    return render(request, "delete_one.html", context={"del":deletable})
def delete_view(request, pk) :
    deletable = MainModel.objects.get(id=pk)
    deletable.delete()
    return redirect("/")
def index_json_view(request):
    todos = MainModel.objects.all().values()
    return JsonResponse({"todos": list(todos)}, safe=False)
def json_frontend_view(request) :
    return render(request, "json_simple.html")
