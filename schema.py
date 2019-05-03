import graphene
import json
from datetime import datetime

class User(graphene.ObjectType):
    id = graphene.ID()
    username = graphene.String()
    created_at = graphene.DateTime()


class Query(graphene.ObjectType):
    users = graphene.List(User)
    hello = graphene.String()
    is_admin = graphene.Boolean()

    def resolve_hello(self, info):
        return "world"

    def resolve_is_admin(self, info):
        return True

    def resolve_users(self, info):
        return [
            User(id="1", username="Ann", created_at=datetime.now()),
            User(id="2", username="Ben", created_at=datetime.now()),
            User(id="3", username="Cathy", created_at=datetime.now()),
            User(id="4", username="Don", created_at=datetime.now()),
            User(id="5", username="Emily", created_at=datetime.now())
        ]

schema = graphene.Schema(query = Query)

result = schema.execute(
    '''
    {
        users {
            id
            username
            createdAt
        }
    }
    '''
)

dictResult = dict(result.data.items())
print(json.dumps(dictResult, indent = 2))
