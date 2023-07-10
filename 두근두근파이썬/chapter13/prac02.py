class TV:
    def __init__(self):
        self.channel = 1
        self.volume = 1
        self.on = 0

    def turnOn(self):
        self.on = 1
    def turnOff(self):
        self.on = 0
    def setChannel(self,channel):
        self.channel = channel
    def setVolume(self,volume):
        self.volume = volume
    def __str__(self):
        msg = f"TV의 채널: {self.channel}\nTV의 음량: {self.volume}"
        return msg

tv = TV()
tv.turnOn()
tv.setChannel(11)
tv.setVolume(100)
print(tv)
