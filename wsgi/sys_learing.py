import sys
import os



envsion = os.environ.items()
for k, v in dict(envsion).items():
    print('{}---{}'.format(k, v))