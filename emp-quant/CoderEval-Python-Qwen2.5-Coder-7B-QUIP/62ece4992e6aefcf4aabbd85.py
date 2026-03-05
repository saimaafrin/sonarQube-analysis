from typing import Optional, Set
from rdflib import Graph, URIRef

def find_roots(graph: Graph, prop: URIRef, roots: Optional[Set[URIRef]] = None) -> Set[URIRef]:
    if roots is None:
        roots = set()

    for s, _, _ in graph.triples((None, prop, None)):
        if s not in roots:
            roots.add(s)

    return roots