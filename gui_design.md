# 🖼️ GUI Design: Qt Client Interface

This document outlines the design and layout of the PyQt5-based GUI client for the `Server_Client-C-app` project. The server remains command-line; this interface is for client-side interaction only.

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

## 🧩 Components

### 🔹 Header
- App title: `Server_Client-C-app`
- Client ID display
- Optional: Settings icon

### 🔹 User List (Sidebar)
- List of connected clients
- Click to select target for chat or file

### 🔹 Chat Panel
- Scrollable message history
- Input box with send button
- Message timestamps and sender labels

### 🔹 File Panel
- File picker
- Send button
- Progress bar per transfer
- Retry and ACK indicators

### 🔹 Status Bar
- Connection status (e.g., Connected to server)
- Log messages (optional toggle)

---

## 🎨 Style Guide

- Font: Segoe UI or system default
- Theme: Light mode (dark mode optional)
- Icons: SVG from `assets/icons/`
- Responsive layout using `QVBoxLayout`, `QHBoxLayout`, and `QSplitter`

---

## 🔌 Event Flow

| Action            | Triggered By       | Result                          |
|-------------------|--------------------|----------------------------------|
| Send message      | Chat input         | Frame sent to server            |
| Receive message   | Socket event       | Message displayed in chat panel |
| Send file         | File panel button  | Chunked transfer begins         |
| Receive file      | Socket event       | Progress bar updates            |
| ACK received      | Socket event       | Transfer marked complete        |

---

## 🧠 Future Enhancements

- Group chat support
- Emoji picker
- Markdown rendering
- Voice/video hooks
- Notification system

---

## 📂 File Mapping

| File               | Purpose                          |
|--------------------|----------------------------------|
| `main.py`          | App entry point                  |
| `chat_panel.py`    | Chat UI logic                    |
| `file_panel.py`    | File transfer UI                 |
| `client_socket.py` | TCP socket and protocol handling |
| `protocol.py`      | Frame construction/parsing       |
| `assets/icons/`    | UI icons                         |

---

## 👥 Contributor Notes

- Use `PyQt5` signals/slots for UI updates
- Keep UI logic separate from network logic
- Follow naming conventions and comment key flows
- Log socket events for debugging

---

