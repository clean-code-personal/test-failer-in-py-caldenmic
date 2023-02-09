from alerter_functions import *
from alerter_test_functions import *

failure_count = alert_in_celcius(400.5)
failure_count = alert_in_celcius(303.6)
alert_failure_count_test(failure_count)
print(f'{alert_failure_count} alerts failed.')
print('All is well (maybe!)')
