import math
class Solution:
    def intToRoman(self, num: int) -> str:
        Roman = []
        thous = floor(num/1000)
        hundr = floor((num-(thous*1000))/100)
        decimal = floor((num-(thous*1000)-(hundr*100))/10)
        units = (((num-(thous*1000)-(hundr*100)-(decimal*10))))
        Roman.append("M"*thous)
        # Hundrets
        if hundr > 4 and hundr != 4 and hundr != 9:
            Roman.append("D")
            Roman.append("C"*(hundr-5))
        if hundr < 4 and hundr != 4 and hundr != 9:
            Roman.append("C"*hundr)
        if hundr == 4:
            Roman.append("CD")
        if hundr == 9:
            Roman.append("CM")
        # Decimals
        if decimal > 4 and decimal != 4 and decimal != 9:
            Roman.append("L")
            Roman.append("X"*(decimal-5))
        if decimal < 4 and decimal != 4 and decimal != 9:
            Roman.append("X"*decimal)
        if decimal == 4:
            Roman.append("XL")
        if decimal == 9:
            Roman.append("XC")
        # Units
        if units > 4 and units != 4 and units != 9:
            Roman.append("V")
            Roman.append("I"*(units-5))
        if units < 4 and units != 4 and units != 9:
            Roman.append("I"*units)
        if units == 4:
            Roman.append("IV")
        if units == 9:
            Roman.append("IX")
        return ''.join(Roman)
              
