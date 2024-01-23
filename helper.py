import calculation



def Low_Sensitivity(json_data):
    low_sensitivity = calculation.LowSensitivitySettings()
    tracker_low= calculation.RollingAverageTracker(low_sensitivity)
    tvoc_checker = calculation.TvocThresholdChecker(low_sensitivity)
    
    tracker_low.reset_data()
    for data_point in json_data:
        time = data_point["_time"]
        pm_2_5 = data_point["pm_2_5"]
        
        tracker_low.add_data_point(time, pm_2_5)
        tracker_low.check_threshold("PM Increase Threshold", low_sensitivity.pm_increase_threshold)
        
    tracker_low.reset_data()
    for data_point in json_data:
        time = data_point["_time"]
        tvoc = data_point["tvoc"]
        
        tracker_low.add_data_point(time, tvoc)
        tracker_low.check_threshold("TVOC Increase Threshold", low_sensitivity.tvoc_increase_threshold)
    
    tracker_low.reset_data()
    for data_point in json_data:
        time = data_point["_time"]
        ethanol = data_point["ethanol"]
        
        tracker_low.add_data_point(time, ethanol)
        tracker_low.check_threshold("Ethanol Increase Threshold", low_sensitivity.ethanol_increase_threshold)
        
    tvoc_checker.reset_data()
    for data_point in json_data:
        time = data_point["_time"]
        tvoc = data_point["tvoc"]
        
        tvoc_checker.add_data_point(time, tvoc)
        tvoc_checker.check_threshold("TVOC Threshold", low_sensitivity.tvoc_threshold)

def Medium_Sensitivity(json_data):
        medium_sensitivity = calculation.MediumSensitivitySettings()
        tracker_medium = calculation.RollingAverageTracker(medium_sensitivity)
        tvoc_checker = calculation.TvocThresholdChecker(medium_sensitivity)
        
        tracker_medium.reset_data()
        for data_point in json_data:
            time = data_point["_time"]
            pm_2_5 = data_point["pm_2_5"]
            
            tracker_medium.add_data_point(time, pm_2_5)
            tracker_medium.check_threshold("PM Increase Threshold", medium_sensitivity.pm_increase_threshold)
            
        tracker_medium.reset_data()
        for data_point in json_data:
            time = data_point["_time"]
            tvoc = data_point["tvoc"]
            
            tracker_medium.add_data_point(time, tvoc)
            tracker_medium.check_threshold("TVOC Increase Threshold", medium_sensitivity.tvoc_increase_threshold)

        tracker_medium.reset_data()
        for data_point in json_data:
            time = data_point["_time"]
            ethanol = data_point["ethanol"]
            
            tracker_medium.add_data_point(time, ethanol)
            tracker_medium.check_threshold("Ethanol Increase Threshold", medium_sensitivity.ethanol_increase_threshold)

        tvoc_checker.reset_data()
        for data_point in json_data:
            time = data_point["_time"]
            tvoc = data_point["tvoc"]
            
            tvoc_checker.add_data_point(time, tvoc)
            tvoc_checker.check_threshold("TVOC Threshold", medium_sensitivity.tvoc_threshold)

def High_Sensitivity(json_data):
    high_sensitivity = calculation.HighSensitivitySettings()
    tracker_high = calculation.RollingAverageTracker(high_sensitivity)
    tvoc_checker = calculation.TvocThresholdChecker(high_sensitivity)
    
    tracker_high.reset_data()
    for data_point in json_data:
        time = data_point["_time"]
        pm_2_5 = data_point["pm_2_5"]
        
        tracker_high.add_data_point(time, pm_2_5)
        tracker_high.check_threshold("PM Increase Threshold", high_sensitivity.pm_increase_threshold)
        
    tracker_high.reset_data()
    for data_point in json_data:
        time = data_point["_time"]
        tvoc = data_point["tvoc"]
        
        tracker_high.add_data_point(time, tvoc)
        tracker_high.check_threshold("TVOC Increase Threshold", high_sensitivity.tvoc_increase_threshold)

    tracker_high.reset_data()
    for data_point in json_data:
        time = data_point["_time"]
        ethanol = data_point["ethanol"]
        
        tracker_high.add_data_point(time, ethanol)
        tracker_high.check_threshold("Ethanol Increase Threshold", high_sensitivity.ethanol_increase_threshold)

    tvoc_checker.reset_data()
    for data_point in json_data:
        time = data_point["_time"]
        tvoc = data_point["tvoc"]
        
        tvoc_checker.add_data_point(time, tvoc)
        tvoc_checker.check_threshold("TVOC Threshold", high_sensitivity.tvoc_threshold)

def Custom_Senstivity(json_data):
    ethanol_threshold = int(input("Ethanol Threshold: "))
    pm_threshold = int(input("PM Increase Threshold: "))
    tvoc_increase_threshold = int(input("TVOC Increase Threshold: "))
    tvoc_threshold = int(input("TVOC Max Threshold: "))
    tvoc_wait_time = int(input("TVOC Wait Thyme: "))
    
    custom_sensitivity = calculation.CustomSensitivitySettings(ethanol_threshold, pm_threshold, tvoc_increase_threshold, tvoc_threshold, tvoc_wait_time)
    tracker_custom = calculation.RollingAverageTracker(custom_sensitivity)
    tvoc_checker = calculation.TvocThresholdChecker(custom_sensitivity)
    
    print(custom_sensitivity.PrintCuston())

    tracker_custom.reset_data()
    for data_point in json_data:
        time = data_point["_time"]
        pm_2_5 = data_point["pm_2_5"]
        
        tracker_custom.add_data_point(time, pm_2_5)
        tracker_custom.check_threshold("PM Increase Threshold", custom_sensitivity.pm_increase_threshold)
        
    tracker_custom.reset_data()
    for data_point in json_data:
        time = data_point["_time"]
        tvoc = data_point["tvoc"]
        
        tracker_custom.add_data_point(time, tvoc)
        tracker_custom.check_threshold("TVOC Increase Threshold", custom_sensitivity.tvoc_increase_threshold)

    tracker_custom.reset_data()
    for data_point in json_data:
        time = data_point["_time"]
        ethanol = data_point["ethanol"]
        
        tracker_custom.add_data_point(time, ethanol)
        tracker_custom.check_threshold("Ethanol Increase Threshold", custom_sensitivity.ethanol_increase_threshold)

    tvoc_checker.reset_data()
    for data_point in json_data:
        time = data_point["_time"]
        tvoc = data_point["tvoc"]
        
        tvoc_checker.add_data_point(time, tvoc)
        tvoc_checker.check_threshold("TVOC Threshold", custom_sensitivity.tvoc_threshold)