from django.shortcuts import render
from django.utils import timezone
from .models import Task, Instance
from django.http import JsonResponse
import json
from django.http import HttpResponse
from rest_framework import routers, serializers, viewsets
import ctypes as ct
import subprocess as sp
from rest_framework import generics
from .serializers import *
import time
import os

# Create your views here.

def task_run(request):
    return render(request, 'task_run.html',  {})

def start(self):
    test("test")
    return JsonResponse({'status':'OK'})

def get_data(self):
    tasks = Task.objects.order_by('created_date')
    return JsonResponse(serializers.serialize('json', tasks), safe=False)

def check_tasks(self):
    tasks = Task.objects.all()
    for task in tasks:
    	if(task.status != "100"):
            time_proc = 0;
            print("Rozpoczynam problem o nazwie: " + task.title)
            ins = Instance.objects.get(id=task.instance_id)
            file=open("cities.tsp",'w')
            outfile = open("stat.txt","w")
            file.write(ins.graph)
            file.close()
            procs = task.proc
            if(procs == 1):
                procs = 2
            timer = ins.cityCount/5
            if (timer < 10):
                timer = 10;
            print("Parametry startowe")
            print("Czas: " + str(timer))
            print("Liczba procesow: "+ str(procs))
            time.sleep(5)
            start = time.time()
            exe = sp.Popen(["mpirun -np " + str(procs) + " --hosts master3,slave4 ./TSP " + str(timer) + " " + str(task.population) + " " + str(task.generations) + " " + str(task.wpz)],stdout=outfile,shell=True)
            running = 1
            while(running):
                end = time.time()
                stat = ((end - start)*100)/(ins.cityCount/5);
                print("status: " + str(stat) + "%, czas: " + str(end-start) +  "s, Calkowity czas: " + str(timer))
                task.status = stat
                task.save()
                if(exe.poll() == 0):
                    running = 0
                    print("Koniec tego!")
                time_proc = time_proc + 1
                time.sleep(1)
                if(stat > 160):
                    exe.terminate()
                    exe.kill()
                    running = 0
                    print("Task killed!")
            task.status = 100;
            task.save()
            outfile.close()
            file=open("stat.txt",'r')
            lineList = file.readlines()
            wyniczek = lineList[-1]
            file.close()
            his = History(owner_id = 1, title = task.title, cityCount = ins.cityCount, graph = wyniczek, time = str(timer), population = task.population, generations = task.generations, wpz = task.wpz, proc = task.proc)
            his.save()
    return JsonResponse({'status':wyniczek})



class CreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()

class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class UserTaskList(generics.ListAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """
        username = self.kwargs['owner_id']
        return Task.objects.filter(owner_id=username)





class CreateView_Instance(generics.ListCreateAPIView):
    queryset = Instance.objects.all()
    serializer_class = InstanceSerializer

    def perform_create(self, serializer):
        serializer.save()

class DetailsView_Instance(generics.RetrieveUpdateDestroyAPIView):
    queryset = Instance.objects.all()
    serializer_class = InstanceSerializer

class UserTaskList_Instance(generics.ListAPIView):
    serializer_class = InstanceSerializer

    def get_queryset(self):
        username = self.kwargs['owner_id']
        return Instance.objects.filter(owner_id=username)




class CreateView_History(generics.ListCreateAPIView):
    queryset = History.objects.all()
    serializer_class = HistorySerializer

    def perform_create(self, serializer):
        serializer.save()

class DetailsView_History(generics.RetrieveUpdateDestroyAPIView):
    queryset = History.objects.all()
    serializer_class = HistorySerializer

class UserTaskList_History(generics.ListAPIView):
    serializer_class = HistorySerializer

    def get_queryset(self):
        username = self.kwargs['owner_id']
        return History.objects.filter(owner_id=username)
