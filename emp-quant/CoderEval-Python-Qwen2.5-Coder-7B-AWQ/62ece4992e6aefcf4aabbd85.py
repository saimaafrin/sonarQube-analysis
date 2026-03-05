from typing import Optional, Set
from rdflib import Graph, URIRef, Node

def find_roots(graph: Graph, prop: URIRef, roots: Optional[Set[Node]] = None) -> Set[Node]:
    if roots is None:
        roots = set()
    
    for node in graph.subjects(prop=None):
        if not any(graph.has_predicate(node, prop, parent) for parent in graph.objects(node, prop)):
            roots.add(node)
    
    return roots