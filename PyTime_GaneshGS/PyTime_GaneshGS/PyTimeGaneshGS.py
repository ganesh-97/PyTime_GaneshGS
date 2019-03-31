class PyTime:
    
    def printTime(self,input):
        time_in_string = str(input)
        if time_in_string == "0" or time_in_string == "00" or time_in_string == "000" or time_in_string == "0000":
            hours = 0
            minutes = 0
            converted_time = self.calculateTime(hours,minutes)
        else:
            time_in_int = int(time_in_string)
            if time_in_int < 1441:
                hours = int(time_in_int/60)
                minutes = time_in_int%60
                converted_time = self.calculateTime(hours,minutes)
            else:
                converted_time = "Invalid Time Format"
        return converted_time

    def calculateTime(self,hours,minutes):
        if minutes < 10:
            minutes = "0" + str(minutes)
        if hours >= 1 and hours < 12:
            converted_time =  str(hours) + ":" + str(minutes)
        elif hours >= 12 and hours < 24:
            converted_time =  str(hours) + ":" + str(minutes)
        elif hours == 0 or hours == 24:
            hours  = 12
            converted_time = str(hours) + ":" + str(minutes) + " AM"
        return converted_time 
