
import json

def load_data():
    try:
        with open("youtube.txt","r")as file:
            return json.load(file)
            
    except FileNotFoundError:
        return[]
    

def list_all_videos(videos):
    pass
def add_video(videos):
    pass

def update_video(videos):
    pass
def delete_video(videos):
    passgit 





def main():
    videos = load_data()
    


while True:
    print("/n youtube manager | choose an option")
    print("1.list a all youtube videos")
    print("2.add youtube video")
    print("3.update a youtube video details")
    print("4.delete a youtube video")
    print("5.exit the app")
    
    choice =  input("enter your choice")
    
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
            print("invalid choice")
            



if __name__ == "__main__":
    main()
    
