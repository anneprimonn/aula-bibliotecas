from flask import Flash
from views import *

app = Flash(__name__)

if __name__ == '__main__':
    app