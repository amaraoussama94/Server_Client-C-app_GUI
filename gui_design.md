# 🧠 Modular Client-Server Chat App with PyQt5 GUI

This project features a cross-platform client-server architecture written in C, now extended with a modular PyQt5 GUI front-end. The GUI launches the compiled C client as a subprocess and communicates via stdin/stdout, preserving protocol integrity and contributor clarity.

## 📦 Project Structure

├── client_gui/           # PyQt5 GUI front-end 
│ ├── main.py             # GUI entry point (launches C client subprocess) 
│ ├── sidebar.py          # Conversation list panel 
│ ├── chat_panel.py       # Message history + input 
│ ├── file_panel.py       # File drag-and-drop interface 
│ ├── settings_panel.py   # Username, theme, connection status 
│ ├── client_socket.py    # Subprocess I/O wrapper 
│ ├── protocol.py         # Frame parsing (mirrors C logic) 
│ └── assets/icons/       # SVG icons

---

## 🎯 Goals

- Provide a clean, responsive interface for chat and file transfer
- Support multi-client communication with delivery feedback
- Modular layout for future features (e.g., groups, presence, media)

---
## 🧩 GUI Component Breakdown

This section defines the key UI components of the PyQt5 GUI client, inspired by modern messaging platforms like Microsoft Teams.

| Section ID | Name                      | Description                                             |
|------------|------------------------   |---------------------------------------------------------|
| 1          | **ConversationListPanel** | Vertical sidebar listing all previous conversations     |
|            |                           |  (by clien or group).                                   |
|--------------------------------------------------------------------------------------------------|
| 2          | **UserStatusHeader**      | Top bar showing current username, avatar, and           |
|            |                           |connectionstatus.                                        |
|--------------------------------------------------------------------------------------------------|
| 3          | **WindowControlPanel**    | Standard window controls (minimize, maximize, close)    |
|            |                           | — top-right corner.                                     |
|--------------------------------------------------------------------------------------------------|
| 4          | **ChatHistoryPanel**      | Main panel showing message history with selected        |
|            |                           |client.                                                  |
|--------------------------------------------------------------------------------------------------|
| 5          | **MessageInputPanel**     | Bottom input area for typing messages or dragging       | 
|            |                           |files to send.                                           |
|--------------------------------------------------------------------------------------------------|
| 6          | **SendButton**            | Action button to confirm sending message or             |
|            |                           |file.                                                    |
----------------------------------------------------------------------------------------------------

---

### 🧱 Layout Sketch
````text
+----------------------------------------------------------------------------------+ 
|     [UserStatusHeader]                   [WindowControlPanel]                    | 
+----------------------------+-----------------------------------------------------+ 
| [ConversationListPanel]    |  [ChatHistoryPanel]                                 |
|                            |                                                     |
|                            |                                                     |
|                            |                                                     |                      |                            | [MessageInputPanel] [SendButton]                    | +----------------------------+-----------------------------------------------------+ 
|                      [Status Bar: Connection + Logs]                             | +----------------------------------------------------------------------------------+
````

## 🔌 How It Works

- The GUI launches the compiled C client as a subprocess
- Frames are sent via `stdin` and received via `stdout`
- The GUI parses and displays messages, file progress, and ACKs
- All protocol logic remains in C — Python acts as a visual wrapper

---
## 🚀 Getting Started

### 1. Compile the C client
```bash
cd client
make
```
### 2. Install Python dependencies

```bash
pip install -r requirements.txt
```
###  3. Run the GUI
```bash
cd client_gui
python main.py
```

---


## 🚀 Features

- ✅ C-based protocol logic with CRC validation
- ✅ PyQt5 GUI with modular panels and subprocess integration
- ✅ Drag-and-drop file sending
- ✅ Auto-version bump via GitHub Actions
- ✅ Binary sync to external test suite repo

## 🧑‍💻 Contributor Notes

- GUI logic is fully modular — each panel is its own class
- C client is launched via `subprocess.Popen` with stdin/stdout piping
- Protocol parsing is mirrored in `client_gui/protocol.py` for consistency
- All commits and PRs follow contributor templates and CI validation

## 🧪 Testing

- Run `make all` to build C binaries
- Launch GUI via `python client_gui/main.py`
- CI builds and releases are automated via GitHub Actions

---


---

### 🛠️ Implementation Notes

- Use `QSplitter` to divide sidebar and main panel
- Use `QStackedWidget` to switch between conversations
- `ChatHistoryPanel` is scrollable (`QTextEdit` or `QListView`)
- `MessageInputPanel` uses `QLineEdit` or `QTextEdit` with drag-and-drop support
- `SendButton` triggers frame construction and subprocess send
- `UserStatusHeader` can be a `QWidget` with `QHBoxLayout` (avatar + label + status)
- `WindowControlPanel` can be native or custom-drawn with `QPushButton`s

---

### 🔄 Signal Flow Example

| From                  | Signal/Event         | To                     | Action                                 |
|-----------------------|----------------------|-------------------------|----------------------------------------|
| MessageInputPanel     | `message_sent(str)`  | ClientBridge            | Send frame to C client via stdin       |
| ClientBridge          | `frame_received(str)`| ChatHistoryPanel        | Append parsed message to history       |
| FilePanel             | `file_selected(path)`| ClientBridge            | Begin chunked file transfer            |
| ClientBridge          | `ack_received(file)` | FilePanel               | Update progress bar                    |

---


