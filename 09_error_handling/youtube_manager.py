import json

fileName = "youtube.txt"


def save_data_helper(videos):
    with open(fileName, "w") as file:
        json.dump(videos, file)


def list_all_video(videos):
    print("\n")
    print("*" * 50)
    for index, video in enumerate(videos, start=1):
        print(f"{index}. {video['name']}, Duration:  {video['time']}")


def add_video(videos):
    name = input("Enter a video name : ")
    time = int(input("Enter a video time : "))
    videos.append({"name": name, "time": time})
    save_data_helper(videos)


def update_video(videos):
    list_all_video(videos)
    index = int(input("Enter the video name to update : "))
    if 1 <= index <= len(videos):
        name = input("Enter a new video name : ")
        time = int(input("Enter a new video time : "))
        videos[index - 1] = {"name": name, "time": time}
        save_data_helper(videos)
    else:
        print("Invalid choice")


def delete_video(videos):
    list_all_video(videos)
    index = int(input("Enter the video name to delete : "))
    if 1 <= index <= len(videos):
        videos.pop(index - 1)
        save_data_helper(videos)
    else:
        print("Invalid choice")


def load_data():
    try:
        with open(fileName) as file:
            return json.load(file)

    except FileNotFoundError:
        return []


def main():
    videos = load_data()
    while True:
        print("\n1. List all videos")
        print("\n2. Add a video")
        print("\n3. Update a video")
        print("\n4. Delete a video")
        print("\n5. Exit")
        choice = int(input("\nEnter the number : "))

        match choice:
            case 1:
                list_all_video(videos)
            case 2:
                add_video(videos)
            case 3:
                update_video(videos)
            case 4:
                delete_video(videos)
            case 5:
                break
            case _:
                print("Invalid choice")


if __name__ == "__main__":
    main()
