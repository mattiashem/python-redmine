import os
from redminelib import Redmine
from flask import Flask
app = Flask(__name__)


redmine = Redmine('https://redmine.fareoffice.com', key=os.environ['REDMINE_KEY'])
project = redmine.project.get('releases')
print(project.identifier)



@app.route("/new/<app>")
def new(app):
    # Create new release
    issue = redmine.issue.create(
        project_id='releases',
        subject='{} Deploy'.format(app),
        description='New deployment for {}'.format(app),
        custom_fields = [{ 'id':345,'value':app}]
    )
    return "created issue"






@app.route("/approve/<app>")
def approve(app):

    #Update to approved
    issues = redmine.issue.filter(
        project_id='releases',
        status_id=1,
        cf_345 = app,
        sort='created_on:desc'
    )
    update_issue =  issues[0]
    update = redmine.issue.update(
         update_issue.id,
         project_id='releases',
         status_id=172)

    return "Approved"



@app.route("/jenkins/<app>/<info>")
def jenkins(app,info):

    # Reject issu
    issues = redmine.issue.filter(
        project_id='releases',
        status_id='open',
        cf_345 = app,
        sort='created_on:desc'
    )
    
    update = redmine.issue.update(
         issues[0].id,
         project_id='releases',
         notes=info)
    return "Rejected"









@app.route("/reject/<app>")
def reject(app):

    # Reject issu
    issues = redmine.issue.filter(
        project_id='releases',
        status_id=172,
        cf_345 = app,
        sort='created_on:desc'
    )
    
    update = redmine.issue.update(
         issues[0].id,
         project_id='releases',
         status_id=6)
    return "Rejected"


@app.route("/deployed/<app>")
def deployed(app):

    # Reject issu
    #Update to approved
    issues = redmine.issue.filter(
        project_id='releases',
        status_id=172,
        cf_345 = app,
        sort='created_on:desc'
    )
    
    update = redmine.issue.update(
         issues[0].id,
         project_id='releases',
         status_id=13)
    return "Deployed"



if __name__ == "__main__":
    app.run(host='0.0.0.0')
