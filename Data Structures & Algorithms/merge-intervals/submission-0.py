class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        

        n_active_intervals = 0

        n = len(intervals)

        times = sorted([(I[0], "s") for I in intervals] + [(I[1], "e") for I in intervals], key = lambda x: (x[0], 0 if x[1] == "s" else 1))



        merged_intervals = []

        starting_time = -1

        for time in times: 
            if n_active_intervals == 0: 
                if time[1] == "s": 
                    starting_time = time[0]
                    n_active_intervals += 1
                if time[1] == "e": 
                    raise Exception("Can't happen!")
            
            else: 
                if time[1] == "s": 
                    n_active_intervals += 1
                if time[1] == "e": 
                    n_active_intervals -= 1
                
                if n_active_intervals == 0: 
                    merged_intervals.append((starting_time, time[0]))

        

        return merged_intervals
