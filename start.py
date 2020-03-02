import exceptions, os, sys
import game

if __name__ == "__main__":
    try:
        game.init.start()

    except exceptions.QuitGameException as E:
        if E.code is "restart":
            print("Restarting...")
            print("Todo: argv")

            # opens a second window
            os.system("python start.py")

            # but... unfortunately, we don't get to here until the second window closes
            sys.exit()
