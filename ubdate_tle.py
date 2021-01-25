from requests import get
def update_tle():
    file = open("tle.txt", "ab")
    file.write(get("http://www.celestrak.com/NORAD/elements/weather.txt").content)                      # 
    print("get tle successfull")
    file.close()

update_tle()