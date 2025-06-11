"""
A simple command-line application for taking notes.

This script allows users to add new notes with a timestamp and view all
existing notes. Notes are stored in a local file named 'my_notes.txt'.
The script provides a basic command-line interface for interaction.
"""
import datetime

def add_note(note_content: str):
  """Adds a new note with a timestamp to the 'my_notes.txt' file.

  The note is formatted with the current date and time before being
  appended to the file.

  Args:
    note_content: The string content of the note to be added.
  """
  timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
  formatted_note = f"[{timestamp}] {note_content}\n"

  try:
    # Open the notes file in append mode ('a') to add the new note.
    # If the file doesn't exist, it will be created.
    with open("my_notes.txt", "a") as f:
      f.write(formatted_note)
  except IOError:
    # Catch IOError in case of issues like file permissions or disk full.
    print("Error: Could not write to the notes file.")

def view_notes():
  """Reads and displays all notes from 'my_notes.txt'.

  If the 'my_notes.txt' file doesn't exist or is empty, it prints a
  message indicating that there are no notes. Otherwise, it displays
  all notes with a header and footer.
  """
  try:
    # Open the notes file in read mode ('r').
    with open("my_notes.txt", "r") as f:
      notes = f.readlines()
      if not notes:
        # Check if the file is empty.
        print("Your notebook is empty.")
      else:
        print("--- Your Notes ---")
        for note in notes:
          print(note.strip()) # strip() to remove trailing newline from readlines()
        print("------------------")
  except FileNotFoundError:
    # Specific handling if the notes file does not exist.
    print("No notes found. Add a note first!")
  except IOError:
    # Catch other IOErrors that might occur during reading.
    print("Error: Could not read the notes file.")

def main():
  """Runs the command-line interface for the note-taking application.

  Presents a menu to the user to add notes, view notes, or exit.
  It continuously loops until the user chooses to exit.
  """
  while True:
    print("\nNote Taking App")
    print("1. Add Note")
    print("2. View Notes")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
      note_content = input("Enter your note: ")
      add_note(note_content)
      print("Note added!")
    elif choice == '2':
      view_notes()
    elif choice == '3':
      print("Exiting application.")
      break # Exit the while loop
    else:
      print("Invalid choice. Please try again.")

if __name__ == "__main__":
  # This block ensures that main() is called only when the script is executed directly,
  # not when it's imported as a module.
  main()
