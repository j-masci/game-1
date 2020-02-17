from app import App
import exceptions, os

if __name__ == "__main__":
    try:
        app = App()
    except exceptions.QuitGameException as E:
        if E.code is "restart":
            print("Restarting...")
            print("Todo: argv")
            os.system("python start.py")
