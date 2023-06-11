![Logo](https://www.mattlayman.com/img/python-django.png)


# 🚀 Portfolio with Python and Django/Bootstrap5
[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/) [![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue)](https://www.linkedin.com/in/pavel-kostyuk-710a521b8/) <img src="https://komarev.com/ghpvc/?username=pavelkostyuk&label=Repository%20views&color=0e75b6&style=flat" alt="pavelkostyuk"/>




<p style="font-size: 34px;">
Build a simple portfolio to clearly show the projects you are working on. The idea of the project is to create a website where you can showcase your ongoing as well as upcoming projects. This project uses the Bootstrap5 template and aims to cover the breadth between the software development process and the infrastructure it is configured on. Learning the DevOps mindset - from code to server.</p>




### 🏗️ Site in production. What you're going to get as a result.

Here's what it looks like running on the server: [Click here to see my Portfolio build](https://www.pavel-kostyuk-portfolio.tech/)


<details>
<summary style="font-size: 1.5em;"><h3>🍭 Features</h3></summary>

- This website is adaptive to screen size and works well on both mobile and desktop.
- You will be able to show a picture of yourself and write a short text about yourself on the home page.
- You will be able to showcase your projects on the "home" page.
- The site has a navigation header, and newly added projects will be displayed there too.
- You will be able to write and edit your blog posts in the admin panel with simple editing.
- You will be able to attach images, videos, and links in your posts.
- You will be able to create a separate contact page with your credentials.
- The website has functionality to upload images to the server and can use embedded video links.
- The website adds new projects in descending order from oldest to newest.
- You can customize the website as you want and use other different elements offered by Bootstrap 5. 

 </details>


<details>
<summary style="font-size: 1.5em;"><h3>🎓 Knowledge requirements for the project</h2></summary>

- Basic Python
- Basic Django
- Basic Linux server (Ubuntu)
- Basic understanding and experience working with GIT/GitHub (version control)
- Basic understanding of Cloud infrastructure
- Basic understanding of databases/SQL (even if you will not need to manually create the database and work with database design, you will need to have "a picture in your head" of how it works in the background because the project uses two databases SQL lite and PostgreSQL one for local development and the other is used on the server side in production).
- Basic understanding of network (HTTP/HTTPS; ports 80, 443, port redirecting, TSL, SSL, SSH)
- Basic understanding of the software development process.

</details>


<details>
<summary style="font-size: 1.5em;"><h3> 💲 Costs and Good to Know:</h2></summary>
  
  Additional costs include: purchasing a domain name, SSL certificate and using Cloud Infrastructure.
  To launch the application you will need to register with one of the following Cloud providers or another. I used DigitalOcean (see link below).
  
  - Domain names are relatively cheap if they are .se or .eu. The price goes up for .com .tech and .co but we're talking about a few hundred SEK at most.
  
  - ​​​​​​​SSL certificates are something you can save on as instead of buying one, you can configure one from Let'sEncrypt on the server side with automatic updates (their certificates are valid for three months)
  
  - Cloud Infrastructure or rather the resources that will be needed are minimal. Of course you can register with one of the big companies that offer Cloud solutions - Azure, AWS, Google and pay for what you use but as a student you can use discounts that go along with GitHub's "bundle" for students.
  
  - [Azure offers $100 for students where you can test their services and use a whole range of different services for free for 12 months](https://azure.microsoft.com/en-us/free/students/)
  - [AWS has a so-called Free Tier that you can use during the first 12 months](https://aws.amazon.com/free/?all-free-tier.sort-by=item.additionalFields.SortRank&all-free-tier.sort-order=asc&awsf.Free%20Tier%20Types=*all&awsf.Free%20Tier%20Categories=*all)
  - [Google Cloud has a program for students as well but I haven't explored it](https://cloud.google.com/edu/students)
  - [DigitalOcean offers $200 for students to use over a year. Click and see their offer here](https://www.digitalocean.com/github-students)
  
  </details>


<details>
<summary style="font-size: 1.5em;"><h3>🔬 Technologies</h2></summary>

- Bootstrap 5/ HTML/ CSS/ Javascript
- Python 3.11.0
- Django 4.2
- django-ckeditor 6.5.1
- gunicorn 19.9.0
- whitenoise 6.4.0
- Pillow 9.5.0
  
  </details>
 
<details> 
<summary style="font-size: 1.5em;"><h3>🖥️ Run Locally</h3></summary>

  
❗Use CMD 
  
  
Clone the project

```cmd
git clone https://github.com/PavelKostyuk/Portfolio_Projekt.git
```

Go to the project directory

```cmd
cd Portfolio_Projekt\Portfolio
```

Create Virtual Env 

```cmd
virtualenv env 
```

Activate Virtual env

```cmd
cd env\scripts & activate  
```

Navigate back to right project directory to install dependencies

```cmd
   cd ..\.. 
```
  
Install dependencies

```cmd
pip install -r requirements.txt
```
  
Makemigrations and migrate to create DB (SQLlite)

```cmd
python manage.py makemigrations && python manage.py migrate
```


Collect static files

```cmd
python manage.py collectstatic
```


Create user for admin panel 

```cmd
python manage.py createsuperuser
```
- Note: No need for email. Create something simple like "admin" with password "abc123"

Run the server

```cmd
python manage.py runserver
```

- Browse to http://127.0.0.1:8000/admin on your local machine and login
- Press "Project" and create your first project.


Stop running server

```cmd
PRESS CTRL+C 
```

  </details>

<details> 
<summary style="font-size: 1.5em;"><h3> 📖 Acknowledgements</h3></summary>
 
Here are some resources I have used to make this project possible. I encourage you to use them to accomplish your project successfully.



- [Bootstrap5 Album-theme](https://getbootstrap.com/docs/5.3/examples/album/)
- [Quickstart: Deploy a Python (Django or Flask) web app to Azure App Service](https://learn.microsoft.com/en-us/azure/app-service/quickstart-python?tabs=flask%2Cwindows%2Cazure-cli%2Cvscode-deploy%2Cdeploy-instructions-azportal%2Cterminal-bash%2Cdeploy-instructions-zip-azcli)
- [Django 4 - Build Portfolio Project with Bootstrap 5 (2023) - Udemy.](https://www.udemy.com/course/django-3-build-portfolio-project-with-django-from-scratch/)
- [Python Django Dev To Deployment (2023) - Udemy.](https://www.udemy.com/course/python-django-dev-to-deployment/)
- [Deploy Django on Linux - Udemy.](https://www.udemy.com/course/deploy-django-on-linux/)
- [How-do-i-install-an-ssl-certificate-on-a-droplet](https://docs.digitalocean.com/support/how-do-i-install-an-ssl-certificate-on-a-droplet/)
- [How-to-install-ssl-certificates](https://www.namecheap.com/support/knowledgebase/article.aspx/795/14/how-to-install-ssl-certificates/)
- [How-to-create-a-self-signed-ssl-certificate-for-nginx-in-ubuntu-20-04-1](https://www.digitalocean.com/community/tutorials/how-to-create-a-self-signed-ssl-certificate-for-nginx-in-ubuntu-20-04-1)
- [Dokumentation från DigitalOcean – “How To Set Up Django with Postgres, Nginx, and Gunicorn on Ubuntu 18.04”](https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-18-04)
- [Simple Django Deployment (part 12) - Setting up Supervisor -YouTube](https://youtu.be/ny2L15dOf4Q)
- [Django- CKEditor Tutorial (+ CodeSnippet) -YouTube](https://youtu.be/L6y6cn1XUfw)
- [Awesome Readme Templates](https://awesomeopensource.com/project/elangosundar/awesome-README-templates)
- [Awesome README](https://github.com/matiassingers/awesome-readme)
- [How to write a Good readme](https://bulldogjob.com/news/449-how-to-write-a-good-readme-for-your-github-project)

 </details>
 
 <details> 
<summary style="font-size: 1.5em;"><h3>✒️ FAQ</summary>

#### Question 1: How do I deploy this project in a live production environment?
It depends on which platform you decide to use and how you want to deploy it. There are various ways to do it, so you can choose the one you like. I have provided information about deployment in the “acknowledgments” section. I used DigitalOcean as a cloud provider.

#### Question 2: Will you add new features to the project?
Yes, I will implement other things in the project and will update the repository accordingly with new features that I develop.

#### Question 3: Can I use this code and build my website on top of your initial setup?
Yes, you can modify the code as you like.
 
 </details>

 
 <details> 
<summary style="font-size: 1.5em;"><h3> ⚖️ License</summary>

MIT License

Copyright (c) 2023 Pavel Kostyuk

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

 </details>

