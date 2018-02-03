"""
This class is instantiated and the object is passed to all of the classes
that require access to the motion class name.
"""


class MotionData(object):
    """ This class simply holds the name of the type of motion detected. """
    motion_class = None
