# Ozan Yetkin | 1908227


class Clock:
    def __init__(self, h=0, m=0):
        'The constructor'
        try:
            h = int(h)
            m = int(m)
        except ValueError as e:
            raise ValueError("Error: Hours and minutes should be integers or strings containing integers!")
        
        if h < 0 or h > 23:
            raise ValueError("Hour must be between 0 and 23")
        if m < 0 or m > 59:
            raise ValueError("Minute must be between 0 and 59")
        self._hour = h
        self._minute = m
        
    def __str__(self):
        'convert the time into a printable format (e.g. 23:10)'
        return "%02d:%02d" % (self._hour,self._minute)
    
    def __repr__(self):
        'Same as __str__'
        return str(self)
    
    def tick(self):
        'Add one minute to the current time'
        self._minute += 1
        if self._minute == 60:
            self._minute = 0
            self._hour = (self._hour + 1) % 24
            
    def __eq__(self, other):
        'check whether the current time is equal to the time on the other Clock'
        if isinstance(other, Clock):
            return self._hour == other._hour and self._minute == other._minute
        else:
            return False
