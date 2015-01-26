import os
import sys

# add module to syspath
pwd = os.path.abspath((os.path.dirname(__file__)))
project = os.path.basename(pwd)
new_path = pwd.strip(project)
full_path = os.path.join(new_path, 'project')
print pwd
print project
print new_path
print full_path

try:
    from project import app
except ImportError:
    sys.path.append(full_path)
    from project import app

def before_feature(context, feature):
    context.client = app.test_client()
