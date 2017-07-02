# _*_ coding=utf-8 _*_
from django.shortcuts import render
from .models import UserMessage  #. means the same directory

# Create your views here.
def getform(request):
    message = None
    """
    get data from database
    """
    all_messages = UserMessage.objects.all() #return all data set(query set type) from database
    # all_messages = UserMessage.objects.filter(name="吴浩") #return [],because without data which satisfied condition in database
    # all_messages.delete()
    # for message in all_messages:
    #     print message.name
    if all_messages:
        message = all_messages[0]


#Post method get data from web page
    if request.method == 'POST':
        name = request.POST.get('name', '')   #Corresponding <input  name="name">
        message = request.POST.get('message', '')  #Corresponding <input  name="message">
        email = request.POST.get('email', '')   #Corresponding <input  name="email">
        address = request.POST.get('address', '')  #Corresponding <input  name="address">

        #save input data of message_form.html
        user_message = UserMessage()
        user_message.name = name
        user_message.message = message
        user_message.email = email
        user_message.address = address
        # user_message.object_id = 'hao'
        user_message.save()

    return render(request, 'message_form.html',   #viod with django interal form.html duplication
                  {"my_message_from_database": message})  #Pass the data to the html page
