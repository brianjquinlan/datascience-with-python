from django.test import TestCase, RequestFactory
from django.core.urlresolvers import reverse

from ..views import *
from ..models import Library, Command, DataFrame

class TestSetUp(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.library = Library.objects.create(library='pandas', description='description')

class TestMainPage(TestSetUp):
    def setUp(self):
        super().setUp()
        self.library2 = Library.objects.create(library='numpy', description='description2')

    def test_get(self):
        request = self.factory.get(reverse('machine_learning:main_page'))
        response = main_page(request)

        libraries = Library.objects.all()

        self.assertEqual(response.status_code, 200)
        # self.assertQuerysetEqual(response.context_data['libraries'],
        #    map(repr, libraries))

class TestInteractive(TestSetUp):
    def setUp(self):
        super().setUp()

        self.dataframe = DataFrame.objects.create(name='Test', data={'test':3})
        self.command = Command.objects.create(library=self.library, section='df', title='test',
            description='description', method='method')

    def test_get(self):
        request = self.factory.get(reverse('machine_learning:interactive',
            kwargs={'library':'pandas'}))
        response = interactive(request, library='pandas')

        commands = Command.objects.filter(library=self.library)

        self.assertEqual(response.status_code, 200)
        # self.assertQuerysetEqual(response.context_data['command_list'], map(repr, commands))
        # self.assertQuerysetEqual(response.context_data['data'], self.dataframe)

    def test_404(self):
        request = self.factory.get(reverse('machine_learning:interactive',
            kwargs={'library':'test'}))
        
        with self.assertRaises(Http404):
            interactive(request, library='test')

class TestAlgorithms(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
    
        self.algorithm = Algorithm.objects.create(name='Gradient Descent', description='Test example',
                slug='gradient-descent')
        
    def test_get(self):
        request = self.factory.get(reverse('machine_learning:algorithms',
            kwargs={'algorithm':'gradient-descent'}))
        response = algorithms(request, algorithm='gradient-descent')

        self.assertEqual(response.status_code, 200)

    def test_404(self):
        request = self.factory.get(reverse('machine_learning:algorithms',
            kwargs={'algorithm':'not-existing'}))

        with self.assertRaises(Http404):
            algorithms(request, algorithm='not-existing')

        # response = self.client.get(reverse('machine_learning:algorithms',
        #     kwargs={'algorithm':'not-existing'}))

        # self.assertEqual(response.status_code, 404)

class TestLibraries(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

        self.pylibrary = PythonLibrary.objects.create(name='Numpy', description='Test example',
                slug='numpy')

    def test_get(self):
        request = self.factory.get(reverse('machine_learning:libraries',
            kwargs={'pylibrary':'numpy'}))
        response = libraries(request, pylibrary='numpy')

        self.assertEqual(response.status_code, 200)

    def test_404(self):
        request = self.factory.get(reverse('machine_learning:libraries',
            kwargs={'pylibrary':'test'}))
        
        with self.assertRaises(Http404):
            libraries(request, pylibrary='test')
