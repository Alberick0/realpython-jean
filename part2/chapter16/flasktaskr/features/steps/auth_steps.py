from behave import *

@given(u'flaskr is set up')
def task_is_setup(context):
    assert context.client