import os

def install_virtual_environment():
    print("Installing virtual environment")
    os.system("/bin/bash --rcfile ./install_venv.sh")


def main():    
    # activate venv
    install_virtual_environment()


if __name__ == "__main__":
    main()
