import unittest
from flask import Flask
from flask_testing import TestCase


class AppTests(TestCase):

    def create_app(self):
        app = Flask(__name__)
        app.config['TESTING'] = True
        return app

    def test_get_image_energy(self):
        response = self.client.get("/walabot/api/v1.0/imageenergy")
        print(self.client)
        print(response)
        self.assertEqual(response.code, 200)
        self.assertTrue('imageenergy' in response.json)
        self.assertTrue(isinstance(response.json['energy'], float))


if __name__ == '__main__':
    unittest.main()
