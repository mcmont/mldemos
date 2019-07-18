"""HTTP request handler for the motion classifier demo."""

import http.server
import logging

from . import motionclassifier

logging.basicConfig(level=logging.INFO, format="%(message)s")
log = logging.getLogger("classifier")


class MotionServer(http.server.BaseHTTPRequestHandler):
    """HTTP request handler."""
    classifier = None
    motion_data = None

    def __init__(self, motion_data, training_mode, *args, **kwargs):
        """
        This pattern allows us to pass an initialised MotionData object
        as an argument. This avoids the need for a global variable to hold
        the motion classification state.
        """
        self.motion_data = motion_data
        self.training_mode = training_mode
        if not self.training_mode:
            self.classifier = motionclassifier.MotionClassifier()
        super(MotionServer, self).__init__(*args, **kwargs)

    def do_GET(self):
        """Respond to a GET request by serving the client.html file."""
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.protocol_version = 'HTTP/1.1'
        self.end_headers()
        with open('client.html') as f:
            self.wfile.write(f.read().encode())
        log.info('%s connected' % (self.client_address[0]))

    def do_POST(self):
        """Receive POST data from the device and classify the motion."""
        post_data = self.rfile.read(int(self.headers['Content-Length']))
        logging.debug(f"{post_data}")
        (x_mean, x_std, y_mean, y_std, z_mean, z_std) = post_data.decode("ascii").split(",")
        if self.training_mode:
            log.info(
                "{:>.7}, {:>.7}, {:>.7}, {:>.7}, {:>.7}, {:>.7}"\
                .format(x_mean, x_std, y_mean, y_std, z_mean, z_std))
            return
        self.motion_data.motion_class = self.classifier.classify(post_data)
        log.info("xMean: {:>.7}, xStd: {:>.7}, yMean: {:>.7}, yStd: {:>.7}, zMean: {:>.7}, zStd: {:>.7}, class: {}"\
                      .format(x_mean, x_std, y_mean, y_std, z_mean, z_std, self.motion_data.motion_class))
