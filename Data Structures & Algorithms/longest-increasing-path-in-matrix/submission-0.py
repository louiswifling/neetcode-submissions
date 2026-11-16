from collections import deque

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        

        n = len(matrix)
        m = len(matrix[0])




        edge_map = [(0, 1), (0, -1), (-1, 0), (1, 0)]

        def incident_edges(pair): 
            i = pair[0]
            j = pair[1] 
            edges = []
            for k in range(4): 
                e = edge_map[k]
                new_i = i + e[0]
                new_j = j + e[1]
                if 0 <= new_i < n and 0 <= new_j < m: 
                    if matrix[new_i][new_j] > matrix[i][j]: 
                        edges.append(k)

            return edges 



        def add_edge(vertex, edge_number): 
            edge = edge_map[edge_number]
            return (vertex[0] + edge[0], vertex[1] + edge[1])



        finished = [[False] * m for _ in range(n)]
        max_length_from_here = [[0] * m for _ in range(n)]
        result = 0

        for i in range(n): 
            for j in range(m): 
                # Start DFS

                if finished[i][j]: 
                    continue


                q = deque()
                q.append(((i, j), -1))

                while q: 
                    current, edge_taken_last_time = q[-1]

                    # Check whether we need to go back one step 
                    found_unfinished = False
                    for e in incident_edges(current): 
                        if e <= edge_taken_last_time: 
                            continue
                        
                        v = add_edge(current, e)
                        if not finished[v[0]][v[1]]: 
                            q.append((v, -1))
                            found_unfinished = True
                            break
                    
                    if not found_unfinished: 
                        l = 0
                        for e in incident_edges(current): 
                            v = add_edge(current, e)
                            l = max(l, max_length_from_here[v[0]][v[1]])
                        
                        max_length_from_here[current[0]][current[1]] = l + 1
                        result = max(
                            l + 1, 
                            result
                        )

                        finished[current[0]][current[1]] = True

                        q.pop()

                        

        return result






