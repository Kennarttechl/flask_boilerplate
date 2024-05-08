import os
from .css import DEMO_CSS
from .model import USER_MODEL
from .settings import APP_SETTINGS
from .html import BASE_HTML, FLASH_MESSAGE, DEMO_HTML_TEMPLATES
from .routes_ import (
    GITIGNORE,
    APP_STARTUP,
    SEARCH_FORM_DATA,
    VIEW_TEMPLATE_CODE,
    ADMIN_TEMPLATE_CODE,
    SEARCH_TEMPLATE_CODE,
    ERROR_HANDLER_TEMPLATE_CODE,
    AUTHENTICATION_TEMPLATE_CODE,
    RESET_PASSWORD_TEMPLATE_CODE,
)


# ANSI escape color code for displaying or printing sucessful message
GREEN = "\033[92m"
RESET = "\033[0m"


# ANSI escape color code for displaying or printing sucessful message
YELLOW = "\033[33m"
RESET = "\033[0m"


APP_STRUCTURE = {
    "templates": {
        "base.html": BASE_HTML, 
        "message.html": FLASH_MESSAGE
        },
    
    "views": {
        "routes.py": VIEW_TEMPLATE_CODE, 
        "__init__.py": ""
        },
    
    "errors": {
        "routes.py": ERROR_HANDLER_TEMPLATE_CODE,
        "__init__.py": "",
    },
    
    "authentication":{
      "routes.py": AUTHENTICATION_TEMPLATE_CODE,
      "form.py": "",
      "__init__.py": ""  
    },
    
    "password_reset":{
      "routes.py": RESET_PASSWORD_TEMPLATE_CODE,
      "form.py": "",
      "__init__.py": ""  
    },
    
    "search":{
      "routes.py": SEARCH_TEMPLATE_CODE,
      "form.py": SEARCH_FORM_DATA,
      "__init__.py": ""  
    },
    
    "admin":{
      "routes.py": ADMIN_TEMPLATE_CODE,
      "form.py": "",
      "__init__.py": ""  
    },

    "static": {
        "css": "base_main.css", 
        "js": "script.js", 
        "media": "flask_cli.png",
        },
    
    "database": {
        "models.py": USER_MODEL, 
        "__init__.py": ""
        },
    
    "config":{
        ".env": "",
        ".flaskenv": ""
    }
}


class CmdHandler:

    def init():
        print(f"{GREEN}Please wait, app is setting up virtual environment......{RESET}")

        os.system("pip install virtualenv")

        os.system("python -m venv venv")

        print(f"{GREEN}Successfully created virtual environment{RESET}")

        print("")

        print(
            f"{YELLOW}Please wait installing, Flask, Flask-Session, Flask-Limiter, flask-babel, Flask-Caching, Flask-Assets, Flask-SQLAlchemy and Flask-Migrate{RESET}"
        )

        os.system(
            "pip install Flask Flask-Assets flask-babel Flask-Bcrypt Flask-Caching Flask-Limiter Flask-Login Flask-Migrate Flask-Session Flask-SQLAlchemy Flask-WTF WTForms cssmin jsmin rcssmin rjsmin"
        )

        print(
            f"{GREEN}These packages are installed globally on your computer. To use them, activate your virtual environment and reinstall them inside.{RESET}"
        )

        print("")

        print(
            f"{YELLOW}To activate the virtual environment, navigate into the 'venv' directory and run 'Scripts/activate' on Windows or 'source bin/activate' on Unix-based systems.{RESET}"
        )

        print("")

    def create_flask_app_folder(app_folder_name):
        try:
            if not os.path.exists(app_folder_name):
                os.mkdir(app_folder_name)
                with open(file="app.py", mode="w") as file:
                    file.write(APP_STARTUP.replace("my_demo_app", app_folder_name))

                with open(
                    file=os.path.join(app_folder_name, "__init__.py"), mode="w"
                ) as file:
                    file.write(APP_SETTINGS.replace("my_demo_app", app_folder_name))

                with open(
                    file=os.path.join(app_folder_name, ".gitignore"), mode="w"
                ) as file:
                    file.write(GITIGNORE)

                for dir, content in APP_STRUCTURE.items():
                    os.mkdir(os.path.join(app_folder_name, dir))

                    if dir in [
                        "errors",
                        "views",
                        "authentication",
                        "admin",
                        "search",
                        "password_reset",
                    ]:
                        template_folder = os.path.join(
                            app_folder_name, dir, "templates"
                        )
                        os.mkdir(template_folder)

                        if dir == "errors":
                            error_files = [
                                "error_403.html",
                                "error_404.html",
                                "error_500.html",
                                "error_429.html",
                            ]
                            for error_file in error_files:
                                file_path = os.path.join(template_folder, error_file)
                                with open(file=file_path, mode="w") as file:
                                    file.write(
                                        f"<!-- This is the {error_file} template -->\n{DEMO_HTML_TEMPLATES}"
                                    )

                        else:
                            template_filenames = {
                                "views": "index.html",
                                "admin": "controller.html",
                                "search": "item_search.html",
                                "authentication": ["login.html", "register.html"],
                                # "authentication": "register.html",
                                "password_reset": "reset_pswd.html",
                            }

                            file_name = template_filenames.get(dir, None)
                            if isinstance(file_name, list):
                                for name in file_name:
                                    file_path = os.path.join(template_folder, name)
                                    with open(file=file_path, mode="w") as file:
                                        file.write(
                                            f"<!-- This is the {name} template -->\n{DEMO_HTML_TEMPLATES}"
                                        )
                            else:
                                file_path = os.path.join(template_folder, file_name)
                                with open(file=file_path, mode="w") as file:
                                    file.write(
                                        f"<!-- This is the {file_name} template -->\n{DEMO_HTML_TEMPLATES}"
                                    )

                            # file_name = template_filenames.get(dir, None)
                            # if file_name:
                            #     file_path = os.path.join(template_folder, file_name)
                            #     with open(file=file_path, mode="w") as file:
                            #         file.write(f"<!-- This is the {file_name} template -->\n{DEMO_HTML_TEMPLATES}")

                    if dir == "static":
                        for static_dir, value in content.items():
                            os.makedirs(os.path.join(app_folder_name, dir, static_dir))
                            with open(
                                file=os.path.join(
                                    app_folder_name, dir, static_dir, value
                                ),
                                mode="w",
                            ) as file:
                                file.write(DEMO_CSS)

                    if dir in [
                        "templates",
                        "views",
                        "errors",
                        "authentication",
                        "database",
                        "config",
                        "admin",
                        "search",
                        "password_reset",
                    ]:
                        for temp, value in content.items():
                            with open(
                                file=os.path.join(app_folder_name, dir, temp), mode="w"
                            ) as file:
                                file.write(
                                    value.replace("my_demo_app", app_folder_name)
                                )
            else:
                print(f"{YELLOW} The Folder {app_folder_name} already exists. {RESET}")
        except FileExistsError as e:
            print(f"{YELLOW} Error: {e}{RESET}")
