#Gas Station

class Solution:
    def startStation(self, gas, cost):
        total_gas = 0  # Total gas available for the whole trip
        current_gas = 0  # Gas available while traveling from the current start
        start_index = 0  # The candidate index for starting the journey
        
        for i in range(len(gas)):
            total_gas += gas[i] - cost[i]  # Calculate net gas at each station
            current_gas += gas[i] - cost[i]  # Calculate the current gas as we move forward
            
            if current_gas < 0:  # If we can't make it to the next station, reset the start
                start_index = i + 1  # Move the start point to the next station
                current_gas = 0  # Reset current gas since we are starting over
        
        # After one full loop, if total gas is >= 0, the start_index is valid
        return start_index if total_gas >= 0 else -1


def main():
    # Ask the user if they want to use user input or inbuilt examples
    choice = input("Do you want to input gas and cost arrays? (yes/no): ").strip().lower()
    
    if choice == 'yes':
        # Get user input for gas and cost arrays
        gas = list(map(int, input("Enter the gas array (space-separated): ").split()))
        cost = list(map(int, input("Enter the cost array (space-separated): ").split()))
        
        # Create an instance of the Solution class
        solution = Solution()
        
        # Call the startStation function
        result = solution.startStation(gas, cost)
        
        # Print the result
        print(f"Start index: {result}")
    
    else:
        # Inbuilt examples to test the function
        print("\nRunning inbuilt examples...")

        # Example 1
        gas1 = [4, 5, 7, 4]
        cost1 = [6, 6, 3, 5]
        solution = Solution()
        result1 = solution.startStation(gas1, cost1)
        print(f"Example 1: Start index: {result1}")  # Expected output: 2

        # Example 2
        gas2 = [1, 2, 3, 4, 5]
        cost2 = [3, 4, 5, 1, 2]
        result2 = solution.startStation(gas2, cost2)
        print(f"Example 2: Start index: {result2}")  # Expected output: 3

        # Example 3
        gas3 = [3, 9]
        cost3 = [7, 6]
        result3 = solution.startStation(gas3, cost3)
        print(f"Example 3: Start index: {result3}")  # Expected output: -1


# Run the main function
if __name__ == "__main__":
    main()
