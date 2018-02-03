""" Motion classification demo using the k-nearest neighbours algorithm. """
import socketserver
import sys
import tkinter
from motiondemo import motiondata
from motiondemo import motionserver


class MotionClassifier(object):
    """ Motion classification demo. """

    def __init__(self, port=8000):
        """ Main control loop. CTRL+C stops the loop. """
        # Instantiate a MotionData object that will store the motion
        # classification state. This object will be shared with the
        # server process to avoid having to use a global variable.
        motion_data = motiondata.MotionData()
        # Start the HTTP server on an available port
        httpd = self.start_server(port, motion_data)
        # Configure the window
        window, canvas, message = self.create_window()

        while True:
            try:
                # Block until we receive HTTP POST data from the device
                httpd.handle_request()
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

    def create_window(self):
        """ Creates the window that displays the classifier result. """
        window = tkinter.Tk()
        # Hide the OS window controls
        # window.overrideredirect(1)

        # Create the dark grey background
        canvas = tkinter.Canvas(
            window,
            background="#333F48",
            width=600,
            height=600
        )
        canvas.pack(side="top", fill="both", expand=True)

        # Centre the window in the display, and bring the
        # window to the front
        self.centre_window(window)
        window.attributes("-topmost", True)

        # Create the classification label placeholder
        label_text = tkinter.StringVar()
        message = canvas.create_text(
            300, 300,
            font='Avenir 52 bold',
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
                httpd = socketserver.TCPServer(
                    ('', port),
                    lambda *args, **kwargs:
                    motionserver.MotionServer(motion_data, *args, **kwargs)
                )

            except OSError as error:
                if error.args[0] != 48:
                    raise
                print('Sorry, port %d is already in use, trying %d...' % (port, port+1))
                port += 1

            else:
                # Hurray, we've found an available port.
                print('Waiting for mobile device connection on port %d...' % (port))
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
    if len(sys.argv) == 2:
        MotionClassifier(port=int(sys.argv[1]))
    else:
        MotionClassifier()
