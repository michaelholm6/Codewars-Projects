from math import floor

def format_duration(seconds):
    
    if (seconds == 0):
       return "now"
    input = seconds
    hours = -1
    minutes = -1
    days = -1
    years = -1
    comma_counter = 0
    seconds_suffix = " seconds" if seconds > 1 else " second"
    output = str(int(seconds)) + seconds_suffix
    if (seconds >= 60):
        comma_counter = 0
        minutes = floor(seconds/60)
        seconds -= minutes*60
        minutes_suffix = " minutes" if minutes > 1 else " minute"
        output = str(int(minutes)) + minutes_suffix
        if (not seconds == 0):
            output += " and " + str(int(seconds)) + " seconds"
    if (minutes >= 60):
        comma_counter = 0
        hours = floor(minutes/60)
        minutes -= hours*60
        hours_suffix = " hours" if hours > 1 else " hour"
        minutes_suffix = " minutes" if minutes > 1 else " minute"
        seconds_suffix = " seconds" if seconds > 1 else " second"
        output = str(int(hours)) + hours_suffix
        if (not minutes == 0):
            output += " and " + str(int(minutes)) + minutes_suffix
        if (not seconds == 0):
            output += " and " + str(int(seconds)) + seconds_suffix
            comma_counter += 1
    if (hours >= 24):
        comma_counter = -1
        days = floor(hours/24)
        hours -= days*24
        days_suffix = " days" if days > 1 else " day"
        hours_suffix = " hours" if hours > 1 else " hour"
        minutes_suffix = " minutes" if minutes > 1 else " minute"
        seconds_suffix = " seconds" if seconds > 1 else " second"
        output = str(int(days)) + days_suffix
        if (not hours == 0):
            output += " and " + str(int(hours)) + hours_suffix
            comma_counter += 1
        if (not minutes == 0):
            output += " and " + str(int(minutes)) + minutes_suffix
            comma_counter += 1
        if (not seconds == 0):
            output += " and " + str(int(seconds)) + seconds_suffix
            comma_counter += 1
    if (days >= 365):
        comma_counter = 0
        years = floor(days / 365)
        days -= years*365
        years_suffix = " years" if years > 1 else " year"
        days_suffix = " days" if days > 1 else " day"
        hours_suffix = " hours" if hours > 1 else " hour"
        minutes_suffix = " minutes" if minutes > 1 else " minute"
        seconds_suffix = " seconds" if seconds > 1 else " second"
        output = str(int(years)) + years_suffix
        if (not days == 0):
            output += " and " + str(int(days)) + days_suffix
        if (not hours == 0):
            output += " and " + str(int(hours)) + hours_suffix
            comma_counter += 1
        if (not minutes == 0):
            output += " and " + str(int(minutes)) + minutes_suffix
            comma_counter += 1
        if (not seconds == 0):
            output += " and " + str(int(seconds)) + seconds_suffix
            comma_counter += 1
    output = output.replace( " and ", ", ", comma_counter)
    return output

print(format_duration(54645364334))

