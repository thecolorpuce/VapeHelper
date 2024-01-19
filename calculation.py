"""

This is where we will math this shit out.

We will have constant formulas for low, medium, and high sensitivities

Planning on adding custom parameters after these are done
"""

"""
LOW
Ethanol Increase Threshold:10
PM Increase Threshold:20
TVOC Increase Threshold:20
TVOC Threshold:490
TVOC Wait Time:45

"""

"""
Medium
Ethanol Increase Threshold:10
PM Increase Threshold:12
TVOC Increase Threshold:20
TVOC Threshold:490
TVOC Wait Time:20

"""

"""
High
Ethanol Increase Threshold:10
PM Increase Threshold:5
TVOC Increase Threshold:20
TVOC Threshold:490
TVOC Wait Time:1

"""

class SensitivitySettings:
    def __init__(self, ethanol_threshold, pm_threshold,tvoc_increase_threshold, tvoc_threshold, tvoc_wait_time):
        self.ethanol_increase_threshold = ethanol_threshold
        self.pm_increase_threshold = pm_threshold
        self.tvoc_increase_threshold = tvoc_increase_threshold
        self.tvoc_threshold = tvoc_threshold
        self.tvoc_wait_time = tvoc_wait_time

class LowSensitivitySettings(SensitivitySettings):
    def __init__(self):
        super().__init__(10, 20, 20, 490, 45)

class MediumSensitivitySettings(SensitivitySettings):
    def __init__(self):
        super().__init__(10, 12, 20, 490, 20)

class HighSensitivitySettings(SensitivitySettings):
    def __init__(self):
        super().__init__(10, 5, 20, 490, 1)

class CustomSensitivitySettings(SensitivitySettings):
    def __init__(self, ethanol_threshold, pm_threshold,tvoc_increase_threshold, tvoc_threshold, tvoc_wait_time):
        super().__init__(ethanol_threshold, pm_threshold,tvoc_increase_threshold, tvoc_threshold, tvoc_wait_time)
    
    def PrintCuston(self):
        print(f"{self.ethanol_increase_threshold}: {self.pm_increase_threshold}: {self.tvoc_increase_threshold}: {self.tvoc_threshold}: {self.tvoc_wait_time}")


class RollingAverageTracker:
    def __init__(self, sensitivity_settings):
        self.sensitivity_settings = sensitivity_settings
        self.data = []
        
    def add_data_point(self, time, value):
        self.data.append((time, value))
        self.data = self.data[-4:] # Retain the last 3 data points
        
    def calculate_rolling_average(self):
        if len(self.data) < 4:
            return None # Not enough data to calculate
        total = sum(data_point[1] for data_point in self.data[:-1])
        rolling_average = total / 3
        
        return rolling_average
    
    
    def check_threshold(self, parameter_name, threshold):
        rolling_average = self.calculate_rolling_average()
        
        if rolling_average is not None and rolling_average < self.data[-1][1] and abs(rolling_average - self.data[-1][1]) > threshold:
            difference = abs(self.data[-1][1]) - abs(rolling_average) 
            print(f"{parameter_name}:Rolling Average:{rolling_average}.Value:{self.data[-1][1]} Threshold:{threshold} exceeded at {self.data[-1][0]} Difference = {abs(difference)}")
    
    def reset_data(self):
        self.data = []

class TvocThresholdChecker:
    def __init__(self, sensitivity_settings):
        self.sensitivity_settings = sensitivity_settings
        self.data = []
        
    def add_data_point(self, time, value):
        self.data.append((time, value))
        self.data = self.data[-1:]
    
    def check_threshold(self, parameter_name, threshold):
        tvoc_value = self.data[-1][1]
        if tvoc_value >= threshold:
            difference = tvoc_value - threshold
            print(f"{parameter_name}: is greater than {threshold} by {difference} at time {self.data[-1][0]}")
    
    def reset_data(self):
        self.data = []