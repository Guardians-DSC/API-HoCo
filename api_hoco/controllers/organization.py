from flask import Flask
from api_hoco.models.Organization import Organization

def register_org(name, github_url, org_image):
    try:
        new_org = Organization(name, github_url, org_image)
        print(vars(new_org))
        resultado = new_org.save()
        
        return {'resultado': resultado } 
    except Exception as e:
        return {'resultado': str(e)} 
        


    



