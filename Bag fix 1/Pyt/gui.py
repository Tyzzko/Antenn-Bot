from simpletk import TApplication, TButton, TGroupBox, TComboBox, TImage, TLabel
from Satelite.manipulator_control import ThreadStart, update_tle, AutoUpdate_tle, ThreadTestStart, ChooseSAT
from Satelite.config import Version, Sats, direct


width  = 1920 // 2
height = 1080 // 2

app = TApplication('ControlPanel ver {}   -  Choi is alive'.format(Version))                # переделать, скорее всего сменить фреймворк на QT
app.size = width, height
app.resizable = False, False
app.background = "#f1f1f1"

butonColor = "#bfbfbf"
buttonTextColor = "#000000"
StartTracking = TButton(app, text = "Start tracking")
StartTracking.size = 120, 30
StartTracking.position = 20, 40
StartTracking.background = butonColor
StartTracking.color = buttonTextColor


UpdateTle = TButton(app, text = "Force get tle update", )
UpdateTle.size = 120, 30
UpdateTle.position = 20, 80 
UpdateTle.background = butonColor
UpdateTle.color = buttonTextColor

test = TButton(app, text = "Admin mode")
test.size = 120, 30
test.position = 20, 120
test.background = butonColor
test.color = buttonTextColor

SatList = TComboBox(app, values = Sats)
SatList.size = 120, 30
SatList.position = 20, height // 2.7 + 20 + 10
SatList.background = "#3F3F3F"
SatList.color = "#C3C3C3"
SatList.text = Sats[0]
SatList.onChange = ChooseSAT

test.onClick = ThreadTestStart

logo = TImage(app)
logo.picture = direct + "logo.jpeg"    # не пашет
logo.align = "center"
logo.position = 540, 20
logo.size = 212, 300


AutoUpdate_tle()
StartTracking.onClick = ThreadStart
UpdateTle.onClick = update_tle

st = TLabel(app)                        # не доделано
st.position = 0, 510
st.size = 120, 30
st.text = "Started"


app.run()