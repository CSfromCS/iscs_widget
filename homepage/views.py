from audioop import reverse
from tkinter import Widget
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from .models import WidgetUser
import pyrebase

config = {
  "apiKey": "AIzaSyAo0LQihQVoi3IUmsmznctCmnJcDJoHv0s",
  "authDomain": "widget-container.firebaseapp.com",
  "databaseURL": "https://widget-container-default-rtdb.asia-southeast1.firebasedatabase.app/",
  "projectId": "widget-container",
  "storageBucket": "widget-container.appspot.com",
  "messagingSenderId": "404457620543",
  "appId": "1:404457620543:web:428046a4db2e5671f9648a",
  "measurementId": "G-L62V3LDS7M"
};

firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
database = firebase.database()

class HomepageView(View):
    def get(self, request):

        users = database.child('data').child('users').get().val()
        
        for key, value in users.items():
            new_user = WidgetUser(key, value["first_name"], value["middle_name"], value["last_name"], value["id_num"], value["email"])
            new_user.save()
        objects_set = {
            "users": [obj for obj in WidgetUser.objects.all().order_by('last_name')]
        }

        return render(request, 'homepage/index.html', objects_set)


class WidgetUserDetailView(DetailView):
    model = WidgetUser


class WidgetUserCreateView(CreateView):
    model = WidgetUser

    fields = ["first_name", "middle_name", "last_name",
              "id_num", "email"]

    def get_success_url(self):
        new_user = WidgetUser.objects.all().filter(id=self.object.id)[0]
        object_to_send = {"first_name": new_user.first_name, "middle_name": new_user.middle_name, "last_name": new_user.last_name, "id_num": new_user.id_num, "email": new_user.email}
        database.child("data").child("users").child(self.object.id).set(object_to_send)

        return "/homepage/"
