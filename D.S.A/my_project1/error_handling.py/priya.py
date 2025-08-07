import json

# Load videos from the file
def load_data():
    try:
        with open("youtube.txt", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

# Save videos to the file
def save_data_helper(videos):
    with open("youtube.txt", "w") as file:
        json.dump(videos, file, indent=4)

# List all videos
def list_all_videos(videos):
    if not videos:
        print("No videos found.")
    for index, video in enumerate(videos, start=1):
        print(f"{index}. {video['name']} ({video['time']})")

# Add a new video
def add_video(videos):
    name = input("Enter video name: ")
    time = input("Enter video time: ")
    videos.append({'name': name, 'time': time})
    save_data_helper(videos)
    print("Video added successfully!")

# Update existing video
def update_video(videos):
    list_all_videos(videos)
    try:
        index = int(input("Enter the number of the video to update: ")) - 1
        if 0 <= index < len(videos):
            name = input("Enter new name (leave blank to keep current): ")
            time = input("Enter new time (leave blank to keep current): ")

            if name:
                videos[index]['name'] = name
            if time:
                videos[index]['time'] = time

            save_data_helper(videos)
            print("Video updated successfully!")
        else:
            print("Invalid video number.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Delete a video
def delete_video(videos):
    list_all_videos(videos)
    try:
        index = int(input("Enter the number of the video to delete: ")) - 1
        if 0 <= index < len(videos):
            deleted = videos.pop(index)
            save_data_helper(videos)
            print(f"Deleted video: {deleted['name']}")
        else:
            print("Invalid video number.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Main program
def main():
    videos = load_data()
    while True:
        print("\nYouTube Manager | Choose an option:")
        print("1. List all YouTube videos")
        print("2. Add a YouTube video")
        print("3. Update a YouTube video")
        print("4. Delete a YouTube video")
        print("5. Exit the app")
        choice = input("Enter your choice: ")

        match choice:
            case "1":
                list_all_videos(videos)
            case "2":
                add_video(videos)
            case "3":
                update_video(videos)
            case "4":
                delete_video(videos)
            case "5":
                break
            case _:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
