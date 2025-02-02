import os


def check_environment():
    environment = {
        "os_name": os.name,
        "platform": os.sys.platform,
        "python_version": os.sys.version,
        "current_directory": os.getcwd(),
    }
    return environment


if __name__ == "__main__":
    env_info = check_environment()
    for key, value in env_info.items():
        print(f"{key}: {value}")
