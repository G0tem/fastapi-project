

class EntityRepositories:
    """Class for entity repositories."""
    @staticmethod
    def get_entity():
        return {"id": 1, "name": "entity!!!", "description": "GET_Hello, entity!!!"}
    
    @staticmethod
    def post_entity():
        return {"message": "POST_Hello, entity!!!"}
