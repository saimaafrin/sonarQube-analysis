from neo4j import GraphDatabase

class Neo4jClient:
    def __init__(self, uri, auth):
        self.driver = GraphDatabase.driver(uri, auth=auth)

    def begin(self, mode=None, bookmarks=None, metadata=None, timeout=None,
              db=None, imp_user=None, dehydration_hooks=None,
              hydration_hooks=None, **handlers):
        with self.driver.session(bookmarks=bookmarks, default_access_mode=mode, default_database=db, default_transaction_timeout=timeout, impersonated_user=imp_user) as session:
            tx = session.begin_transaction()
            response = tx.run("BEGIN", metadata=metadata, dehydration_hooks=dehydration_hooks, hydration_hooks=hydration_hooks, **handlers)
            return response