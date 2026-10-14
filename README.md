# Playlist Manager

A lightweight Python CLI application that implements a music playlist using a custom **Doubly Linked List** data structure. The application enables sequential track navigation, dynamic track addition, and playback tracking through interactive terminal menus.

---

## Key Features

* **Doubly Linked List Core**: Built from scratch without external libraries using custom `Song` nodes and pointer references (`next` and `prev`).


* **Dynamic Track Management**: Append new songs (`title` and `artist`) to the end of the playlist in real time.


* **Sequential Navigation**: Move seamlessly forward (`next_song`) and backward (`previous_song`) through the playlist while tracking current playback state.


* **Interactive CLI Interface**: Terminal menu driving playlist setup, track playback, list display, and execution control.



---

## Technical Specifications & Architecture

### Data Structure Breakdown

1. **`Song` Node**: Represents individual tracks storing:
* `title`: Track name


* `artist`: Performer name


* `next`: Reference pointer to the succeeding track


* `prev`: Reference pointer to the preceding track




2. **`Playlist` Controller**: Manages pointer bounds and playback state:
* `head`: Points to the first track in the doubly linked list


* `tail`: Points to the last track in the doubly linked list


* `current`: Tracks the currently selected node/song





---

## Applications & Educational Uses

* **Data Structures Implementation**: Practical visual example of doubly linked lists, showing bi-directional traversal and dynamic memory linkage without reliance on built-in array/list operations.


* **State & Pointer Management**: Demonstrates maintaining state pointers (`head`, `tail`, `current`) during list insertions and iterations.


* **CLI Software Design**: Practical template for developing interactive command-line interface systems with menu loops.



---

## Requirements & Execution

### Prerequisites

* **Python 3.x**


### Running the Application

1. Save the source code into `playlist.py`.


2. Execute the script via terminal or command prompt:

```bash
python playlist.py

```

---

## Interactive Menu Guide

| Option | Action | Description |
| --- | --- | --- |
| **1** | `Add Song` | Prompts for track title and artist, then appends the song to the end of the playlist.|
| **2** | `Play Current Song` | Prints the details of the currently active track.|
| **3** | `Next Song` | Advances playback pointer to the next track if available.|
| **4** | `Previous Song` | Moves playback pointer back to the preceding track if available.|
| **5** | `Display Playlist` | Iterates from `head` to `tail` and prints all songs in sequential order.|
| **6** | `Exit` | Terminates the terminal loop and closes the application.|
