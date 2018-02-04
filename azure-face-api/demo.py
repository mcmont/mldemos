"""
Microsoft Azure Face API demo.

Loads an image from a URL then queries the Microsoft Azure Face API to find
faces in the image and locate their features.
"""
import io
import json
import os
import requests
import sys
import time
import tkinter
from PIL import ImageTk, Image


class FaceApiDemo(object):
    """ Microsoft Azure Face API demo. """

    def __init__(self, image_url):
        """ Demo entrypoint. """
        self.create_window(image_url)

    def get_face_data(self, image_url):
        """ Queries the Azure Face API using the image URL. """
        endpoint_url = 'https://westeurope.api.cognitive.microsoft.com/face/v1.0/detect?returnFaceLandmarks=true'
        headers = {
            'Content-Type': 'application/json',
            'Ocp-Apim-Subscription-Key': os.environ['AZURE_COGNITIVE_SERVICES_API_KEY']
        }
        payload = {'url': image_url}

        print("Sending request to face API...")
        start = time.time()
        response = requests.post(endpoint_url, headers=headers, json=payload)
        end = time.time()
        print("Response received in %.3fms" % (1000*(end-start)))

        if (200 != response.status_code):
            raise Exception(
                'HTTP %d response received from Face API. \
                Error message: %s\r\nExiting.'
                % (response.status_code, response.text)
            )

        # The JSON response body contains an array of face data objects,
        # one per face that was found in the image.
        face_data = json.loads(response.text)
        print('%d faces detected' % (len(face_data)))
        return face_data

    def create_window(self, image_url):
        """ Creates a window to display the image and the Face API data. """
        window = tkinter.Tk()
        image = self.download_image(image_url)
        width, height = image.size
        tk_image = ImageTk.PhotoImage(image)

        canvas = tkinter.Canvas(
            window,
            width=width-3,
            height=height-3,
        )
        canvas.pack()
        canvas.create_image(0, 0, anchor=tkinter.NW, image=tk_image)

        # Call the keypress_handler() function when the user presses a key.
        window.bind_all(
            '<Key>',
            lambda event, canvas=canvas: self.keypress_handler(
                event,
                canvas,
                image_url
            )
        )

        # Centre the window in the display, and bring the
        # window to the front
        self.centre_window(window)
        window.title(image_url)
        window.attributes("-topmost", True)
        window.mainloop()
        return

    def download_image(self, image_url):
        """ Download an image and return it in PIL format. """
        response = requests.get(image_url, verify=True)
        response.raw.decode_content = True
        image_data = io.BytesIO(response.content)
        return Image.open(image_data)

    def keypress_handler(self, event, canvas, image_url):
        """ Query the Face API and overlay the data. """
        face_data = self.get_face_data(image_url)
        self.draw_face_overlay(canvas, face_data)

    def centre_window(self, window):
        """ Centre the window on the display. """
        window.update_idletasks()
        w = window.winfo_screenwidth()
        h = window.winfo_screenheight()
        size = tuple(int(_) for _ in window.geometry().split('+')[0].split('x'))
        x = w/2 - size[0]/2
        y = h/2 - size[1]/2
        window.geometry("%dx%d+%d+%d" % (size + (x, y)))

    def draw_face_overlay(self, canvas, face_data):
        """ Overlay the Face API features. """
        landmark_width = 3

        for face in face_data:
            # Draw the bounding rectangle in green
            canvas.create_rectangle(
                face['faceRectangle']['left'],
                face['faceRectangle']['top'],
                face['faceRectangle']['left'] + face['faceRectangle']['width'],
                face['faceRectangle']['top'] + face['faceRectangle']['height'],
                outline='#00ff00',
                width=landmark_width
            )

            # Draw the pupils in red
            canvas.create_oval(
                face['faceLandmarks']['pupilLeft']['x'],
                face['faceLandmarks']['pupilLeft']['y'],
                face['faceLandmarks']['pupilLeft']['x'],
                face['faceLandmarks']['pupilLeft']['y'],
                fill='#ff0000',
                outline='#ff0000',
                width=landmark_width
            )
            canvas.create_oval(
                face['faceLandmarks']['pupilRight']['x'],
                face['faceLandmarks']['pupilRight']['y'],
                face['faceLandmarks']['pupilRight']['x'],
                face['faceLandmarks']['pupilRight']['y'],
                fill='#ff0000',
                outline='#ff0000',
                width=landmark_width
            )

            # Draw the eye outlines in red
            canvas.create_line(
                face['faceLandmarks']['eyeLeftOuter']['x'],
                face['faceLandmarks']['eyeLeftOuter']['y'],
                face['faceLandmarks']['eyeLeftTop']['x'],
                face['faceLandmarks']['eyeLeftTop']['y'],
                face['faceLandmarks']['eyeLeftInner']['x'],
                face['faceLandmarks']['eyeLeftInner']['y'],
                face['faceLandmarks']['eyeLeftBottom']['x'],
                face['faceLandmarks']['eyeLeftBottom']['y'],
                face['faceLandmarks']['eyeLeftOuter']['x'],
                face['faceLandmarks']['eyeLeftOuter']['y'],
                fill='#ff0000',
                smooth=True
            )
            canvas.create_line(
                face['faceLandmarks']['eyeRightOuter']['x'],
                face['faceLandmarks']['eyeRightOuter']['y'],
                face['faceLandmarks']['eyeRightTop']['x'],
                face['faceLandmarks']['eyeRightTop']['y'],
                face['faceLandmarks']['eyeRightInner']['x'],
                face['faceLandmarks']['eyeRightInner']['y'],
                face['faceLandmarks']['eyeRightBottom']['x'],
                face['faceLandmarks']['eyeRightBottom']['y'],
                face['faceLandmarks']['eyeRightOuter']['x'],
                face['faceLandmarks']['eyeRightOuter']['y'],
                fill='#ff0000',
                smooth=True
            )

            # Draw the eyebrows in magenta
            canvas.create_line(
                face['faceLandmarks']['eyebrowLeftInner']['x'],
                face['faceLandmarks']['eyebrowLeftInner']['y'],
                face['faceLandmarks']['eyebrowLeftOuter']['x'],
                face['faceLandmarks']['eyebrowLeftOuter']['y'],
                fill='#ff00ff',
                width=landmark_width
            )
            canvas.create_line(
                face['faceLandmarks']['eyebrowRightInner']['x'],
                face['faceLandmarks']['eyebrowRightInner']['y'],
                face['faceLandmarks']['eyebrowRightOuter']['x'],
                face['faceLandmarks']['eyebrowRightOuter']['y'],
                fill='#ff00ff',
                width=landmark_width
            )

            # Draw the mouth outline in magenta
            canvas.create_polygon(
                face['faceLandmarks']['mouthLeft']['x'],
                face['faceLandmarks']['mouthLeft']['y'],
                face['faceLandmarks']['upperLipTop']['x'],
                face['faceLandmarks']['upperLipTop']['y'],
                face['faceLandmarks']['mouthRight']['x'],
                face['faceLandmarks']['mouthRight']['y'],
                face['faceLandmarks']['underLipBottom']['x'],
                face['faceLandmarks']['underLipBottom']['y'],
                face['faceLandmarks']['mouthLeft']['x'],
                face['faceLandmarks']['mouthLeft']['y'],
                width=landmark_width,
                outline='#ff00ff',
                fill='',
                smooth=1
            )

            # Draw the mouth and lip dimensions in white
            canvas.create_line(
                face['faceLandmarks']['mouthLeft']['x'],
                face['faceLandmarks']['mouthLeft']['y'],
                face['faceLandmarks']['mouthRight']['x'],
                face['faceLandmarks']['mouthRight']['y'],
                fill='#ffffff',
                width=landmark_width
            )
            canvas.create_line(
                face['faceLandmarks']['upperLipTop']['x'],
                face['faceLandmarks']['upperLipTop']['y'],
                face['faceLandmarks']['upperLipBottom']['x'],
                face['faceLandmarks']['upperLipBottom']['y'],
                fill='#ffffff',
                width=landmark_width
            )
            canvas.create_line(
                face['faceLandmarks']['underLipTop']['x'],
                face['faceLandmarks']['underLipTop']['y'],
                face['faceLandmarks']['underLipBottom']['x'],
                face['faceLandmarks']['underLipBottom']['y'],
                fill='#ffffff',
                width=landmark_width
            )

            # Draw the nose outline in yellow
            canvas.create_polygon(
                face['faceLandmarks']['noseRootLeft']['x'],
                face['faceLandmarks']['noseRootLeft']['y'],
                face['faceLandmarks']['noseRootRight']['x'],
                face['faceLandmarks']['noseRootRight']['y'],
                face['faceLandmarks']['noseRightAlarTop']['x'],
                face['faceLandmarks']['noseRightAlarTop']['y'],
                face['faceLandmarks']['noseRightAlarOutTip']['x'],
                face['faceLandmarks']['noseRightAlarOutTip']['y'],
                face['faceLandmarks']['noseLeftAlarOutTip']['x'],
                face['faceLandmarks']['noseLeftAlarOutTip']['y'],
                face['faceLandmarks']['noseLeftAlarTop']['x'],
                face['faceLandmarks']['noseLeftAlarTop']['y'],
                face['faceLandmarks']['noseRootLeft']['x'],
                face['faceLandmarks']['noseRootLeft']['y'],
                width=landmark_width,
                outline='#ffff00',
                fill='',
                smooth=1
            )

            # Draw the nose tip in yellow
            canvas.create_oval(
                face['faceLandmarks']['noseTip']['x'],
                face['faceLandmarks']['noseTip']['y'],
                face['faceLandmarks']['noseTip']['x'],
                face['faceLandmarks']['noseTip']['y'],
                fill='#ffff00',
                outline='#ffff00',
                width=landmark_width
            )


if __name__ == "__main__":
    if len(sys.argv) == 2:
        FaceApiDemo(image_url=sys.argv[1])
    else:
        print('Please provide an image URL.')
