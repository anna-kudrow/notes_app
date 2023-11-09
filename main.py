from datetime import datetime
from Note import Note
import csv


def create_note():
    text = input("Write your note here: ")
    creating_date = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    with open("/Users/annakudravceva/Desktop/GEEKBRAINS/ControlWork/NotesPython/my_notes.csv", "r") as csvfile:
        reader = csv.reader(csvfile, delimiter=";")
        notes = list(reader)

        note_id = str(len(notes) + 1)

        note = Note(note_id, text, creating_date)

        with open("/Users/annakudravceva/Desktop/GEEKBRAINS/ControlWork/NotesPython/my_notes.csv", "a",
                  newline="") as csvfile:
            writer = csv.writer(csvfile, delimiter=";")
            writer.writerow([note.note_id, note.text, note.datetime])

        print("Your note created!")


def read_notes():
    with open("/Users/annakudravceva/Desktop/GEEKBRAINS/ControlWork/NotesPython/my_notes.csv", "r") as csvfile:
        reader = csv.reader(csvfile, delimiter=";")
        for row in reader:
            # print(f"{row[0]}) {row[1]}\t Created: {row[2]}\n")
            print(row[0] + ") " + row[1] + "\t" + "Created: " + row[2] + "\n")


def change_note():
    note_id = input("Which note you would like to change? Input it's ID: ")
    new_text = input("Write a new note instead of the previous one: ")
    new_datetime = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    with open("/Users/annakudravceva/Desktop/GEEKBRAINS/ControlWork/NotesPython/my_notes.csv", "r") as csvfile:
        reader = csv.reader(csvfile, delimiter=";")
        notes = list(reader)

    found = False
    with open("/Users/annakudravceva/Desktop/GEEKBRAINS/ControlWork/NotesPython/my_notes.csv", "w",
              newline="") as csvfile:
        writer = csv.writer(csvfile, delimiter=";")
        for note in notes:
            if note[0] == note_id:
                writer.writerow([note_id, new_text, new_datetime])
                found = True
            else:
                writer.writerow(note)
    if found:
        print("Your note changed =)")
    else:
        print("Note with this ID wasn't found =()")

def delete_note():
    note_id = input("Which note you would like to delete? Input it's ID: ")
    with open("/Users/annakudravceva/Desktop/GEEKBRAINS/ControlWork/NotesPython/my_notes.csv", "r") as csvfile:
        reader = csv.reader(csvfile, delimiter=";")
        notes = list(reader)

    found = False
    with open("/Users/annakudravceva/Desktop/GEEKBRAINS/ControlWork/NotesPython/my_notes.csv", "w",
              newline="") as csvfile:
        writer = csv.writer(csvfile, delimiter=";")
        for note in notes:
            if note[0] == note_id:
                writer.writerow(note)
                found = True
            else:
                writer.writerow(note)
    if found:
        print("Your note deleted =)")
    else:
        print("Note with this ID wasn't found =()")

print("====================== Welcome to the notes app!! ======================")

while True:
    print(
        "MENU:\n What would you like to do?\n\t 1 - create a new note \n\t 2 - read my notes \n\t 3 - change a note \n\t 4 - delete a note \n\t 5 - exit")

    user_choise = int(input("Enter what you need: "))
    if user_choise == 1:
        create_note()
    elif user_choise == 2:
        read_notes()
    elif user_choise == 3:
        change_note()
    elif user_choise == 4:
        delete_note()
    if user_choise == 5:
        print("====================== See you next time!! ======================\n")
        break
    else:
        ("Please choose a point from the menu from 1 to 5")
