<div id="top"></div>

<!-- PROJECT LOGO -->
<br/>
<div align="center">
  <a href="https://github.com/KDerec/Motus/blob/master/static/images/logo.png">
    <img src="static/images/logo.png" alt="Logo" width="100">
  </a>

<h3 align="center">Motus Simulation</h3>
  <p align="center">
  <a href="https://www.python.org">
    <img src="https://img.shields.io/badge/Python-3.12+-3776AB?style=flat&logo=python&logoColor=white" alt="python-badge">
  </a>
  <a href="https://www.djangoproject.com">
    <img src="https://img.shields.io/badge/Django-5.0+-092E20?style=flat&logo=django&logoColor=white" alt="django-badge">
  </a>
  </p>
  <p align="center">
    Mettez vos capacités à l'épreuve en relevant le défi de deviner des mots cachés dans cette simulation du célèbre jeu Motus !
  </p>
  </p>
</div>


<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#about-the-project">About The Project</a></li>
    <li><a href="#built-with">Built With</a></li>
    <li><a href="#installation">Installation</a></li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>


<!-- ABOUT THE PROJECT -->
## About The Project
Exercice pratique pour démontrer mes compétences en Django, JS, HTML et CSS pour un test.
Le projet n'est pas prévu pour une déploiement en production.

Après avoir suivi le guide d'installation, vous pouvez :
1. Partir de zéro et créer un compte admin avec la commande `python manage.py createsuperuser`,
2. Ajouter les trois utilisateurs ci-dessous en utilisant la commande `python manage.py loaddata sample` *(nom utilisateur : mot de passe)* :
   * JohnDoe : eT00cCMwdimeibv
   * JeanMichel : kYrK507nM5Oxqwa
   * admin : Kc1M3TPajtEmaLJ

### Built With
* [Python 3.12](https://www.python.org/)
* [Django 5.0](https://www.djangoproject.com/)

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- INSTALLATION -->
## Installation
0. *(shortcut) Pour exécuter les étapes 2 à 9 en une commande (testé sur macOs) :*
      ```sh
      git clone https://github.com/KDerec/Motus.git && cd Motus && python3 -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt && python manage.py migrate && python manage.py loaddata sample && python manage.py runserver
      ```
1. <a href="#python-installation">Install Python</a> ;
2. Clone the project in desired directory ;
   ```sh
   git clone https://github.com/KDerec/Motus.git
   ```
3. Change directory to project folder ;
   ```sh
   cd path/to/Motus
   ```
4. Create a virtual environnement *(More detail to [Creating a virtual environment](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment))* ;
    * For Windows :
      ```sh
      python -m venv .venv
      ```
    * For macOs / Linux :
      ```sh
      python3 -m venv .venv
      ```
5. Activate the virtual environment ;
    * For Windows :
      ```sh
      .\.venv\Scripts\activate
      ```
    * For macOS / Linux :
      ```sh
      source .venv/bin/activate
      ```
6. Install package of requirements.txt ;
   ```sh
   pip install -r requirements.txt
   ```
7. Apply migration ;
   ```sh
   python manage.py migrate
   ```
8. (optional) Load data in database (<a href="#about-the-project">see about project for more details</a>);
   ```sh
   python manage.py loaddata sample
   ```
9. Run your local server ;
   ```sh
   python manage.py runserver
   ```
10. Go to http://127.0.0.1:8000/, create an account and enjoy !

<p align="right">(<a href="#top">back to top</a>)</p>


#### Python installation
1. Install Python. If you are using Linux or macOS, it should be available on your system already. If you are a Windows user, you can get an installer from the Python homepage and follow the instructions to install it:
   - Go to [python.org](https://www.python.org/)
   - Under the Download section, click the link for Python "3.xxx".
   - At the bottom of the page, click the Windows Installer link to download the installer file.
   - When it has downloaded, run it.
   - On the first installer page, make sure you check the "Add Python 3.xxx to PATH" checkbox.
   - Click Install, then click Close when the installation has finished.

2. Open your command prompt (Windows) / terminal (macOS/ Linux). To check if Python is installed, enter the following command (this should return a version number.):
   ``` sh
   python -V
   # If the above fails, try:
   python3 -V
   # Or, if the "py" command is available, try:
   py -V
   ```

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- USAGE EXAMPLES -->
## Usage
L'application nécessite un compte utilisateur pour pouvoir jouer.
### Créer des nouveaux utilisateurs
Rendez-vous à l'adresse `/signup` et suivre les indications ou rendez-vous à l'adresse `/admin/motus/user/add/` connecté en tant qu'administrateur pour créer un compte utilisateur.
### Règle du jeu
Le jeu repose sur la recherche de mots d'un nombre fixé de lettres.
Le mot apparaît alors sur une grille : les lettres présentes et bien placées sont coloriées en rouge, les lettres présentes mais mal placées sont coloriés en jaune. Pour une lettre, on ne peut avoir au maximum que le nombre d'occurrences de cette lettre dans le mot de coloriées (soit en jaune, soit en rouge si certaines sont bien placées).
Si le joueur trouve le mot, il gagne des points équivalent au nombre de lettres du mot trouvé.
Les mots à deviner sont en anglais et la longueur des mots va de 3 à 8 lettres.
<p align="right">(<a href="#top">back to top</a>)</p>


<!-- LICENSE -->
## License
Distributed under the MIT License. See `LICENSE` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- CONTACT -->
## Contact
Kévin Dérécusson ->
Email : kevin.derecusson@outlook.fr ou
LinkedIn : https://www.linkedin.com/in/kevin-derecusson/

<p align="right">(<a href="#top">back to top</a>)</p>
