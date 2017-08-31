import Queue

class DirectedGraph(object):
    """
    Directed Graph, with graph represented as an adjacency list
    """

    def __init__(self):
        self.adjacency_list = {}

    def add_edge(self, source, destination):
        """
        Adds an edge defined by vertices source and destination
        """
        if source not in self.adjacency_list:
            self.adjacency_list[source] = set()
        self.adjacency_list[source].add(destination)

    def get_vertex(self):
        """
        Generator for returning the next vertex from the adjacency list
        """
        for v in self.adjacency_list:
            yield v

    def get_neighbor(self, vertex):
        """
        Generator for returning the next vertex adjacent to the given vertex
        """
        if vertex in self.adjacency_list:
            for u in self.adjacency_list[vertex]:
                yield u

    def get_reverse_neighbor(self, vertex):
        """
        Generator for returning the reversed edge neighbor to the given vertex (parent)
        """
        reversed_list = {}
        for v, u in self.adjacency_list.items():
            for w in u:
                if w not in reversed_list:
                    reversed_list[w] = set()
                reversed_list[w].add(v)

        if vertex in reversed_list:
            for u in reversed_list[vertex]:
                yield u


    def bfs(self):
        """
        Computes the the parents for each vertex as determined through breadth-first search
        """
        parents = {}
        to_visit = Queue.Queue()

        for vertex in self.get_vertex():
            to_visit.put(vertex)

            while not to_visit.empty():
                v = to_visit.get()

                for neighbor in self.get_neighbor(v):
                    if neighbor not in parents:
                        parents[neighbor] = v
                        to_visit.put(neighbor)

        return parents

    def dfs(self):
        """
        Computes the initial source vertices for each connected component
        and the parents for each vertex as determined through depth-first-search
        """
        parents = {}
        components = set()
        to_visit = []

        for vertex in self.get_vertex():
            if vertex not in parents:
                components.add(vertex)
            else:
                continue

            to_visit.append(vertex)

            while to_visit:
                v = to_visit.pop()

                for neighbor in self.get_neighbor(v):
                    if neighbor not in parents:
                        parents[neighbor] = v
                        to_visit.append(neighbor)

        return components, parents

    def contains_cycle(self):
        """
        Determines if one of the connected components contains a cycle
        """
        contains_cycle = False
        STATUS_STARTED = 1
        STATUS_FINISHED = 2

        for vertex in self.get_vertex():
            statuses = {}
            to_visit = [vertex]

            while to_visit and not contains_cycle:
                v = to_visit.pop()

                if v in statuses:
                    if statuses[v] == STATUS_STARTED:
                        statuses[v] = STATUS_FINISHED
                else:
                    statuses[v] = STATUS_STARTED
                    to_visit.append(v)  # add to stack again to signal vertex has finished DFS

                for u in self.get_neighbor(v):
                    if u in statuses:
                        if statuses[u] == STATUS_STARTED:
                            contains_cycle = True
                            break
                    else:
                        to_visit.append(u)

                if contains_cycle:
                    break

        return contains_cycle

    def topological_sort(self):
        """
        Determines the priority of vertices to be visited.
        """
        STATUS_STARTED = 1
        STATUS_FINISHED = 2
        order = []
        statuses = {}

        assert (not self.contains_cycle())

        for vertex in self.get_vertex():
            to_visit = [vertex]

            while to_visit:
                v = to_visit.pop()

                if v in statuses:
                    if statuses[v] == STATUS_STARTED:
                        statuses[v] = STATUS_FINISHED
                        order.append(v)
                else:
                    statuses[v] = STATUS_STARTED
                    to_visit.append(v)  # add to stack again to signal vertex has finished DFS

                for u in self.get_neighbor(v):
                    if u not in statuses:
                        to_visit.append(u)

        order.reverse()

        return order

    def strongly_connected_components(self):
        """
        Compute the vertices in the strongly connected components
        """
        stack = self.scc_dfs_forward_pass()
        components = self.scc_dfs_reverse_pass(stack)

        return components

    def scc_dfs_forward_pass(self):
        stack = []
        visited = set()

        for v in self.get_vertex():
            self.dfs_forward(v, stack, visited)

        return stack

    def dfs_forward(self, vertex, stack, visited):
        if vertex not in visited:
            visited.add(vertex)
            for u in self.get_neighbor(vertex):
                self.dfs_forward(u, stack, visited)
            stack.append(vertex)

    def scc_dfs_reverse_pass(self, stack):
        components = []
        visited = set()

        while stack:
            v = stack.pop()
            if v not in visited:
                component = []
                self.dfs_reverse(v, component, visited)
                component.reverse()
                components.append(component)

        return components

    def dfs_reverse(self, vertex, component, visited):
        if vertex not in visited:
            visited.add(vertex)
            component.append(vertex)
            for u in self.get_reverse_neighbor(vertex):
                self.dfs_reverse(u, component, visited)
