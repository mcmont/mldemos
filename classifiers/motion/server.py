""" Motion classification using the k-nearest neighbour algorithm. """

import http.server
import socketserver
import sys
import tkinter
import motionclassifier

motion_class = None


class MotionServer(http.server.BaseHTTPRequestHandler):
    """ Handle HTTP requests. """
    classifier = motionclassifier.MotionClassifier()

    def do_GET(self):
        """ Respond to a GET request by serving the accel.html file. """
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
        global motion_class
        motion_class = self.classifier.classify(post_data)


def main(port=8000):
    """ Main control loop. CTRL+C stops the loop. """

    # Start the HTTP server, using the MotionServer class as the handler
    httpd = socketserver.TCPServer(('', port), MotionServer)
    print('Waiting for HTTP connections on port '+str(port)+'...')

    # Configure the window
    window = tkinter.Tk()
    window.title("Motion classifier")
    window.attributes("-topmost", True)

    # Create the dark grey background canvas
    canvas = tkinter.Canvas(
        window,
        background="#333F48",
        width=600,
        height=600
    )
    canvas.pack(side="top", fill="both", expand=True)

    # Render the message text
    label_text = tkinter.StringVar()
    message = canvas.create_text(
        300, 300,
        font='Avenir 52 bold',
        fill="#e35205",
        text=label_text.get()
    )

    try:
        while True:
            # Block until we receive HTTP POST data from the device
            httpd.handle_request()
            # Update the message text
            canvas.itemconfigure(message, text=motion_class)
            window.update()

    except KeyboardInterrupt:
        print('\nCaught CTRL+C, exiting.')

    finally:
        httpd.server_close()
        print('HTTP server stopped.')
        window.destroy()


if __name__ == "__main__":
    if len(sys.argv) == 2:
        main(port=int(sys.argv[1]))
    else:
        main()
