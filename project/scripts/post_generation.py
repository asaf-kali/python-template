import os
import shutil


def main():
    clean_up_providers()
    run_command("make lock")
    run_command("git add -A")
    run_command("make install")
    delete_myself()

    print("Project successfully generated!")
    print("Run `make` to show the available actions.")


def silence_errors(func):
    def wrapped(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except Exception:
            pass

    return wrapped


@silence_errors
def run_command(command):
    os.system(command)


@silence_errors
def rm(path):
    os.remove(path)


@silence_errors
def rmdir(path):
    shutil.rmtree(path)


def clean_up_providers():
    provider = "{{ repository_provider }}"
    if provider == "github.com":
        rm(".gitlab-ci.yml")
    elif provider == "gitlab.com":
        rmdir(".github")


def delete_myself():
    rm(__file__)


if __name__ == "__main__":
    main()
