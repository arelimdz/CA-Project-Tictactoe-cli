from menu_system import start_menu_system


def main():
    try:
        start_menu_system()
    except KeyboardInterrupt:
        return


if __name__ == "__main__":
    main()
