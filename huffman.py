from heapq import *
import judy_parser
import judy_objects
import distance

DONT_CARE = 'X'

def hamming_distance(node1, node2):
    if not node1 or not node2:
        return 100000000
    return distance.hamming(node1.bitmap, node2.bitmap)

def get_closest_cousin(ref_node, node_queue):
    closest_cousin = None
    remaining_nodes = node_queue[:]
    for node in remaining_nodes:
        if hamming_distance(ref_node, node) < hamming_distance(ref_node, closest_cousin):
            closest_cousin = node
    return closest_cousin

def generate_bitmap(node1, node2):
    assert len(node1.bitmap) == len(node2.bitmap)
    bitmap = ''
    for bit1, bit2 in zip(node1.bitmap, node2.bitmap):
        if bit1 is bit2:
            bitmap += bit1
        else:
            bitmap += DONT_CARE
    return bitmap

def find_contrasting_properties(node1, node2, schema):
    contrasting_properties = set()
    
    rev_schema = {v: k for k, v in schema.items()}
    i = 0
    for bit1, bit2 in zip(node1.bitmap, node2.bitmap):
        if bit1 != bit2 and bit1 != DONT_CARE and bit2 != DONT_CARE:
            contrasting_properties.add(rev_schema.get(i))
        i += 1
    return contrasting_properties

def generate_node_question(contrasting_properties):
    QN_PREFIX = 'Is it '
    QN_DELIMITER = ' OR '
    QN_SUFFIX = '?'

    question = ''
    return

def generate_tree(file_name):
    schema, node_queue = judy_parser.get_catalog(file_name)

    heapify(node_queue)
    while len(node_queue) > 1:
        l = heappop(node_queue)
        r = get_closest_cousin(l, node_queue)
        contrasting_properties = find_contrasting_properties(l, r, schema)

        n = judy_objects.Node(None, float(r.probability) + float(l.probability), generate_bitmap(l,r))
        n.setChildren(l,r)
        heappush(node_queue, n)
    return node_queue
