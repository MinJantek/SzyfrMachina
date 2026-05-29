# SzyfrMachina Architecture

## Overview

SzyfrMachina is a Pygame-based GUI application designed to handle Polish scout cipher operations. The architecture follows a component-based design pattern with separation of concerns between UI rendering, event handling, and configuration.

## System Architecture

```
┌─────────────────────────────────────────────┐
│        Main Application (project.py)        │
│  - Event Loop                               │
│  - Window Management                        │
│  - Frame Orchestration                      │
└──────────────┬──────────────────────────────┘
               │
    ┌──────────┼──────────┐
    │          │          │
    ▼          ▼          ▼
┌────────┐  ┌────────┐  ┌──────────┐
│ Frame  │  │ Setup  │  │  Assets  │
│ Class  │  │ Config │  │ (Images) │
└────────┘  └────────┘  └──────────┘
```

## Component Details

### 1. Main Application (`project.py`)

**Responsibilities:**
- Initialize Pygame and create display window
- Load and display background image
- Manage frame instances (8 total)
- Handle user events (keyboard, mouse)
- Update screen display
- Track application state

**Key Variables:**
```python
screen                # Pygame display surface
background           # Background image
picked               # Currently selected cipher frame (frame1-6)
picked2              # Currently selected operation (frame7-8)
active               # Application running state
frame1-frame8        # Individual Frame objects
```

**Main Loop Logic:**
```
While active:
  1. Display background
  2. Process events
     - ESC key: exit
     - Mouse click: check frame collision and update selection
  3. Render all frames
  4. Update display
```

### 2. Frame Class (`frame.py`)

**Purpose:** Represents interactive UI elements (buttons/frames)

**Class Structure:**
```python
class Frame(pygame.sprite.Sprite):
    __init__(coordinates, file)      # Constructor
    render(picked, picked2, name)    # Rendering logic
```

**Attributes:**
- `file` - Image filename
- `image` - Pygame surface object
- `rect` - Rectangle for positioning and collision detection
- `mask` - Boolean flag for hover state

**Methods:**

#### `__init__(coordinates, file)`
- Loads image from `IMAGE_PATH/{file}`
- Creates rectangle at specified coordinates (top-left)
- Initializes sprite

#### `render(picked, picked2, name)`
- **Input:** 
  - `picked` - Name of selected cipher frame
  - `picked2` - Name of selected operation frame
  - `name` - This frame's identifier
- **Output:** String command to blit frame
- **Logic:**
  1. Check if mouse is over frame
  2. If hovering AND not selected: darken image
  3. Return blit command string
  4. If selected: display normally
  5. If not hovering and not selected: don't render

**Rendering States:**
- **Selected** - Display at full brightness
- **Hovering (not selected)** - Display darkened (blend_add with gray)
- **Inactive** - Not rendered (returns None implicitly)

### 3. Configuration (`setup.py`)

**Global Constants:**
```python
SCREEN_WIDTH = 1240       # Window width
SCREEN_HEIGHT = 800       # Window height
IMAGE_PATH = "assets"     # Asset directory path
```

## Data Flow

### Initialization Flow
```
project.py runs
    ↓
setup.py imported (constants loaded)
    ↓
Frame class imported from frame.py
    ↓
8 Frame objects created with coordinates and images
    ↓
Main event loop starts
```

### Event Handling Flow
```
Event occurs (mouse click/key press)
    ↓
Is it ESC key?
    ├─ Yes → Print results, set active = False, exit
    └─ No → Continue
    ↓
Is it mouse click?
    ├─ Yes → Check collision with frames 1-6
    │         If collision: update 'picked'
    │         Check collision with frames 7-8
    │         If collision: update 'picked2'
    └─ No → Continue
    ↓
Render all frames (call frame.render() for each)
    ↓
Update display
    ↓
Loop
```

### Frame Rendering Flow
```
For each of 8 frames:
    ↓
Call frame.render(picked, picked2, f"frame{i}")
    ↓
Check mouse collision
    ├─ Hovering?
    │  ├─ Yes → Is it selected? 
    │  │        ├─ Yes → Return blit normal
    │  │        └─ No → Darken and return blit
    │  └─ No → If selected, return blit normal
    └─ Return command string
    ↓
Execute returned command (blit to screen)
    ↓
Next frame
```

## Frame Layout

### Visual Layout
```
┌────────────────────────────────────────────────────────────────────┐
│  Frame1    Frame2    Frame3    Frame4    Frame5    Frame6          │
│  (20,20)  (220,20)  (420,20)  (620,20)  (820,20) (1020,20)        │
│  200x60   200x60    200x60    200x60    200x60   200x60           │
│                                                                    │
│                      Frame7 (230,106)                              │
│                      1000x300                                      │
│                                                                    │
│                      Frame8 (230,406)                              │
│                      1000x300                                      │
│                                                                    │
└────────────────────────────────────────────────────────────────────┘
```

**Frame Dimensions:**
- Cipher Selection (1-6): 200x60 pixels
- Operation Frames (7-8): 1000x300 pixels

## Technical Implementation Details

### Image Rendering Technique
The application uses a dynamic `eval()` approach for rendering:

```python
# For each frame, render returns a command string:
a = eval(f"frame{i}.render('{picked}','{picked2}','frame{i}')")
eval(f"{a}")

# Example: if render returns "screen.blit(frame1.image,frame1.rect)"
# Then eval executes: screen.blit(frame1.image,frame1.rect)
```

**Note:** While functional, using `eval()` is considered a code smell and could be refactored for better performance and security.

### Hover Effect Implementation
```python
# Blend add with gray (130, 130, 130)
self.image.fill((130,130,130), special_flags=pygame.BLEND_ADD)
```
This creates a darkening effect by adding gray values to the image.

## State Management

### Application State
- **active** - Boolean tracking if app is running
- **picked** - String: currently selected cipher (default "frame2")
- **picked2** - String: currently selected operation (default "frame7")

### State Transitions
```
Initial State:
  picked = "frame2"
  picked2 = "frame7"
  active = True

On Mouse Click → Update picked or picked2
On ESC Key    → active = False, exit loop
```

## Performance Considerations

1. **Image Loading** - Images loaded on every render cycle (optimization opportunity)
2. **Eval Usage** - Dynamic code execution has performance overhead
3. **Event Loop** - Runs at unlimited FPS (no frame rate cap)

## Future Improvements

### Code Quality
- Replace `eval()` with direct method calls
- Implement frame-rate limiting
- Add error handling for missing images
- Use object-oriented state management

### Functionality
- Add actual cipher encoding/decoding
- Implement text input fields
- Add configuration UI
- Create cipher algorithms module

### Performance
- Cache loaded images
- Use sprite groups for batch rendering
- Implement dirty rect optimization
