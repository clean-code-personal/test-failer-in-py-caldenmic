import unittest
from alerter_production import *

class TestAlerter(unittest.TestCase):
    def test_failure_count(self):
        failure_count = alert_in_celcius(303.6, network_alert_stub)
        self.assertTrue(failure_count > 0)
        
    def test_return_status_200(self, temperature = 400.5):
        return_status = network_alert_stub(temperature)
        self.assertEqual(return_status, 200)
    
    def test_return_status_500(self, temperature = 190):
        return_status = network_alert_stub(temperature)
        self.assertEqual(return_status, 500)
