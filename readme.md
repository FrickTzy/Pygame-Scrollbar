# Pygame-Scrollbar

## Overview

The Pygame-Scrollbar package provides classes and utilities to implement scrollable interfaces in Pygame applications. It includes components such as scroll bars, content bars, and event handlers to enable smooth scrolling functionality.

## Classes

- **ScrollBarManager:** Manages the creation and rendering of scroll bars.
- **ContentBar:** Represents individual content bars within a scrollable interface.

## Installation

You can install the package via pip:

```bash
pip install pygame-scrollbar
```

## Usage

Here's a basic example demonstrating how to use the Scrollable Interface Package:

```python
import pygame
from scrollable_interface import ScrollBarManager, ContentBar

# Create content bars
content_bar1 = ContentBar(size=(100, 50))
content_bar2 = ContentBar(size=(100, 50))
content_bar3 = ContentBar(size=(100, 50))
content_bar_list = [content_bar1, content_bar2, content_bar3]

# Create a scroll bar manager
scroll_bar_manager = ScrollBarManager(size=(20, 200), content_bar_list=content_bar_list, position=(0, 0))

# In your main loop:
while running:
    # Update the window
    window.fill((255, 255, 255))
    scroll_bar_manager.show(surface=window, window_height=window_height)
    pygame.display.update()
```

## Documentation

For detailed documentation, please refer to the [github repository](API_REFERENCE.md).

## License

This package is licensed under the MIT License.

## Contribution

Contributions are welcome! Please feel free to submit issues, feature requests, or pull requests.

---