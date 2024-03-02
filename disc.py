import discord
from discord.ext import commands
import requests
from points import pointSystem
from tierscore import ProblemTracker
import random
from webscraper import Webscraper


image_path = "./worldMap.jpg"
image_path2 = "./tier2.jpg"
image_path3 = "./portal.jpg"
user_id = ''
#problemtracker = ProblemTracker(userName)
leet_dict = {}
marketplace = {
    100: ['axe', 'bows', 'sword', 'dagger'],
    200: ['poison potion', 'health potion', 'strength potion'],
    300: ['chespiece', 'helmet', 'pants', 'boots'],
    1000: ['todoro']
}

# Define your intents
intents = discord.Intents.default()

# Enable specific intents based on your needs
intents.message_content = True
intents.guilds = True
# Add more intents as needed

bot = commands.Bot(command_prefix='!', intents=intents)



@bot.command(name='beginjourney')
async def beginjourney(ctx, leetcode_username):
    global user_id
    user_id = ctx.author.id
    # Store the LeetCode username in the dictionary
    leet_dict[user_id] = leetcode_username
    problemTracker = ProblemTracker(leetcode_username) 
    leetcode_score = problemTracker.calculate_user_score()
    leetcode_tier = problemTracker.calculate_user_tier()
    array = list()
    array.append(leetcode_username)
    array.append(leetcode_score)
    array.append(leetcode_tier)
    array.append(list())

    leet_dict[user_id] = array

    await ctx.send(f"LeetCode username set for {ctx.author.name}: {leetcode_username}")
    await ctx.send(f"Youre score is {leetcode_score}")
    await ctx.send(" In the mystical world of Algol, where coding is the language of power, an ancient order known as the Guild of Developers has maintained the balance between magic and technology. However, an evil force, the NullByte Sorcerer, has emerged, threatening to plunge Algol into chaos by corrupting the very fabric of code.\n\n As the chosen one, a skilled programmer, you embark on a heroic journey to restore order to Algol and defeat the NullByte Sorcerer. To do so, you must venture through the CodeQuest, a series of dungeons filled with coding challenges that test your programming skills and problem-solving abilities.")
    await ctx.send(file=discord.File(image_path))
    print(leet_dict)

    

@bot.command(name='checkXP')
async def checkXP(ctx):
    arr = leet_dict[user_id]
    await ctx.send(f"XP: {arr[1]}")

@bot.command(name='checkRank')
async def checkRank(ctx):
    arr = leet_dict[user_id]
    await ctx.send(f"Rank: {arr[2]}")


@bot.command(name='item')
async def item(ctx):
    array9 = leet_dict[user_id]
    array = array9[3]

    if leet_dict[user_id][1] >= 1000:
        array2 = marketplace[1000]
        array.append(array2[0])
    
    elif leet_dict[user_id][1] >= 300:
        array3 = marketplace[300]
        array.append(array3[random.randint(0,len(array3[2]))])
        

    
    elif leet_dict[user_id][1] >= 200:
        array4 = marketplace[200]
        array.append(array4[random.randint(0,len(array4[1]))])
    

    elif leet_dict[user_id][1] >= 100:
        array5 = marketplace[100]
        array.append(array5[random.randint(0,len(array5[0]))])
    
    await ctx.send(f"You recieved item: {array[0]}")

@bot.command(name='leetcode')
async def leetcode(ctx):
    # Fetch a random LeetCode problem using LeetCode API or a web scraping library
    leetcode_problem = get_random_leetcode_problem()

    # Send the problem to the Discord channel
    await ctx.send(f"**LeetCode Problem:**\n\n{leetcode_problem}")

@bot.command(name='profile')
async def profile(ctx):

    arr = leet_dict[user_id] 

    

    await ctx.send(f"Tier: {arr[2]}")

    await ctx.send(f"XP: {arr[1]} ")



def get_random_leetcode_problem():
    # Implement logic to fetch a random LeetCode problem
    # You can use the LeetCode API or scrape the LeetCode website
    # Make sure to format the problem nicely

    # Example using LeetCode API (replace with your own logic):
    response = requests.get('https://leetcode.com/api/problems/algorithms/')
    problem_data = response.json()
    random_problem = problem_data['stat_status_pairs'][0]['stat']['question__title']

    return random_problem

@bot.command(name='solve')
async def solve(ctx, solution):
    # Validate the solution (replace with your own validation logic)
    is_solution_correct = validate_solution(solution)

    # Provide feedback to the user
    if is_solution_correct:
        await ctx.send("Congratulations! Your solution is correct.")
    else:
        await ctx.send("Oops! Your solution is incorrect. Try again!")

def validate_solution(solution):
    # Implement logic to validate the user's solution
    # You may compare it with the correct answer or use other methods
    # Return True if the solution is correct, False otherwise

    # Example (replace with your own validation logic):
    correct_answer = "42"
    return solution == correct_answer


@bot.command(name='LevelUp')
async def LevelUp(ctx):
    array = leet_dict[user_id]
    problemTracker = ProblemTracker(array[0]) 
    
    level = array[2] + 1

    if array[2]== problemTracker.calculate_user_tier():
        await ctx.send("Step into the JavaScript Junction, where each line of code is a melody and every function is a dance.\n\n Explore the vibrant crossroads of web development, where promises and callbacks pave the way for your JavaScript adventure!")
        await ctx.send(file=discord.File(image_path2))



    array[1] = problemTracker.calculate_user_score()
    array[2] = problemTracker.calculate_user_tier()



    newDic = problemTracker.returnDic()
    
    
    problemArray = newDic[level]
    problem_links = ""
    for i in problemArray:
        problem_name=i
        problem_link = f"https://leetcode.com/problems/{problem_name.lower().replace(' ', "-")}/description"
        problem_links += f"[{problem_name}]({problem_link})\n"
    await ctx.send(f"{problem_links}")

@bot.command(name='getProblem')
async def getProblem(ctx, nameProblem):
    await ctx.send(file=discord.File(image_path3))
    await ctx.send("WOAH what’s happening? \n\n *....teleporting to new dungeon…* …")
    problem_links = ""
    problem_name=nameProblem
    problem_link = f"https://leetcode.com/problems/{problem_name.lower().replace(' ', "-")}/description"
    problem_links += f"[{problem_name}]({problem_link})\n"
    await ctx.send(f"{problem_links}")

@bot.command(name='suggest')
async def suggest(ctx):
    array = leet_dict[user_id]
    problemTracker = ProblemTracker(array[0])
    for i in range(5):
        difficulty = problemTracker.returndifficulty()
        suggestion = problemTracker.suggest_problems(i,difficulty)
    await ctx.send(f"{suggestion}")


     



bot.run('MTIxMTE4MzExNDEwMjExNjM2Mg.GgE12q.dXFNcQUpA1Qb5LH0QvMGutS9G248-cK5nsHHlY')
