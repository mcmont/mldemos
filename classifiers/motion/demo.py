""" Motion classification demo using the k-nearest neighbours algorithm. """
import argparse
from http.server import HTTPServer
import ssl
import sys

import tkinter

from motiondemo import motiondata
from motiondemo import motionserver


class MotionClassifier(object):
    """Motion classification demo."""
    _window_size_px = 1000

    def __init__(self):
        """Main control loop. CTRL+C stops the loop."""
        self.args = self._parse_args()

        # Instantiate a MotionData object that will store the motion
        # classification state. This object will be shared with the
        # server process to avoid having to use a global variable.
        motion_data = motiondata.MotionData()
        # Start the HTTP server on an available port
        httpd = self.start_server(self.args.port, motion_data)
        if not self.args.train:
            # Configure the window
            window, canvas, message = self.create_window()

        while True:
            try:
                # Block until we receive HTTP POST data from the device
                httpd.handle_request()

                if not self.args.train:
                    # Update the message text
                    canvas.itemconfigure(message, text=motion_data.motion_class)
                    window.update()

            except (Exception, KeyboardInterrupt):
                print('\nCaught CTRL+C or the window was closed. Exiting.')
                httpd.server_close()
                print('HTTP server stopped.')
                try:
                    window.destroy()
                except Exception:
                    pass
                break

    @staticmethod
    def _parse_args(args=sys.argv[1:]) -> argparse.Namespace:
        parser = argparse.ArgumentParser()
        parser.add_argument("--port", help="Port number", type=int, required=True)
        parser.add_argument("--train", help="Run in training mode", action='store_true')
        return parser.parse_args(args)

    def create_window(self):
        """Creates the window that displays the classifier result. """
        window = tkinter.Tk()

        # Create the dark grey background
        canvas = tkinter.Canvas(
            window,
            background="#333F48",
            width=self._window_size_px,
            height=self._window_size_px
        )
        canvas.pack(side="top", fill="both", expand=True)

        # Centre the window in the display, and bring the
        # window to the front
        self.centre_window(window)
        window.title("Motion classifier")
        window.attributes("-topmost", True)

        # Create the classification label placeholder
        label_text = tkinter.StringVar()
        message = canvas.create_text(
            int(self._window_size_px/2), int(self._window_size_px/2),
            font='Avenir 72 bold',
            fill="#E35205",
            text=label_text.get()
        )
        return window, canvas, message

    def start_server(self, port, motion_data):
        """ Find an available port and start the HTTP server. """
        while True:
            try:
                # Try to start the HTTP server on the chosen port,
                # using the MotionServer class as the handler
                httpd = HTTPServer(('', port),
                                   lambda *args, **kwargs: motionserver.MotionServer(motion_data, self.args.train, *args, **kwargs))
                httpd.socket = ssl.wrap_socket(httpd.socket,
                                               keyfile="./key.pem",
                                               certfile='./cert.pem', server_side=True)

            except OSError as error:
                if error.args[0] != 48:
                    raise
                print(f'Sorry, port {port} is already in use, trying {port+1}...')
                port += 1

            else:
                # Hurray, we've found an available port.
                print(f'Waiting for mobile device connection on port {port}...')
                return httpd

    def centre_window(self, window):
        """ Centre the window on the display. """
        window.update_idletasks()
        w = window.winfo_screenwidth()
        h = window.winfo_screenheight()
        size = tuple(int(_) for _ in window.geometry().split('+')[0].split('x'))
        x = w/2 - size[0]/2
        y = h/2 - size[1]/2
        window.geometry("%dx%d+%d+%d" % (size + (x, y)))


if __name__ == "__main__":
    MotionClassifier()
