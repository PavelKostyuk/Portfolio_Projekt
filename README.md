![Logo](https://www.mattlayman.com/img/python-django.png)


# 🚀 Portfolio with Python and Django/Bootstrap5
[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/) [![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue)](https://www.linkedin.com/in/pavel-kostyuk-710a521b8/) <img src="https://komarev.com/ghpvc/?username=pavelkostyuk&label=Repository%20views&color=0e75b6&style=flat" alt="pavelkostyuk"/>




<p style="font-size: 34px;">
Build a simple portfolio to clearly show the projects you are working on. The idea of the project is to create a website where you can showcase your ongoing as well as upcoming projects. This project uses the Bootstrap5 template and aims to cover the breadth between the software development process and the infrastructure it is configured on. Learning the DevOps mindset - from code to server.</p>




### 🏗️ Site in production. What you're going to get as a result.

Here's what it looks like running on the server: [Click here to see my Portfolio build](https://www.pavel-kostyuk-portfolio.tech/)


<details>
<summary style="font-size: 1.5em;"><h3>🍭 Features</h3></summary>

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
<summary style="font-size: 1.5em;"><h3>🖥️ Run Locally</h2></h3></summary>

  
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

Run the server

```cmd
python manage.py runserver
```

Stop running server

```cmd
PRESS CTRL+C 
```
Create user for admin panel 

```cmd
python manage.py createsuperuser
```
- Note: No need for email. Create something simple like "admin" with password "abc123"

- Browese to http://127.0.0.1:8000/admin and login

- Press Project and create your first project



  </details>



