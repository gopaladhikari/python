import sqlite3

con = sqlite3.connect("youtube.db")
cursor = con.cursor()


cursor.execute(
    """
        CREATE TABLE IF NOT EXISTS videos (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            time TEXT NOT NULL
        )
"""
)


def add_video(name, time):
    cursor.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (name, time))
    con.commit()


def list_all_video():
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)


def update_video(id, name, time):
    cursor.execute("UPDATE videos SET name=?, time=? WHERE id=?", (name, time, id))
    con.commit()


def delete_video(id):
    cursor.execute("DELETE FROM videos WHERE id=?", (id,))
    con.commit()


def main():
    while True:
        print("\n1. List all videos")
        print("\n2. Add a video")
        print("\n3. Update a video")
        print("\n4. Delete a video")
        print("\n5. Exit")
        choice = int(input("\nEnter your choice : "))

        if choice == 1:
            list_all_video()

        elif choice == 2:
            name = input("Enter a video name : ")
            time = input("Enter a video time : ")
            add_video(name, time)

        elif choice == 3:
            video_id = int(input("Enter the video id : "))
            name = input("Enter a new video name : ")
            time = input("Enter a new video time : ")
            update_video(video_id, name, time)

        elif choice == 4:
            video_id = int(input("Enter the video id : "))
            delete_video(video_id)

        elif choice == 5:
            break

        else:
            print("Invalid choice")

    con.close()


if __name__ == "__main__":
    main()
