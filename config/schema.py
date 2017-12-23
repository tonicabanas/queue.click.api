import graphene

import queueclick.queues.schema


class Queries(
    graphene.ObjectType,
    queueclick.queues.schema.Query,
):
    pass


schema = graphene.Schema(query=Queries)
