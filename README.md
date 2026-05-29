# SzyfrMachina

A pygame-based application that allows you to encipher and decipher most of Polish scout codes. This interactive tool provides a user-friendly graphical interface for working with various cipher techniques used in Polish scouting traditions.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Configuration](#configuration)
- [Architecture](#architecture)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Interactive GUI** - Built with Pygame for a smooth user experience
- **Multiple Polish Scout Codes** - Support for various cipher techniques used in Polish scouting
- **Encipher & Decipher** - Convert text using different encoding methods
- **Frame-Based Interface** - Multiple interactive frames for different cipher types
- **Visual Feedback** - Hover effects and interactive elements for better usability

## Requirements

- Python 3.6+
- pygame

## Installation

### Prerequisites
Make sure you have Python 3.6 or higher installed on your system.

### Steps

1. Clone the repository:
```bash
git clone https://github.com/MinJantek/SzyfrMachina.git
cd SzyfrMachina
```

2. Install required dependencies:
```bash
pip install pygame
```

3. Ensure the `assets` folder is in the same directory as the Python files (it should contain all necessary images)

## Usage

### Running the Application

To start the SzyfrMachina application, run:

```bash
python project.py
```

### How to Use

1. **Launch the Application** - Run `project.py` to open the main window
2. **Select a Cipher** - Click on one of the available cipher frames at the top of the window (frame1-frame6)
3. **Choose Operation** - Select whether you want to encipher or decipher (frame7-frame8)
4. **Enter Text** - Input the text you want to encode or decode
5. **Exit** - Press `ESC` to close the application and view the results in console

### Keyboard Controls

- **ESC** - Exit the application and print results to console

### Mouse Controls

- **Click on Frame Buttons** - Select cipher type or operation
- **Hover** - Frames highlight with a darker shade when you hover over them

## Project Structure

```
SzyfrMachina/
├── project.py          # Main application file - entry point
├── frame.py            # Frame class for UI components
├── setup.py            # Configuration and constants
├── assets/             # Folder containing all image assets
│   └── *.png           # Button and background images
├── README.md           # This file
├── GETTING_STARTED.md  # Getting started guide
├── ARCHITECTURE.md     # Architecture documentation
├── API.md              # API reference
└── .gitignore          # Git ignore rules
```

### File Descriptions

#### `project.py` (Main Application)
The main entry point of the application. Handles:
- Pygame initialization and event loop
- Window and background setup
- Frame creation and positioning
- Event handling (mouse clicks, keyboard input)
- Screen rendering and display updates

#### `frame.py` (UI Component)
Defines the `Frame` class that extends `pygame.sprite.Sprite`:
- Manages individual clickable UI elements
- Handles image loading and positioning
- Implements hover effects (darkening on mouse-over)
- Tracks whether a frame is selected
- Renders frames with visual feedback

#### `setup.py` (Configuration)
Contains global configuration constants:
- `SCREEN_WIDTH` - Window width (1240 pixels)
- `SCREEN_HEIGHT` - Window height (800 pixels)
- `IMAGE_PATH` - Path to assets folder

## Configuration

All configuration is managed through `setup.py`. You can modify:

```python
SCREEN_WIDTH = 1240      # Change window width
SCREEN_HEIGHT = 800      # Change window height
IMAGE_PATH = "assets"    # Change assets folder location
```

## Architecture

SzyfrMachina uses a frame-based architecture where each UI element is represented as a `Frame` object:

**Frame Types:**
- **Cipher Selection Frames** (frame1-frame6) - Top row for selecting different cipher types
- **Operation Frames** (frame7-frame8) - Bottom area for selecting encipher/decipher operations

**Event Flow:**
```
1. User clicks on screen
2. Check collision with frame rectangles
3. Update selected frame (picked or picked2)
4. Render frames with appropriate styling
5. Display update on screen
6. User can press ESC to exit and view results
```

### Key Components

- **Frame Class** - Encapsulates UI button functionality with collision detection
- **Main Loop** - Handles continuous rendering and event processing
- **Mouse Interaction** - Tracks which frame is selected via `picked` and `picked2` variables
- **Visual Rendering** - Dynamic frame highlighting based on selection and hover state

For detailed architecture information, see [ARCHITECTURE.md](ARCHITECTURE.md).

## Documentation

- **[GETTING_STARTED.md](GETTING_STARTED.md)** - Step-by-step installation and first run guide
- **[ARCHITECTURE.md](ARCHITECTURE.md)** - Detailed system architecture and design patterns
- **[API.md](API.md)** - Complete API reference for all modules and classes

## Future Enhancements

Potential areas for improvement:
- Implement actual cipher logic for encoding/decoding
- Add text input fields for user text entry
- Store and display encoded/decoded results in GUI
- Add more Polish scout cipher types
- Create a settings/preferences menu
- Add undo/redo functionality
- Keyboard shortcuts for cipher selection

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Issues and Bug Reports

If you encounter any issues or have suggestions, please [open an issue](https://github.com/MinJantek/SzyfrMachina/issues) on GitHub.

## License

This project is currently unlicensed. Please see the repository for more information.

---

**Author:** MinJantek  
**Repository:** [SzyfrMachina](https://github.com/MinJantek/SzyfrMachina)  
**Created:** 2026-05-29
