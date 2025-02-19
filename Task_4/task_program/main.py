import os
from statistics import Statistics


def showMenu():
    print("\n" + "="*50)
    print(" " * 15 + " Statistic Program ")
    print("="*50)
    print(" " * 10 + " 1. Add Numbers")
    print(" " * 10 + " 2. View Numbers")
    print(" " * 10 + " 3. View Sorted Numbers")
    print(" " * 10 + " 4. Find Min")
    print(" " * 10 + " 5. Find Max")
    print(" " * 10 + " 6. Find Mean")
    print(" " * 10 + " 7. Find Mode")
    print(" " * 10 + " 8. Find Median")
    print(" " * 10 + " 9. Find Range")
    print(" " * 10 + "10. Find Variance")
    print(" " * 10 + "11. Find Standard Deviation")
    print(" " * 10 + "12. Find Quartiles")
    print(" " * 10 + "13. Find IQR")
    print(" " * 10 + "14. Summary All Statistics")
    print(" " * 10 + "15. Exit")
    print("="*50)
    
def main():
    statistics = Statistics()
    try:
        while True:
            showMenu()
            choice = input("Enter your choice: ").strip()
            os.system('cls' if os.name == 'nt' else 'clear')
            match choice:
                case "1":
                    statistics.get_numbers()
                case "2":
                    statistics.view_numbers()
                case "3":
                    statistics.view_sorted_numbers()
                case "4":
                    print(f"Min: {statistics.find_min()}")
                case "5":
                    print(f"Max: {statistics.find_max()}")
                case "6":
                    print(f"Mean: {statistics.find_mean()}")
                case "7":
                    print(f"Mode: {statistics.find_mode()}")
                case "8":
                    print(f"Median: {statistics.find_median()}")
                case "9":
                    print(f"Range: {statistics.find_range()}")
                case "10":           
                    print(f"Variance: {float(statistics.find_variance()):.3f}") #not working to make it 3 decimals after floating 😓
                case "11":           
                    print(f"Standard Deviation: {float(statistics.find_STD()):.5f}") #not working also 😓
                case "12":           
                    print(f"Quartiles: {statistics.find_Quariles()}")
                case "13":           
                    print(f"IQR: {statistics.find_IQR()}")
                case "14":           
                    statistics.summary_statistics()
                case "15":   
                    print("\nExiting System.")
                    break
                case _:
                    print(" Invalid choice! Enter a number between 1-15.")
    except KeyboardInterrupt:
        print("\nExiting System.😘")

if __name__ == "__main__":
    main()