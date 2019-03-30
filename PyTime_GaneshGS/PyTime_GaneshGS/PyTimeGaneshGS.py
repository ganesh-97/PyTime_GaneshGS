class PyTime:
    
    def printTime(self,input):
        time_in_string = str(input)
        length = len(time_in_string)
        if length == 3:
            hour,minute1,minute2 = time_in_string
            hours = "0" + hour
            minutes = minute1 + minute2
            converted_time = self.calculateTime(hours,minutes)
        elif length == 4:
            hour1,hour2,minute1,minute2 =  time_in_string
            hours = hour1 + hour2
            minutes = minute1 + minute2
            converted_time = self.calculateTime(hours,minutes)
        elif time_in_string=="000" or time_in_string=="0000":
            hour1,hour2,minute1,minute2 =  time_in_string
            hours = hour1 + hour2
            minutes = minute1 + minute2
            converted_time = self.calculateTime(hours,minutes)
        else:
            converted_time = "Invalid Format"
        return converted_time

    def calculateTime(self,hours,minutes):
        hours_in_int = int(hours)
        minutes_in_int = int(minutes)
        if hours_in_int >= 1 and hours_in_int < 12:
            converted_time =  hours + ":" + minutes + " AM"
        elif hours_in_int >= 12 and hours_in_int < 24:
            converted_time =  hours + ":" + minutes + " PM"
        elif hours == "00":
            hours  = "12"
            converted_time = hours + ":" + minutes + " AM"
        elif hours_in_int >= 24:
            converted_time = "Invalid Format"
        return converted_time 
