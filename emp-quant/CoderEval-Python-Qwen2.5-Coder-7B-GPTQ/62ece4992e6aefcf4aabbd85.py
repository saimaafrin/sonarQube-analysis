from typing import Optional, Set
from rdflib import Graph, URIRef, Node

def find_roots(
    graph: Graph, prop: URIRef, roots: Optional[Set[Node]] = None
) -> Set[Node]:
    if roots is None:
        roots = set()
    
    for s, p, o in graph.triples((None, prop, None)):
        if o not in roots and not any(graph.has_predicate(o, prop)):
            roots.add(s)
    
    return roots