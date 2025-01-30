# GitHubStalker
Different solution for the [github-user-activity](https://roadmap.sh/projects/github-user-activity) challenge from [roadmap.sh](https://roadmap.sh/) by using **Python** languege and **Django** framework.

## How to run
1- Clone the repository:
```bash
git clone https://github.com/soheildeb/GitHubStalker.git
cd GitHubStalker
```
2- Install venv and Make virtuel envirement:
```bash
sudo apt install python3-venv
python3 -m venv venv
source venv/bin/activate
```
3- Install requirements
```bash
python3 -m pip install -r requirements.txt
```
3- Run the application:
```bash
cd GitHubStalker
./manage.py runserver 8000
```

## How to use the app
1- Open the app on your browser ([click](https://roadmap.sh/projects/github-user-activity)).
2- Enter the username of the person whose activity you want to view.
The access token only needed when the API is limited without authentication for your IP, you just have to enter a **read only** access token.
