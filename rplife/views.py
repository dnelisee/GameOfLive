import platform
from time import sleep
from rplife.grid import LifeGrid

"""
__all__ : define the list of names that the module views will export.
"""
__all__ = ["UnifiedView"]

# check the OS 
IS_WINDOWS = platform.system() == "Windows"

if IS_WINDOWS:
    from blessed import Terminal
else:
    import curses


class UnifiedView:
    def __init__(self, pattern, gen=10, frame_rate=7, bbox=(0, 0, 20, 20)):
        self.pattern = pattern       # initial generation  
        self.gen = gen               # number of generations
        self.frame_rate = frame_rate # number of frames per second
        self.bbox = bbox             # part of the grid to display
        if IS_WINDOWS:
            self.term = Terminal()

    def show(self):
        if IS_WINDOWS:
            # use blessed
            with self.term.fullscreen(), self.term.hidden_cursor():
                self._draw_blessed()
        else:
            # use curses
            curses.wrapper(self._draw_curses)

    def _draw_blessed(self):
        # Define the grid of the first generation
        current_grid = LifeGrid(self.pattern)

        # Clear the screen
        print(self.term.clear)

        # Try to display the first generation on the screen
        try:
            print(self.term.move(0, 0) + current_grid.as_string(self.bbox))
        except Exception as e:
            raise ValueError(
                f"Error: terminal too small for pattern '{self.pattern.name}'"
            ) from e

        # Display generations
        for _ in range(self.gen):
            current_grid.evolve()
            print(self.term.move(0, 0) + current_grid.as_string(self.bbox))
            sleep(1 / self.frame_rate)

    def _draw_curses(self, screen):
        """
            screen is automatically sended when we do curses.wrapper(self._draw_curses)
        """
        # Define the grid of the first generation
        current_grid = LifeGrid(self.pattern)

        # Make the cursor invisible
        curses.curs_set(0)

        # Clear the screen
        screen.clear()

        # Try to display the first generation on the screen
        try:
            screen.addstr(0, 0, current_grid.as_string(self.bbox))
        except curses.error:
            raise ValueError(
                f"Error: terminal too small for pattern '{self.pattern.name}'"
            )

        # Display generations
        for _ in range(self.gen):
            current_grid.evolve()
            screen.addstr(0, 0, current_grid.as_string(self.bbox))
            screen.refresh()
            sleep(1 / self.frame_rate)

