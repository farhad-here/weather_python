# =====================================
from tkinter import *
from requests import *
# =====================================
address = "http://dataservice.accuweather.com"
api_key = "YOUR_APIKEY"
address_w = "http://dataservice.accuweather.com"
# =====================================
window = Tk()
window.title("ACCU WEATHER")
# =====================================
d1_1 = Label(window)
n1_1 = Label(window)
d2_2 = Label(window)
n2_2 = Label(window)
d3_3 = Label(window)
n3_3 = Label(window)
d4_4 = Label(window)
n4_4 = Label(window)
d5_5 = Label(window)
n5_5 = Label(window)
fasle_2 = Label(window)
fasle_3 = Label(window)
fasle_4 = Label(window)
fasle_5 = Label(window)
# =====================================
def cle():
    print(d1_1.config(text=""))
    print(n1_1.config(text=""))
    print(fasle_2.config(text=""))
    print(d2_2.config(text=""))
    print(n2_2.config(text=""))
    print(fasle_3.config(text=""))
    print(d3_3.config(text=""))
    print(n3_3.config(text=""))
    print(fasle_4.config(text=""))
    print(d4_4.config(text=""))
    print(n4_4.config(text=""))
    print(fasle_5.config(text=""))
    print(d5_5.config(text=""))
    print(n5_5.config(text=""))
    
#=======================================
def ex():
    print(window.destroy())

#=======================================
def send():
    city_name = et_et.get()
    url = f"{address}/locations/v1/cities/search?apikey={api_key}&q={city_name}"
    rq = get(url)
    data = rq.json()
    key = data[0]["Key"]
    url_w = f"{address_w}/forecasts/v1/daily/5day/{key}?apikey={api_key}"
    rq_w = get(url_w)
    data_w = rq_w.json()
# ===============================================================
    d1 = data_w["DailyForecasts"][0]["Day"]["IconPhrase"]
    n1 = data_w["DailyForecasts"][0]["Night"]["IconPhrase"]
    d2 = data_w["DailyForecasts"][1]["Day"]["IconPhrase"]
    n2 = data_w["DailyForecasts"][1]["Night"]["IconPhrase"]
    d3 = data_w["DailyForecasts"][2]["Day"]["IconPhrase"]
    n3 = data_w["DailyForecasts"][2]["Night"]["IconPhrase"]
    d4 = data_w["DailyForecasts"][3]["Day"]["IconPhrase"]
    n4 = data_w["DailyForecasts"][3]["Night"]["IconPhrase"]
    d5 = data_w["DailyForecasts"][4]["Day"]["IconPhrase"]
    n5 = data_w["DailyForecasts"][4]["Night"]["IconPhrase"]
# ===============================================================
    d1_1.config(text=f"Day(1) {d1}")
    n1_1.config(text=f"Night(1) {n1}")
    d2_2.config(text=f"Day(2) {d2}")
    n2_2.config(text=f"Night(2) {n2}")
    d3_3.config(text=f"Day(3) {d3}")
    n3_3.config(text=f"Night(3) {n3}")
    d4_4.config(text=f"Day(4) {d4}")
    n4_4.config(text=f"Night(4) {n4}")
    d5_5.config(text=f"Day(5) {d5}")
    n5_5.config(text=f"Night(5) {n5}")
    fasle_2.config(text = "--------------------------")
    fasle_3.config(text = "--------------------------")
    fasle_4.config(text = "--------------------------")
    fasle_5.config(text = "--------------------------")
    d1_1.pack()
    n1_1.pack()
    fasle_2.pack()
    d2_2.pack()
    n2_2.pack()
    fasle_3.pack()
    d3_3.pack()
    n3_3.pack()
    fasle_4.pack()
    d4_4.pack()
    n4_4.pack()
    fasle_5.pack()
    d5_5.pack()
    n5_5.pack()


# ================================================================
filter = Label(window, text="#its filter for using its better to use urban vpn#", fg="green")
filter.pack()
et = Label(window, text="enter the cities name")
et.pack()
et_et = Entry(bg = "cyan")
et_et.pack()
b_r = Button(window, text="Recived",fg="green",bg = "lightblue", command=send)
b_r.pack()
b_c = Button(window,text="clear",bg="skyblue",fg= "white",command=cle)
b_c.pack()
b_e = Button(window,text="exit",fg="red",command=ex)
b_e.pack()


window.resizable(height=False, width=False)
window.geometry("500x500")
window.mainloop()
