from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import SocketServer
import numpy
import matplotlib.pyplot as plt
import sys

movement_data = None

class accel_server(BaseHTTPRequestHandler):

    def do_GET(self):
        """ Respond to a GET request by serving the accel.html file. """
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.protocol_version = 'HTTP/1.1'
        self.end_headers()
        with file('client.html') as f:
            self.wfile.write(f.read())
        print('%s connected' % (self.client_address[0]))

    def do_POST(self):
        """ Receive data from the client device's accelerometer. """
        post_data = self.rfile.read(int(self.headers['Content-Length']))
        new_values = numpy.fromstring(post_data, sep=',')
        # print(new_values)
        global movement_data
        movement_data = numpy.vstack((movement_data, new_values))


def run(server_class=HTTPServer, handler_class=accel_server, port=8000):
    global movement_data
    movement_data = numpy.zeros(3)
    init_plot()
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print('Waiting for connections on port '+str(port)+'...')

    while (1):
        httpd.handle_request()
        print(movement_data)
        if movement_data.shape[0] > 5:
            movement_data = movement_data[-5:, :]

        x_data = movement_data[:, 0]
        x_mean = numpy.mean(x_data)
        x_stddev = numpy.std(x_data)

        y_data = movement_data[:, 1]
        y_mean = numpy.mean(y_data)
        y_stddev = numpy.std(y_data)

        z_data = movement_data[:, 2]
        z_mean = numpy.mean(z_data)
        z_stddev = numpy.std(z_data)

        update_plot()

def init_plot():
    # Set the plot window size
    plt.rcParams["figure.figsize"] = (4, 2)
    plt.show(False)

def update_plot():
    x = range(movement_data.shape[0])
    plt.plot(x, [y for y in movement_data[:, 0]])
    plt.plot(x, [y for y in movement_data[:, 1]])
    plt.plot(x, [y for y in movement_data[:, 2]])
    plt.show(False)

if __name__ == "__main__":
    if len(sys.argv) == 2:
        run(port=int(sys.argv[1]))
    else:
        run()
