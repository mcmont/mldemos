import http.server
import motionclassifier
import numpy
import socketserver
import sys
import threading

movement_data = None

class MotionServer(http.server.BaseHTTPRequestHandler):
    classifier = motionclassifier.MotionClassifier()
    
    """ Handle HTTP requests. """
    def do_GET(self):
        """ Respond to a GET request by serving the accel.html file. """
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.protocol_version = 'HTTP/1.1'
        self.end_headers()
        with open('client.html') as f:
            self.wfile.write(f.read().encode())
        print('%s connected' % (self.client_address[0]))
        return

    def do_POST(self):
        """ Receive POST data from the client device. """
        post_data = self.rfile.read(int(self.headers['Content-Length']))
        movement_data = numpy.fromstring(post_data, sep=',')
        print(movement_data)
        self.classifier.classify(movement_data)


def main(port=8000):
    """
    Main control loop. CTRL+C stops the loop.
    """
    server_address = ('', port)
    print('Waiting for connections on port '+str(port)+'...')

    httpd = socketserver.TCPServer(server_address, MotionServer)
    try:
        carry_on = True
        while (carry_on):
            httpd.handle_request()

    except KeyboardInterrupt:
        carry_on = False
        print('Caught CTRL+C, exiting.')

    finally:
        httpd.server_close()


if __name__ == "__main__":
    if len(sys.argv) == 2:
        main(port=int(sys.argv[1]))
    else:
        main()
