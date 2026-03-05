from typing import Optional, Set
from rdflib import Graph, URIRef, Node

def find_roots(
    graph: Graph, prop: URIRef, roots: Optional[Set[Node]] = None
) -> Set[Node]:
    if roots is None:
        roots = set()
    
    for node in graph.subjects(prop):
        if not any(graph.has_statement((node, prop, parent)) for parent in roots):
            roots.add(node)
    
    return roots