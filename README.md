# Doubly Linked List Music Playlist Manager

A lightweight Python CLI application that implements a music playlist using a custom **Doubly Linked List** data structure. The application enables sequential track navigation, dynamic track addition and removal, and playback tracking through an interactive terminal menu.

---

## Key Features

* **Doubly Linked List Core**: Built from scratch using custom `Song` nodes and pointer references (`next` and `prev`).


* **Dynamic Track Management**:
* **Add Songs**: Append new songs (`title` and `artist`) to the end of the playlist.


* **Remove Songs**: Search and remove songs by title with dynamic node unlinking and playback state reassignment.




* **Sequential Navigation**: Move forward (`next_song`) and backward (`previous_song`) through the playlist while tracking current playback state.


* **Interactive CLI Interface**: Terminal menu driving playlist configuration, track playback, list display, and execution control.



---

## Technical Specifications & Architecture

### Data Structure Breakdown

1. **`Song` Node**: Represents individual tracks storing:
* `title`: Track name


* `artist`: Performer name


* `next`: Pointer reference to the succeeding track


* `prev`: Pointer reference to the preceding track




2. **`Playlist` Controller**: Manages list operations, pointer adjustments, and active state:
* `head`: Points to the first track in the doubly linked list


* `tail`: Points to the last track in the doubly linked list


* `current`: Tracks the currently selected track node


* `remove_song(title)`: Locates matching node by title and handles `head`, `tail`, `prev`, `next`, and active `current` pointer reassignment.





---

## Applications & Educational Uses

* **Data Structures & Pointer Manipulation**: Illustrates real-world applications of doubly linked lists, specifically edge-case node deletion (updating `head`, `tail`, and sibling pointers).


* **Active State Resiliency**: Shows how active pointers (`current`) can fall back gracefully to neighboring nodes (`next` or `prev`) when an active item is deleted.


* **CLI System Engineering**: Practical example for building interactive stateful command-line tools.



---

## Requirements & Execution

### Prerequisites

* **Python 3.x**


### Running the Application

1. Save the source code into `playlist_2.py`.


2. Execute the script via terminal or command prompt:

```bash
python playlist_2.py

```

---

## Interactive Menu Guide

| Option | Action | Description |
| --- | --- | --- |
| **1** | `Add Song` | Prompts for title and artist, then appends the song to the end of the playlist.|
| **2** | `Remove Song` | Prompts for a song title, unlinks its node from the list, and updates active playback.|
| **3** | `Play Current Song` | Prints details of the currently active track.|
| **4** | `Next Song` | Advances playback pointer to the next track if available.|
| **5** | `Previous Song` | Moves playback pointer back to the preceding track if available.|
| **6** | `Display Playlist` | Iterates from `head` to `tail` and prints all songs in sequential order.|
| **7** | `Exit` | Terminates the loop and exits the application.|
