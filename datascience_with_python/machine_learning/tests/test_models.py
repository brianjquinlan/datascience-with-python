from django.test import TestCase

from ..models import Library, Command, DataFrames

class TestLibrary(TestCase):
    def setUp(self):
        self.library = Library.objects.create(library='pandas', 
                description='description')

    def test_str(self):
        library = Library.objects.get(library='pandas')
        self.assertEqual(str(library), self.library.library)

class TestCommand(TestCase):
    def setUp(self):
        self.library = Library.objects.create(library='pandas', description='description')
        self.command = Command.objects.create(library=self.library, section='DF', title='title',
	    description='description', method='method')

    def test_str(self):
        command = Command.objects.get(title='title')
        self.assertEqual(str(command), self.command.title)

class TestLibrary(TestCase):
    def setUp(self):
        self.dataframe = DataFrames.objects.create(name='test', data={'data':3})

    def test_str(self):
        dataframe = DataFrames.objects.get(name='test')
        self.assertEqual(str(dataframe), self.dataframe.name)

