class Statistics:
    def __init__(self, data : list):
        self.data = data
    
    def mean(self):
        a = 0
        for i in self.data:
            a += i
        return a/len(self.data) if len(self.data) != 0 else None
    
    def median(self):
        if len(self.data) % 2 != 0:
            return self.data[len(self.data)//2]
        elif len(self.data) % 2 == 0:
            return (self.data[len(self.data)//2] + self.data[(len(self.data)//2) - 1])/2
        return None
    def mode(self):
        items = set(self.data)
        converted_chart = [(self.data.count(i), i) for i in items]
        sorted_chart = sorted(converted_chart, key = lambda x:x[0], reverse=True)
        final_list = [{"mode": i[1], "count" : i[0]} for i in sorted_chart if i[0] == sorted_chart[0][0]]
        return final_list 
    
    def range_(self):
        return self.data[-1] - self.data[0]
    
    def variance(self):
        t = len(self.data)
        mean_ = self.mean()
        new_list = [(i - mean_)**2 for i in self.data]
        v = 1/t * sum(new_list)
        return v
    
    def standard_deviation(self):
        return self.variance()**0.5
    
    def min_(self):
        return min(self.data)    
    
    def max_(self):
        return max(self.data)
    
    def count(self):
        return len(self.data)
    
    def frequency_distribution(self):
        items = set(self.data)
        converted_chart = [(self.data.count(i) / len(self.data) * 100, i) for i in items]
        sorted_chart = sorted(converted_chart, key = lambda x:x[0], reverse=True)
        return sorted_chart


    def describe(self):
        message = (
        f"Count: {self.count()}\n"
        f"Sum: {sum(self.data)}\n"
        f"Min: {self.min_()}\n"
        f"Max: {self.max_()}\n"
        f"Range: {self.range_()}\n"
        f"Mean: {round(self.mean(), 1)}\n"
        f"Median: {self.median()}\n"
        f"Mode: {self.mode()}\n"
        f"Variance: {round(self.variance(), 1)}\n"
        f"Standard Deviation: {round(self.standard_deviation(), 1)}\n"
        f"Frequency Distribution: {self.frequency_distribution()}"
        )
        return message
    
ages =[31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]
my_statistics = Statistics(ages)
print(my_statistics.describe())