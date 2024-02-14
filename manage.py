import os
import unittest

from app.main import create_app
from app import blueprint

app = create_app(os.getenv('BOILERPLATE_ENV') or 'dev')
app.register_blueprint(blueprint)
app.app_context().push()



from app.main.model import todo

if __name__ == '__main__':
   app.run()
 
