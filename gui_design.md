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

## 🧱 Layout Overview

---
````text
+--------------------------------------------------------+
| [Header] App title + Client ID                        |
+-------------------+------------------------------------+
| [Sidebar]         | [Main Panel]                      |
| - Chat            | - Message history                 |
| - Files           | - Compose box                     |
| - Settings        | - File transfer panel             |
+-------------------+------------------------------------+
| [Status Bar] Connection + Logs                        |
+--------------------------------------------------------+

````
---

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

