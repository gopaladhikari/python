from pymongo import MongoClient
from bson import ObjectId


client = MongoClient(
    "uri",
    tlsAllowInvalidCertificates=True,
)

db = client["python-mongo"]

video_collection = db["videos"]

# print(video_collection)


def add_video(name, time):
    video_collection.insert_one({"name": name, "time": time})


def list_all_video():
    for video in video_collection.find():
        print(f"id: {video['_id']} Name: {video['name']}  Time: {video['time']}")


def update_video(id, name, time):
    video_collection.update_one(
        {"_id": ObjectId(id)}, {"$set": {"name": name, "time": time}}
    )


def delete_video(id):
    video_collection.delete_one({"_id": ObjectId(id)})


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


if __name__ == "__main__":
    main()
