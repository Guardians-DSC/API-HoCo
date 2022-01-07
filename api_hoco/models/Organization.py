from .db import mongo

class Organization:
    def __init__(self, name, github_url, image):
        self.name = name
        self.github = github_url
        self.image = image

    def save(self):
        try:
            org_image = f'{self.name}-logo'

            mongo.save_file(org_image, self.image)
            
            mongo.db.organization.insert_one({
                'name': self.name,
                'github_url': self.github,
                'image_id': org_image,
            }) 

            return True
        except Exception as e:
            return str(e)


