import pytest
from mixer.backend.django import mixer
from django.urls import reverse



@pytest.mark.django_db  # Ensure database access for this test
def test_home_view(client):
    # Assuming 'Project' is the model within the 'projects' app
    project = mixer.blend('projects.Project')

    # Replace 'reverse('home')' with the actual URL for your 'home' view
    response = client.get(reverse('home'))

    assert response.status_code == 200
    assert 'projects' in response.context
    assert project in response.context['projects']
    assert 'projects/home.html' in [template.name for template in response.templates]

@pytest.mark.django_db
def test_contact_view(client):
    project = mixer.blend('projects.Project')

    # Replace 'reverse('contact')' with the actual URL for your 'contact' view
    response = client.get(reverse('contact'))

    assert response.status_code == 200
    assert 'projects' in response.context
    assert project in response.context['projects']
    assert 'projects/contact.html' in [template.name for template in response.templates]

@pytest.mark.django_db
def test_detail_view(client):
    # Creating a sample project using mixer
    project = mixer.blend('projects.Project')

    # Constructing the URL for the detail view, assuming project.id is 1
    detail_url = reverse('detail', kwargs={'project_id': project.id})

    # Testing the view with an existing project_id
    response = client.get(detail_url)
    assert response.status_code == 200
    assert 'project' in response.context
    assert response.context['project'] == project
    assert 'projects' in response.context
    assert project in response.context['projects']
    assert 'projects/detail.html' in [template.name for template in response.templates]

#this test ensures that the detail view for a project functions correctly by checking various aspects 
# of the HTTP response, including context variables and the rendered template. 


