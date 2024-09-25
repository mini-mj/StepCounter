import os
import pandas as pd

data_file_path = os.path.join('data', 'July__August__and_September_Steps_and_Calories_Dataset.csv')
data = pd.read_csv(data_file_path)

data.head()

class StepCounter:
    def __init__(self, data):
        """
        Initialize the StepCounter with the given dataset.
        """
        self.data = data
        self.data['Date'] = pd.to_datetime(self.data['Date'])  # Ensure the Date column is in datetime format
    
    def total_weekly_steps(self):
        """
        Calculate the total number of steps taken in the past 7 days.
        """
        last_seven_days = self.data[self.data['Date'] >= (pd.Timestamp.now() - pd.Timedelta(days=7))]
        total_steps = last_seven_days['Steps'].sum()
        return total_steps
    
    def average_daily_steps(self):
        """
        Calculate the average daily steps.
        """
        avg_steps = self.data['Steps'].mean()
        return avg_steps
    
    def activity_feedback(self):
        """
        Provide feedback on the user's activity level based on average daily steps.
        """
        avg_steps = self.average_daily_steps()
        if avg_steps < 5000:
            return "Low activity level"
        elif 5000 <= avg_steps <= 10000:
            return "Moderate activity level"
        else:
            return "High activity level"

step_counter = StepCounter(data)

# Calculate the total weekly steps, average daily steps, and get feedback on activity level
total_weekly_steps = step_counter.total_weekly_steps()
average_daily_steps = step_counter.average_daily_steps()
activity_feedback = step_counter.activity_feedback()

print(f"Total Weekly Steps: {total_weekly_steps}")
print(f"Average Daily Steps: {average_daily_steps}")
print(f"Activity Feedback: {activity_feedback}")