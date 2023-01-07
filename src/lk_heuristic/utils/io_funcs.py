import logging

from lk_heuristic.models.node import Node2D, Node3D

import tsplib95

# create a logger object
logger = logging.getLogger(__name__)

def import_tsp_file(tsp_file: str):
    """
    Import a .tsp file containing tsp definition and parse tsp header to a dictionary and tsp nodes to a list. Returns both objects in a tuple.

    *This function only works for .tsp instances of "TYPE" = TSP (symmetric tsp) and for "EDGE_WEIGH_TYPE" = EUC_2D or EUC_3D, which are the tsp problems that solver can handle currently.

    :param tsp_file: the .tsp file path
    :type tsp_file: str
    :return: a tuple with the header dict definition and a list of nodes
    :rtype: dict
    """

    # set the allowed type and edge weight for tsp
    allowed_types = ["TSP"]
    allowed_edge_weights = ["EUC_2D", "EUC_3D", "EXPLICIT"]

    # return objects
    tsp_header = {}  # the .tsp header dict to be returned by the function
    nodes = []       # the list of nodes to be parsed from node coord section

    problem = tsplib95.loaders.load(tsp_file)

    kw_dict = problem.as_keyword_dict()

    if not kw_dict['TYPE'] in  allowed_types:
        return None, None, "Not a TSP type problem"

    for k,v in kw_dict.items():
        if k == "NODES":
            break
        tsp_header[k] = v

    for k,v in kw_dict.items():


    # return the .tsp dict and node values
    return tsp_header, nodes


def export_tsp_file(tsp_file_path, tsp_header, nodes):
    """
    Export a .tsp file using tsp_header header elements and list of nodes. Nodes are parsed into "NODES_COORD_SECTION" format.

    :param tsp_file_path: the name of tsp file to be exported
    :type tsp_file_path: str
    :param tsp_header: a dictionary containing header values for the .tsp file
    :type tsp_header: dict
    :param nodes: a list containing nodes to be parsed into tsp file
    :type nodes: list
    """

    # try to execute the export
    try:

        # create tsp file to write data
        with open(tsp_file_path, "w+") as f:

            # loop through each header value and write it to file
            for k, v in tsp_header.items():
                f.write(f"{k} : {v}\n")

            # write the node section
            f.write("NODE_COORD_SECTION\n")

            # loop through each node and write its values to file
            for i, node in enumerate(nodes):
                if type(node) == Node2D:
                    f.write(f"{i} {node.x} {node.y}\n")
                elif type(node) == Node3D:
                    f.write(f"{i} {node.x} {node.y} {node.z}\n")

            # write end of file line
            f.write("EOF\n")

    # print error to user
    except Exception as e:
        logger.error(f"Error during export of .tsp file: '{e}'")
