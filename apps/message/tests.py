from django.test import TestCase
from models import UserMessage

# Create your tests here.
tables = UserMessage()
print "get datatable:"
print "access datatable:", tables.name, tables.email