class Statistics:
    def __init__(self):
        self.data = []

    def get_numbers(self):
        self.data.clear()
        while True:
            try:
                nums = input("Enter numbers separated by spaces or 'q' to quit: ").strip()
                if nums.lower() == 'q':
                    break
                self.data.extend([float(num) for num in nums.split()])
            except ValueError:
                print("Invalid input! Please enter numbers separated by spaces.")
                
                
    
    def view_numbers(self):
        if not self.data:
            print("List is empty! Please add numbers.")
        else:
            print(f"Numbers: {self.data}")            
    
    def view_sorted_numbers(self):
        if not self.data:
            print("List is empty! Please add numbers.")
        else:
            print(f"Sorted Numbers: {sorted(self.data)}")
            
    def find_min(self):
        if not self.data:
            print("List is empty! Please add numbers.")
            return None
        else:
            min_num = self.data[0]
            for num in self.data:
                if num < min_num:
                    min_num = num
            return min_num

    def find_max(self):
        if not self.data:
            print("List is empty! Please add numbers.")
            return None
        else:
            max_num = self.data[0]
            for num in self.data:
                if num > max_num:
                    max_num = num
            return max_num

    def find_mean(self):
        if not self.data:
            print("List is empty! Please add numbers.")
        else:
            sum_num = 0
            for num in self.data:
                sum_num += num
            mean = sum_num / len(self.data)
            return mean

    def find_mode(self):
        if not self.data:
            print("List is empty! Please add numbers.")
        else:
            freq = {}
            for num in self.data:
                if num in freq:
                    freq[num] += 1
                else:
                    freq[num] = 1
            max_freq = list(freq.values())[0]
            for count in freq.values():
                if count > max_freq:
                    max_freq = count
            modes = []
            for num, count in freq.items():
                if count == max_freq:
                    modes.append(num)
            return modes

    def find_median(self):
        if not self.data:
            print("List is empty! Please add numbers.")
        else:
            sorted_data = sorted(self.data)
            n = len(sorted_data)
            if n % 2 == 0:
                median = (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2
            else:
                median = sorted_data[n // 2]
            return median

    def find_range(self):
        if not self.data:
            print("List is empty! Please add numbers.")
        else:
            range_value = self.find_max() - self.find_min()
            return range_value

    def find_variance(self):
        if not self.data:
            print("List is empty! Please add numbers.")
        else:
            mean = self.find_mean()
            sum_squares = 0
            for num in self.data:
                sum_squares += (num - mean) ** 2
            variance = sum_squares / (len(self.data)-1)
            return variance

    def find_STD(self):
        if not self.data:
            print("List is empty! Please add numbers.")
        else:
            variance = self.find_variance()
            STD = variance ** 0.5
            return STD

    def find_Quariles(self):
        if not self.data:
            print("List is empty! Please add numbers.")
        else:
            sorted_data = sorted(self.data)
            n = len(sorted_data)
            Q1 = sorted_data[n // 4]
            Q2 = sorted_data[n // 2]
            Q3 = sorted_data[3 * n // 4]
            return Q1, Q2, Q3

    def find_IQR(self):
        if not self.data:
            print("List is empty! Please add numbers.")
        else:
            sorted_data = sorted(self.data)
            n = len(sorted_data)
            Q1 = sorted_data[n // 4]
            Q3 = sorted_data[3 * n // 4]
            IQR = Q3 - Q1
            return IQR

    def summary_statistics(self):
        if not self.data:
            print("List is empty! Please add numbers.")
        else:
            print(f"Summary Statistics:")
            print(f"Min: {self.find_min()}")
            print(f"Max: {self.find_max()}")
            print(f"Mean: {self.find_mean()}")
            print(f"Mode: {self.find_mode()}")
            print(f"Median: {self.find_median()}")
            print(f"Range: {self.find_range()}")
            print(f"Variance: {self.find_variance()}")
            print(f"Standard Deviation: {self.find_STD()}")
            print(f"Quartiles: {self.find_Quariles()}")
            print(f"IQR: {self.find_IQR()}")