""" HTTP request handler for the motion classifier demo. """
import http.server
from . import motionclassifier


class MotionServer(http.server.BaseHTTPRequestHandler):
    """ HTTP request handler. """
    classifier = motionclassifier.MotionClassifier()
    motion_data = None

    def __init__(self, motion_data, *args, **kwargs):
        """
        This pattern allows us to pass an initialised MotionData object
        as an argument. This avoids the need for a global variable to hold
        the motion classification state.
        """
        self.motion_data = motion_data
        super(MotionServer, self).__init__(*args, **kwargs)

    def do_GET(self):
        """ Respond to a GET request by serving the client.html file. """
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.protocol_version = 'HTTP/1.1'
        self.end_headers()
        with open('client.html') as f:
            self.wfile.write(f.read().encode())
        print('%s connected' % (self.client_address[0]))

    def do_POST(self):
        """ Receive POST data from the device and classify the motion. """
        post_data = self.rfile.read(int(self.headers['Content-Length']))
        self.motion_data.motion_class = self.classifier.classify(post_data)
