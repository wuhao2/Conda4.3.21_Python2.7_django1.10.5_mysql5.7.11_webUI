# _*_ coding=utf-8 _*_
from django.shortcuts import render
import MySQLdb

def getform(request):
    return render (request, 'message_form.html')

def user_message(request):
    db = MySQLdb.connect(user='zhenya', db='message_usermessage', passwd='zhenya', host='localhost')
    cursor = db.cursor()
    cursor.execute('SELECT * FROM message_usermessage   ORDER BY name')
    names = [row[1] for row in cursor.fetchall()]
    db.close()


#   models.py ,no need write sql code
#    Mapping table structures into classes