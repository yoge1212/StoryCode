from webscraper import Webscraper

class ProblemTracker:
    def __init__(self,userName):
        
        self.user_completed_problems = Webscraper.createArray(userName)
        self.tier_problems = {
    1: ["Contains Duplicate", "Valid Anagram", "Two Sum", "Group Anagrams", "Top K Frequent Elements", "Product of Array Except Self", "Valid Sudoku", "Encode and Decode Strings", "Longest Consecutive Sequence"],
    
    2: ["Valid Palindrome", "Two Sum II Input Array Is Sorted", "3Sum", "Container With Most Water", "Trapping Rain Water"],
    
    3: ["Best Time to Buy And Sell Stock", "Longest Substring Without Repeating Characters", "Longest Repeating Character Replacement", "Permutation In String", "Minimum Window Substring", "Sliding Window Maximum"],
    
    4: ["Valid Parentheses", "Min Stack", "Evaluate Reverse Polish Notation", "Generate Parentheses", "Daily Temperatures", "Car Fleet", "Largest Rectangle In Histogram"],
    
    5: ["Binary Search", "Search a 2D Matrix", "Koko Eating Bananas", "Find Minimum In Rotated Sorted Array", "Search In Rotated Sorted Array", "Time Based Key Value Store", "Median of Two Sorted Arrays"],
    
    6: ["Reverse Linked List", "Merge Two Sorted Lists", "Reorder List", "Remove Nth Node From End of List", "Copy List With Random Pointer", "Add Two Numbers", "Linked List Cycle", "Find The Duplicate Number", "LRU Cache", "Merge K Sorted Lists", "Reverse Nodes In K Group"],
    
    7: ["Invert Binary Tree", "Maximum Depth of Binary Tree", "Diameter of Binary Tree", "Balanced Binary Tree", "Same Tree", "Subtree of Another Tree", "Lowest Common Ancestor of a Binary Search Tree", "Binary Tree Level Order Traversal", "Binary Tree Right Side View", "Count Good Nodes In Binary Tree", "Validate Binary Search Tree", "Kth Smallest Element In a Bst", "Construct Binary Tree From Preorder And Inorder Traversal", "Binary Tree Maximum Path Sum", "Serialize And Deserialize Binary Tree"],
    
    8: ["Implement Trie Prefix Tree", "Design Add And Search Words Data Structure", "Word Search II"],
    
    9: ["Kth Largest Element In a Stream", "Last Stone Weight", "K Closest Points to Origin", "Kth Largest Element In An Array", "Task Scheduler", "Design Twitter", "Find Median From Data Stream"],
    
    10: ["Subsets", "Combination Sum", "Permutations", "Subsets II", "Combination Sum II", "Word Search", "Palindrome Partitioning", "Letter Combinations of a Phone Number", "N Queens"],
    
    11: ["Number of Islands", "Clone Graph", "Max Area of Island", "Pacific Atlantic Water Flow", "Surrounded Regions", "Rotting Oranges", "Walls And Gates", "Course Schedule", "Course Schedule II", "Redundant Connection", "Number of Connected Components In An Undirected Graph", "Graph Valid Tree", "Word Ladder"],
    
    12: ["Reconstruct Itinerary", "Min Cost to Connect All Points", "Network Delay Time", "Swim In Rising Water", "Alien Dictionary", "Cheapest Flights Within K Stops"],
    
    13: ["Climbing Stairs", "Min Cost Climbing Stairs", "House Robber", "House Robber II", "Longest Palindromic Substring", "Palindromic Substrings", "Decode Ways", "Coin Change", "Maximum Product Subarray", "Word Break", "Longest Increasing Subsequence", "Partition Equal Subset Sum"],
    
    14: ["Unique Paths", "Longest Common Subsequence", "Best Time to Buy And Sell Stock With Cooldown", "Coin Change II", "Target Sum", "Interleaving String", "Longest Increasing Path In a Matrix", "Distinct Subsequences", "Edit Distance", "Burst Balloons", "Regular Expression Matching"],
    
    15: ["Maximum Subarray", "Jump Game", "Jump Game II", "Gas Station", "Hand of Straights", "Merge Triplets to Form Target Triplet", "Partition Labels", "Valid Parenthesis String"],
    
    16: ["Insert Interval", "Merge Intervals", "Non Overlapping Intervals", "Meeting Rooms", "Meeting Rooms II", "Minimum Interval to Include Each Query"],
    
    17: ["Rotate Image", "Spiral Matrix", "Set Matrix Zeroes", "Happy Number", "Plus One", "Pow(x, n)", "Multiply Strings", "Detect Squares"],
    
    18: ["Single Number", "Number of 1 Bits", "Counting Bits", "Reverse Bits", "Missing Number", "Sum of Two Integers"]
    }

        self.problems = {
        "Arrays & Hashing": [
        {"name": "Contains Duplicate", "difficulty": "Easy"},
        {"name": "Valid Anagram", "difficulty": "Easy"},
        {"name": "Two Sum", "difficulty": "Easy"},
        {"name": "Group Anagrams", "difficulty": "Medium"},
        {"name": "Top K Frequent Elements", "difficulty": "Medium"},
        {"name": "Product of Array Except Self", "difficulty": "Medium"},
        {"name": "Valid Sudoku", "difficulty": "Medium"},
        {"name": "Encode and Decode Strings", "difficulty": "Medium"},
        {"name": "Longest Consecutive Sequence", "difficulty": "Medium"}
    ],
    "Two Pointers": [
        {"name": "Valid Palindrome", "difficulty": "Easy"},
        {"name": "Two Sum II - Input Array Is Sorted", "difficulty": "Medium"},
        {"name": "3Sum", "difficulty": "Medium"},
        {"name": "Container With Most Water", "difficulty": "Medium"},
        {"name": "Trapping Rain Water", "difficulty": "Hard"}
    ],
    "Sliding Window": [
        {"name": "Best Time to Buy And Sell Stock", "difficulty": "Easy"},
        {"name": "Longest Substring Without Repeating Characters", "difficulty": "Medium"},
        {"name": "Longest Repeating Character Replacement", "difficulty": "Medium"},
        {"name": "Permutation In String", "difficulty": "Medium"},
        {"name": "Minimum Window Substring", "difficulty": "Hard"},
        {"name": "Sliding Window Maximum", "difficulty": "Hard"}
    ],
    "Stack": [
        {"name": "Valid Parentheses", "difficulty": "Easy"},
        {"name": "Min Stack", "difficulty": "Medium"},
        {"name": "Evaluate Reverse Polish Notation", "difficulty": "Medium"},
        {"name": "Generate Parentheses", "difficulty": "Medium"},
        {"name": "Daily Temperatures", "difficulty": "Medium"},
        {"name": "Car Fleet", "difficulty": "Medium"},
        {"name": "Largest Rectangle in Histogram", "difficulty": "Hard"}
    ],
    "Binary Search": [
        {"name": "Binary Search", "difficulty": "Easy"},
        {"name": "Search a 2D Matrix", "difficulty": "Medium"},
        {"name": "Koko Eating Bananas", "difficulty": "Medium"},
        {"name": "Find Minimum in Rotated Sorted Array", "difficulty": "Medium"},
        {"name": "Search in Rotated Sorted Array", "difficulty": "Medium"},
        {"name": "Time Based Key Value Store", "difficulty": "Medium"},
        {"name": "Median of Two Sorted Arrays", "difficulty": "Hard"}
    ],
    "Linked List": [
        {"name": "Reverse Linked List", "difficulty": "Easy"},
        {"name": "Merge Two Sorted Lists", "difficulty": "Easy"},
        {"name": "Reorder List", "difficulty": "Medium"},
        {"name": "Remove Nth Node From End of List", "difficulty": "Medium"},
        {"name": "Copy List with Random Pointer", "difficulty": "Medium"},
        {"name": "Add Two Numbers", "difficulty": "Medium"},
        {"name": "Linked List Cycle", "difficulty": "Easy"},
        {"name": "Find the Duplicate Number", "difficulty": "Medium"},
        {"name": "LRU Cache", "difficulty": "Medium"},
        {"name": "Merge k Sorted Lists", "difficulty": "Hard"},
        {"name": "Reverse Nodes in k-Group", "difficulty": "Hard"}
    ],
    "Trees": [
        {"name": "Invert Binary Tree", "difficulty": "Easy"},
        {"name": "Maximum Depth of Binary Tree", "difficulty": "Easy"},
        {"name": "Diameter of Binary Tree", "difficulty": "Easy"},
        {"name": "Balanced Binary Tree", "difficulty": "Easy"},
        {"name": "Same Tree", "difficulty": "Easy"},
        {"name": "Subtree of Another Tree", "difficulty": "Easy"},
        {"name": "Lowest Common Ancestor of a Binary Search Tree", "difficulty": "Medium"},
        {"name": "Binary Tree Level Order Traversal", "difficulty": "Medium"},
        {"name": "Binary Tree Right Side View", "difficulty": "Medium"},
        {"name": "Count Good Nodes in Binary Tree", "difficulty": "Medium"},
        {"name": "Validate Binary Search Tree", "difficulty": "Medium"},
        {"name": "Kth Smallest Element in a BST", "difficulty": "Medium"},
        {"name": "Construct Binary Tree from Preorder and Inorder Traversal", "difficulty": "Medium"},
        {"name": "Binary Tree Maximum Path Sum", "difficulty": "Hard"},
        {"name": "Serialize and Deserialize Binary Tree", "difficulty": "Hard"}
    ],"Tries": [
      {"name": "Implement Trie (Prefix Tree)", "difficulty": "Medium"},
      {"name": "Design Add and Search Words Data Structure", "difficulty": "Medium"},
      {"name": "Word Search II", "difficulty": "Hard"}
  ],
  "Heap / Priority Queue": [
      {"name": "Kth Largest Element in a Stream", "difficulty": "Easy"},
      {"name": "Last Stone Weight", "difficulty": "Easy"},
      {"name": "K Closest Points to Origin", "difficulty": "Medium"},
      {"name": "Kth Largest Element in an Array", "difficulty": "Medium"},
      {"name": "Task Scheduler", "difficulty": "Medium"},
      {"name": "Design Twitter", "difficulty": "Medium"},
      {"name": "Find Median from Data Stream", "difficulty": "Hard"}
  ],
  "Backtracking": [
      {"name": "Subsets", "difficulty": "Medium"},
      {"name": "Combination Sum", "difficulty": "Medium"},
      {"name": "Permutations", "difficulty": "Medium"},
      {"name": "Subsets II", "difficulty": "Medium"},
      {"name": "Combination Sum II", "difficulty": "Medium"},
      {"name": "Word Search", "difficulty": "Medium"},
      {"name": "Palindrome Partitioning", "difficulty": "Medium"},
      {"name": "Letter Combinations of a Phone Number", "difficulty": "Medium"},
      {"name": "N-Queens", "difficulty": "Hard"}
  ],
  "Graphs": [
      {"name": "Number of Islands", "difficulty": "Medium"},
      {"name": "Clone Graph", "difficulty": "Medium"},
      {"name": "Max Area of Island", "difficulty": "Medium"},
      {"name": "Pacific Atlantic Water Flow", "difficulty": "Medium"},
      {"name": "Surrounded Regions", "difficulty": "Medium"},
      {"name": "Rotting Oranges", "difficulty": "Medium"},
      {"name": "Walls and Gates", "difficulty": "Medium"},
      {"name": "Course Schedule", "difficulty": "Medium"},
      {"name": "Course Schedule II", "difficulty": "Medium"},
      {"name": "Redundant Connection", "difficulty": "Medium"},
      {"name": "Number of Connected Components in an Undirected Graph", "difficulty": "Medium"},
      {"name": "Graph Valid Tree", "difficulty": "Medium"},
      {"name": "Word Ladder", "difficulty": "Hard"}
  ],
  "Advanced Graphs": [
      {"name": "Reconstruct Itinerary", "difficulty": "Hard"},
      {"name": "Min Cost to Connect All Points", "difficulty": "Medium"},
      {"name": "Network Delay Time", "difficulty": "Medium"},
      {"name": "Swim in Rising Water", "difficulty": "Hard"},
      {"name": "Alien Dictionary", "difficulty": "Hard"},
      {"name": "Cheapest Flights Within K Stops", "difficulty": "Medium"}
  ],
  "1-D Dynamic Programming": [
      {"name": "Climbing Stairs", "difficulty": "Easy"},
      {"name": "Min Cost Climbing Stairs", "difficulty": "Easy"},
      {"name": "House Robber", "difficulty": "Medium"},
      {"name": "House Robber II", "difficulty": "Medium"},
      {"name": "Longest Palindromic Substring", "difficulty": "Medium"},
      {"name": "Palindromic Substrings", "difficulty": "Medium"},
      {"name": "Decode Ways", "difficulty": "Medium"},
      {"name": "Coin Change", "difficulty": "Medium"},
      {"name": "Maximum Product Subarray", "difficulty": "Medium"},
      {"name": "Word Break", "difficulty": "Medium"},
      {"name": "Longest Increasing Subsequence", "difficulty": "Medium"},
      {"name": "Partition Equal Subset Sum", "difficulty": "Medium"}
  ],
  "2-D Dynamic Programming": [
      {"name": "Unique Paths", "difficulty": "Medium"},
      {"name": "Longest Common Subsequence", "difficulty": "Medium"},
      {"name": "Best Time to Buy and Sell Stock with Cooldown", "difficulty": "Medium"},
      {"name": "Coin Change 2", "difficulty": "Medium"},
      {"name": "Target Sum", "difficulty": "Medium"},
      {"name": "Interleaving String", "difficulty": "Medium"},
      {"name": "Longest Increasing Path in a Matrix", "difficulty": "Hard"},
      {"name": "Distinct Subsequences", "difficulty": "Hard"},
      {"name": "Edit Distance", "difficulty": "Medium"},
      {"name": "Burst Balloons", "difficulty": "Hard"},
      {"name": "Regular Expression Matching", "difficulty": "Hard"}
  ],
  "Greedy": [
      {"name": "Maximum Subarray", "difficulty": "Medium"},
      {"name": "Jump Game", "difficulty": "Medium"},
      {"name": "Jump Game II", "difficulty": "Medium"},
      {"name": "Gas Station", "difficulty": "Medium"},
      {"name": "Hand of Straights", "difficulty": "Medium"},
      {"name": "Merge Triplets to Form Target Triplet", "difficulty": "Medium"},
      {"name": "Partition Labels", "difficulty": "Medium"},
      {"name": "Valid Parenthesis String", "difficulty": "Medium"}
  ],
  "Intervals": [
      {"name": "Insert Interval", "difficulty": "Medium"},
      {"name": "Merge Intervals", "difficulty": "Medium"},
      {"name": "Non-overlapping Intervals", "difficulty": "Medium"},
      {"name": "Meeting Rooms", "difficulty": "Easy"},
      {"name": "Meeting Rooms II", "difficulty": "Medium"},
      {"name": "Minimum Interval to Include Each Query", "difficulty": "Hard"}
  ],
  "Math & Geometry": [
      {"name": "Rotate Image", "difficulty": "Medium"},
      {"name": "Spiral Matrix", "difficulty": "Medium"},
      {"name": "Set Matrix Zeroes", "difficulty": "Medium"},
      {"name": "Happy Number", "difficulty": "Easy"},
      {"name": "Plus One", "difficulty": "Easy"},
      {"name": "Pow(x, n)", "difficulty": "Medium"},
      {"name": "Multiply Strings", "difficulty": "Medium"},
      {"name": "Detect Squares", "difficulty": "Medium"}
  ],
  "Bit Manipulation": [
      {"name": "Single Number", "difficulty": "Easy"},
      {"name": "Number of 1 Bits", "difficulty": "Easy"},
      {"name": "Counting Bits", "difficulty": "Easy"},
      {"name": "Reverse Bits", "difficulty": "Easy"},
      {"name": "Missing Number", "difficulty": "Easy"},
      {"name": "Sum of Two Integers", "difficulty": "Medium"},
      {"name": "Reverse Integer", "difficulty": "Medium"}
  ]
}


    def get_user_score(self, user_problems):
        user_score = 0
        for problem in user_problems:
            for tier, tier_problems_list in self.tier_problems.items():
                if problem.returnName() in tier_problems_list:
                    user_score = tier * 10
                    break 
        return user_score

    def get_user_tier(self, user_problems):
        greatest_tier = 0  # Initialized with the lowest tier
        tier_end = False

        for tier, tier_problems_list in self.tier_problems.items():
            if set(tier_problems_list).issubset(set(user_problems)):
                greatest_tier = max(greatest_tier, tier)
                tier_end = True
            elif tier_end:
                return greatest_tier

        return greatest_tier

    def calculate_user_tier(self):
        
        newlist = [x.returnName() for x in self.user_completed_problems]

        user_tier = self.get_user_tier(newlist)

        return user_tier
    
    def calculate_user_score(self):
        user_score = self.get_user_score(self.user_completed_problems)

        return user_score
    
    def getArray(self):
        return self.user_completed_problems
    
    def returnDic(self):
        return self.tier_problems
    
    def returndifficulty(self):
        total_solved = self.user_completed_problems[0].returnSolved()
        easy_threshold = 100
        medium_threshold = 300

        if total_solved < easy_threshold:
            return "beginner"
        elif total_solved < medium_threshold:
            return "intermediate"
        else:
            return "advanced"
    
    def suggest_problems(self, i, user_category):
        beginner_problems = self.problems["Arrays & Hashing"] + self.problems["Two Pointers"] + self.problems["Sliding Window"]
        intermediate_problems = self.problems["Stack"] + self.problems["Binary Search"] + self.problems["Linked List"]
        advanced_problems = self.problems["Trees"] + self.problems["Tries"] + self.problems["Heap / Priority Queue"]

        
        if user_category == "beginner":
            beginner_problems = self.problems.get("Beginner", [])  # Replace "Beginner" with the correct category name

            if user_category == "beginner":
                problem_links = ""
                if i == 0:
                    problem_name = beginner_problems[2]
                    print(problem_name)
                    problem_link = f"https://leetcode.com/problems/{problem_name.lower().replace(' ', '-')}/description"
                    problem_links += f"[{problem_name}]({problem_link})\n"
                    return problem_links
                else:
                    print(f"Index {i} is out of bounds for beginner_problems.")

            
        elif user_category == "intermediate":
            problem_links = ""
            problem_name= intermediate_problems[i]
            problem_link = f"https://leetcode.com/problems/{problem_name.lower().replace(' ', "-")}/description"
            problem_links += f"[{problem_name}]({problem_link})\n"
            return problem_links
        else:
            problem_links = ""
            problem_name= advanced_problems[i]
            problem_link = f"https://leetcode.com/problems/{problem_name.lower().replace(' ', "-")}/description"
            problem_links += f"[{problem_name}]({problem_link})\n"
            return problem_links
            
        
        
        


# Usage

#user_tier = ProblemTracker.calculate_user_tier()
#user_score = ProblemTracker.calculate_user_score()

#print(f"Your tier is: {user_tier}")
#print(f"Your score is: {user_score}")
