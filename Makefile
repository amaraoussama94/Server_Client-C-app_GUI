##
# @file Makefile
# @brief Unified build script for C server/client and Python GUI.
#        Supports cross-platform compilation and packaging.
#
#        - Builds C server and client using GCC and Make
#        - Builds Python GUI using PyInstaller (Windows/Linux)
#        - Includes clean targets for both C and GUI artifacts
#
# @author Oussama Amara
# @version 2.0
# @date 2025-10-20
##

# ─── Compiler and Paths ─────────────────────────────────────
CC = gcc
CFLAGS = -Wall -Wextra -Iinclude
SRC_DIR = src
OBJ_DIR = build
BIN_DIR = build/bin

# ─── Source and Object Files ────────────────────────────────
SRCS := $(shell find $(SRC_DIR) -name "*.c")
OBJS := $(patsubst $(SRC_DIR)/%.c,$(OBJ_DIR)/%.o,$(SRCS))

# ─── Platform Detection ─────────────────────────────────────
ifeq ($(OS),Windows_NT)
PLATFORM_LIBS = -lws2_32
CFLAGS += -D_WIN32 -mconsole
TARGET_SERVER = $(BIN_DIR)/server.exe
TARGET_CLIENT = $(BIN_DIR)/client.exe
GUI_BINARY = build/bin/ServerClientGUI.exe
PYINSTALLER_FLAGS = --onefile --windowed --name ServerClientGUI
else
PLATFORM_LIBS =
TARGET_SERVER = $(BIN_DIR)/server
TARGET_CLIENT = $(BIN_DIR)/client
GUI_BINARY = build/bin/ServerClientGUI
PYINSTALLER_FLAGS = --onefile --name ServerClientGUI
endif

DEPFLAGS = -MMD -MP
CFLAGS += $(DEPFLAGS)

.PHONY: all clean gui clean-gui

# ─── Build All C Targets ────────────────────────────────────
all: $(TARGET_SERVER) $(TARGET_CLIENT)

# ─── Server Build ───────────────────────────────────────────
$(TARGET_SERVER): $(OBJS)
		@echo " Linking $@..."
		@mkdir -p $(BIN_DIR)
		$(CC) $(CFLAGS) -o $@ \
				$(filter build/server/%.o build/features/%.o build/protocol/%.o build/utils/%.o,$(OBJS)) \
				$(PLATFORM_LIBS)

# ─── Client Build ───────────────────────────────────────────
$(TARGET_CLIENT): $(OBJS)
		@echo " Linking $@..."
		@mkdir -p $(BIN_DIR)
		$(CC) $(CFLAGS) -o $@ \
				$(filter build/client/%.o build/features/%.o build/protocol/%.o build/utils/%.o,$(OBJS)) \
				$(PLATFORM_LIBS)

# ─── Object Compilation ─────────────────────────────────────
$(OBJ_DIR)/%.o: $(SRC_DIR)/%.c
		@mkdir -p $(dir $@)
		$(CC) $(CFLAGS) -c $< -o $@

# ─── Dependency Includes ────────────────────────────────────
-include $(OBJS:.o=.d)

# ─── GUI Build (Python + PyInstaller) ───────────────────────
# Detect platform
UNAME_S := $(shell uname -s)
IS_MSYS := $(findstring MINGW,$(UNAME_S))

ifeq ($(IS_MSYS),MINGW)
PYTHON=python
INSTALL_PYINSTALLER=pacman -S --noconfirm mingw-w64-x86_64-pyinstaller
INSTALL_PYQT5=pacman -S --noconfirm mingw-w64-x86_64-python-pyqt5
else
PYTHON=python3
INSTALL_PYINSTALLER=$(PYTHON) -m pip install pyinstaller
INSTALL_PYQT5=$(PYTHON) -m pip install PyQt5
endif

PYINSTALLER=pyinstaller
PYINSTALLER_FLAGS=--onefile --windowed
# ─── Build GUI Target ───────────────────────────────────────
build-gui:
	@echo " Building Python GUI..."
	@echo " Installing PyInstaller and PyQt5..."
	@$(INSTALL_PYINSTALLER) > /dev/null
	@$(INSTALL_PYQT5) > /dev/null
	@echo " Building Python GUI executable..."
	@$(PYINSTALLER) $(PYINSTALLER_FLAGS) --distpath $(BIN_DIR)  client_gui/main.py
	@echo " GUI built: $(GUI_BINARY)"
	@echo " Copying assets to $(BIN_DIR)..."
	@cp -r assets $(BIN_DIR)/assets
	@echo " GUI built: $(GUI_BINARY)"


# ─── Clean GUI Artifacts ────────────────────────────────────
clean-gui:
	@echo " Cleaning GUI build artifacts..."
	@rm -rf dist build client_gui/__pycache__ client_gui/*.spec

# ─── Clean C Artifacts ──────────────────────────────────────
clean:
	@echo " Cleaning C build artifacts..."
	@rm -rf $(OBJ_DIR) $(TARGET_SERVER) $(TARGET_CLIENT)
