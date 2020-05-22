"""
Categorise the episodes of Naruto: Shippuden into
their respective arcs.
"""


from collections import OrderedDict


main_arcs = OrderedDict()
filler_arcs = OrderedDict()
all_arcs = OrderedDict()


def sort_arc_list(arc_file):
    """
    Takes in a file called `arcfile` and then sorts each line into arcs and
    their corresponding episode_numbers which are then piped into either
    `main_arcs` or `filler_arcs`, and `all_arcs`.

    Does not return anything, it instead modifies the dictionaries
    mentioned above.
    """
    with open(arc_file, 'r') as f:
        for line in f:
            current_arc = line.strip()

            if current_arc.count('/') == 2:
                # It is a filler arc

                title, ep_range = current_arc.split('/')[1:]
                # We get a list of the start and end points
                # of the episodes
                ep_range = list(map(int, ep_range.split('.')))

                start, end = ep_range[0], ep_range[1] + 1
                ep_range = list(range(start, end))

                filler_arcs[title] = ep_range
            else:
                # It is a canon arc

                # Of which there can be two types; those which are linear
                # i.e are continous and don't jump around, or get interrupted
                # by filler episodes, and those which are non-linear

                title, ep_range = current_arc.split('/')

                if ep_range.count('+'):
                    # It is a non linear arc

                    # Getting a 2D list of all the episodes in the arc
                    ep_range = ep_range.split('+')
                    for i in range(len(ep_range)):
                        ep_range[i] = ep_range[i].strip()
                        ep_range[i] = list(map(int, ep_range[i].split('.')))

                        start, end = ep_range[i][0], ep_range[i][1] + 1
                        ep_range[i] = list(range(start, end))

                    # Flattening the 2D list of episodes in the arc
                    temp = [ep for sub_eps in ep_range for ep in sub_eps]
                    ep_range = temp[::]
                else:
                    # It is a linear arc

                    ep_range = list(map(int, ep_range.split('.')))

                    start, end = ep_range[0], ep_range[1] + 1
                    ep_range = list(range(start, end))
                main_arcs[title] = ep_range
            all_arcs[title] = ep_range


if __name__ == '__main__':
    pass
