
# Goblin Panel - Game Server Administration Panel

⚠️ **Warning: This is in ACTIVE development and is not currently suitable for production use.**

Welcome to the Goblin Panel core repository. This panel is designed as an alternative to Pterodactyl, utilizing a backend API approach to streamline complex deployments and integrate seamlessly with cloud services such as Cloudflare Zero Trust tunnels and other proxy solutions.

## Features
- Backend API Approach: Communicate via RESTful APIs for easier integration and deployment.
- Cloud-Friendly: Simplify deployments with support for Cloudflare Zero Trust tunnels and other proxy services.
- Flexible: Easily manage and configure multiple game servers from a single interface.
- Extensible: Built with modularity in mind for future enhancements and integrations.

## Getting Started
### Prerequisites
- Python >= 3.9
- Django >= 5.0.7
- A supported database (e.g., PostgreSQL, MySQL, MariaDB or Sqlite3)

### Installation
**1. Clone the Repository**
```
git clone https://github.com/HavenRealms/goblin-panel.git
cd game-server-panel
```
**2. Setup Python Virtual Environment**
```
python -m venv venv
```
**3. Install Required Packages & Dependencies**
```
python -m pip install -r requirements.txt
```
**4. Migrate Database**
```
python manage.py makemigrations
python manage.py makemigrations serveradmin
python manage.py migrate
```
**5. Run Django Server**
```
python manage.py runserver
```
This will start an instance of the Goblin Panel in a development environment available at https://localhost:8080/.

## API Documentation
For detailed information on how to interact with the panel via APIs, please refer to the [Wiki](https://github.com/HavenRealms/goblin-panel/wiki "Wiki").

## License

This project is licensed under the GPL v3 license - see the [LICENSE](https://github.com/HavenRealms/goblin-panel/blob/main/LICENSE "LICENSE") file for details.

## Contact
For any questions or support, please open an issue on GitHub or open a support ticket via our [discord](https://discord.gg/wsB7bPxxGe "discord").