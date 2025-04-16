# Weather predict
API from **OpenWeatherAPI**

---

1. Go to *https://openweathermap.org/city/2643743*
2. Get API KEY
3. Create `.env` file and pass to that `API_KEY=YOUR_API_KEY`
4. 
a) Windows
``` Windows
python -m venv env | ./env/Scripts/activate | pip install -r req.txt
```
b) Linux
``` Windows
python3 -m venv env | source ./env/bin/activate | pip install -r req.txt
```
5. python main.py `your_city`