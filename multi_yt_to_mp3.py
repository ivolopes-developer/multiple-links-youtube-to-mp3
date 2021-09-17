import youtube_dl
import os
import time


url_list = []


def getURL():
    os.system("cls")
    urls = input(
        "\n\nInsert here your URLs separated with ',' and then press ENTER to continue -> ")
    urls_without_spaces = urls.replace(" ", "")

    # spliting the urls by commas
    final_urls = urls_without_spaces.split(",")

    return final_urls


def menu():
    os.system("cls")
    option = 0
    while (option != '1') and (option != '2'):
        print("""

            1) Insert URLs
            2) Exit
        
        """)

        option = input("\tOpção -> ")

        if option == '1':
            # get the urls
            url_list = getURL()
            # start converting the urls
            convertURLs(url_list)
        elif option == '2':
            os.system("cls")
            exit()


def convertURLs(urls):
    convert_counter = 1

    for url in urls:
        print(f"\nStarting converting the {convert_counter} URL...")
        video_info = youtube_dl.YoutubeDL().extract_info(
            url=url, download=False
        )
        filename = f"{video_info['title']}.mp3"

        options = {
            'format': 'bestaudio/best',
            'keepvideo': False,
            'outtmpl': filename,
        }

        with youtube_dl.YoutubeDL(options) as ydl:
            ydl.download([video_info['webpage_url']])

        print(f"URL {convert_counter} -> download complete... | {filename}")

        convert_counter += 1

        time.sleep(2)

    menu()


def hello():
    os.system("cls")
    print(""" 
            HHHHHHHHH     HHHHHHHHH                   lllllll lllllll                  
            H:::::::H     H:::::::H                   l:::::l l:::::l                  
            H:::::::H     H:::::::H                   l:::::l l:::::l                  
            HH::::::H     H::::::HH                   l:::::l l:::::l                  
              H:::::H     H:::::H      eeeeeeeeeeee    l::::l  l::::l    ooooooooooo   
              H:::::H     H:::::H    ee::::::::::::ee  l::::l  l::::l  oo:::::::::::oo 
              H::::::HHHHH::::::H   e::::::eeeee:::::eel::::l  l::::l o:::::::::::::::o
              H:::::::::::::::::H  e::::::e     e:::::el::::l  l::::l o:::::ooooo:::::o
              H:::::::::::::::::H  e:::::::eeeee::::::el::::l  l::::l o::::o     o::::o
              H::::::HHHHH::::::H  e:::::::::::::::::e l::::l  l::::l o::::o     o::::o
              H:::::H     H:::::H  e::::::eeeeeeeeeee  l::::l  l::::l o::::o     o::::o
              H:::::H     H:::::H  e:::::::e           l::::l  l::::l o::::o     o::::o
            HH::::::H     H::::::HHe::::::::e         l::::::ll::::::lo:::::ooooo:::::o
            H:::::::H     H:::::::H e::::::::eeeeeeee l::::::ll::::::lo:::::::::::::::o
            H:::::::H     H:::::::H  ee:::::::::::::e l::::::ll::::::l oo:::::::::::oo 
            HHHHHHHHH     HHHHHHHHH    eeeeeeeeeeeeee llllllllllllllll   ooooooooooo    
    """)
    time.sleep(3)

    menu()


if __name__ == '__main__':
    hello()
