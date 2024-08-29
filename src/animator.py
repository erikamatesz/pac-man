from constants import *

class Animator(object):
    """
    A class to handle animation by managing frames and controlling their playback.

    Attributes:
        frames (list): A list of frames to be displayed in the animation.
        current_frame (int): The index of the current frame being displayed.
        speed (int): The speed of the animation in frames per second.
        loop (bool): A flag indicating whether the animation should loop when finished.
        dt (float): The accumulated time to manage frame updates.
        finished (bool): A flag indicating whether the animation has finished.
    """

    def __init__(self, frames=[], speed=20, loop=True):
        """
        Initializes a new instance of the Animator class.

        Args:
            frames (list, optional): A list of frames to be used in the animation. Defaults to an empty list.
            speed (int, optional): The speed of the animation in frames per second. Defaults to 20.
            loop (bool, optional): A flag indicating whether the animation should loop when finished. Defaults to True.
        """
        self.frames = frames
        self.current_frame = 0
        self.speed = speed
        self.loop = loop
        self.dt = 0
        self.finished = False

    def reset(self):
        """
        Resets the animation to the beginning.

        Sets the current frame to 0 and marks the animation as not finished.
        """
        self.current_frame = 0
        self.finished = False

    def update(self, dt):
        """
        Updates the animation based on the elapsed time.

        Advances to the next frame if the accumulated time exceeds the frame duration.
        If the end of the frames list is reached, loops back to the start if looping is enabled,
        or marks the animation as finished if looping is not enabled.

        Args:
            dt (float): The time elapsed since the last update.

        Returns:
            The current frame to be displayed.
        """
        if not self.finished:
            self.nextFrame(dt)
        if self.current_frame == len(self.frames):
            if self.loop:
                self.current_frame = 0
            else:
                self.finished = True
                self.current_frame -= 1

        return self.frames[self.current_frame]

    def nextFrame(self, dt):
        """
        Advances to the next frame based on the elapsed time.

        Accumulates the elapsed time and updates the current frame if the time threshold is met.

        Args:
            dt (float): The time elapsed since the last update.
        """
        self.dt += dt
        if self.dt >= (1.0 / self.speed):
            self.current_frame += 1
            self.dt = 0
