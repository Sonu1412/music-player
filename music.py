import pygame
import os

def play_music(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

def stop_music():
    pygame.mixer.music.stop()

def main():
    print("Simple Music Player")
    print("-------------------")
    print("1. Play music")
    print("2. Stop music")
    print("3. Quit")

    while True:
        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            file_path = input("Enter the path to the music file: ")
            if os.path.exists(file_path):
                play_music(file_path)
                print("Playing music...")
            else:
                print("File not found!")
        elif choice == '2':
            stop_music()
            print("Music stopped.")
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
