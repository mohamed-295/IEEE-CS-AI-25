class Solution(object):
    def sampleStats(self, count):
        min_val=-1
        max_val=-1

        for i in range(256):
            if count[i] > 0:
                min_val = i
                break

        for i in range(255, -1, -1):
            if count[i] > 0:
                max_val = i
                break

        total_sum = sum(i * count[i] for i in range(256))
        total_count = float(sum(count))
        mean = round(total_sum / total_count, 5)

        median_pos = total_count // 2
        if total_count % 2 == 0:
            m1 = m2 = None
            curr = 0
            for i in range(256):
                curr += count[i]
                if m1 is None and curr > median_pos - 1:
                    m1 = i
                if m2 is None and curr > median_pos:
                    m2 = i
                    break
            median = (m1 + m2) / 2.0
        else:
            curr = 0
            for i in range(256):
                curr += count[i]
                if curr > median_pos:
                    median = i
                    break

        mode = count.index(max(count))

        return [float(min_val), float(max_val), mean, median, float(mode)]
