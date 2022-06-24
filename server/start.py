import os
import sys
_this_folder = os.path.abspath(os.path.dirname(__file__))
sys.path.append(os.path.join(_this_folder, ".."))

from settings.config import HOST, PORT, DEBUG
from server.apps import create_app

app = create_app()


if __name__ == '__main__':
    app.run(host=HOST, port=PORT, debug=DEBUG)