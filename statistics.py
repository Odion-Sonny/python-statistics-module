class statistics:
    def __init__(self,x) -> None:
        self.x = x
        pass
    
    # count method
    def count(self):
        counter = 0
        for i in self.x:
            counter += 1
        return counter

    # sum method
    def sum(self):
        adder = 0
        for i in self.x:
            adder += i
        return adder

    # min method
    def min(self):
        smallest_num = self.x[0]
        for i in self.x:
            if i < smallest_num:
                smallest_num = i
        return smallest_num

    # max method
    def max(self):
        highest_num = self.x[0]
        for i in self.x:
            if i > highest_num:
                highest_num = i
        return highest_num

    # range method
    def range(self):
        highest_num = self.x[0]
        for i in self.x:
            if i > highest_num:
                highest_num = i

        lowest_num = self.x[0]
        for i in self.x:
            if i < lowest_num:
                lowest_num = i
        
        return highest_num - lowest_num

    # mean method
    def mean(self):
        add=0
        for i in self.x:
            add += i
        return -(add // -len(self.x))

    # median method
    def median(self):
        self.x.sort()

        if len(self.x) % 2 == 0:
            median1 = self.x[len(self.x)//2]
            median2 = self.x[len(self.x)//2 - 1]
            median = (median1 + median2)/2
            return median
        else:
            median = self.x[len(self.x)//2]
            return median

    # mode method
    def mode(self):
        self.x.sort()
        counter = []
        i=0
        while i < len(self.x):
            counter.append(self.x.count(self.x[i]))
            i += 1
        
        d = dict(zip(self.x,counter))
        # key=[]
        # value=[]
        res = []
        for k,v in d.items():
            if v == max(counter):
                res.append({'mode':k, 'count':v})   
            #     key=k
            #     value=v
            # res={'mode':key, 'count':value}
        return res


    # standard deviation method
    def std(self):
        l = len(self.x)
        mean = sum(self.x) / l
        variance = sum((x - mean) ** 2 for x in self.x) / l
        std = variance ** 0.5
        return std


    # variance method
    def var(self):
        l = len(self.x)
        mean = sum(self.x) / l
        variance = sum((x - mean) ** 2 for x in self.x) / l
        return variance
