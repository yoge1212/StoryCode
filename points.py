from tierscore import ProblemTracker
import datetime
from webscraper import Webscraper


#problemtracker = ProblemTracker()
#newArray = problemtracker.getArray()
#points = problemtracker.calculate_user_score()

class pointSystem: 

    def sendReminder(self,userName):
        problemtracker = ProblemTracker(userName)
        newArray = problemtracker.getArray()
        self.points = problemtracker.calculate_user_score()
        timeStamp = float(newArray[0].returnTime())  # or int(newArray[0].returnTime()) if it's an integer string
        dt_object = datetime.datetime.fromtimestamp(timeStamp)
        currentTime = datetime.datetime.now()
        time_difference = currentTime - dt_object
        days_difference = time_difference.days
        reminder = "It's been over 24 hours. Why not practice some LeetCode?"
        if days_difference >= 1:
          return reminder

    #After a day call this method
    count = 0
    def pointsOnTime(self,points, count):
         timeStamp = float(self.newArray[0].returnTime())
         dt_object = datetime.datetime.fromtimestamp(timeStamp)
         currentTime = datetime.datetime.now()
         time_difference = currentTime - dt_object
         days_difference = time_difference.days
         if days_difference <= 1:
              count = count + 1
              if count == 3:
                 count = 0
                 points = points + 1
         return points


 









