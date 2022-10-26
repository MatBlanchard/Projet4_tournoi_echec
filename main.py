from controllers.controller import Controller

if __name__ == "__main__":
    try:
        Controller().start()
    except KeyboardInterrupt:
        print("\nFin du programme")
