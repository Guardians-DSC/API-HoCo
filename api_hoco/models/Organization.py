from .db import mongo

class Organization:
    def __init__(self, name, github_url, image):
        self.name = name
        self.url = github_url
        self.image = image

    def to_string(self):
        return { 
            'name': self.name,
            'org_url': self.url,
            'image_id': f'{self.name}-logo'
        }

    def save(self):
        org_image = f'{self.name}-logo'

        mongo.save_file(org_image, self.image)
        
        org = self.to_string()

        mongo.db.organization.insert_one(org) 

        return mongo.db.organization.find_one({ 'name': self.name })


