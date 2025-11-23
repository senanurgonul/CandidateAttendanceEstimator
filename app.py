from flask import Flask, render_template, request
import pandas as pd
from datetime import datetime, timedelta
from sklearn.ensemble import RandomForestRegressor

app = Flask(__name__)

#--------------------

df = pd.read_csv("DataKabin.csv", sep=";")
df["Mülakat Planlanma Tarihi"] = pd.to_datetime(df["Mülakat Planlanma Tarihi"], dayfirst=True)
df["Gelmeyen Sayısı"] = df["Toplam Gelmesi Planlanan Kişi Sayısı"] - df["Planlandığı Gün Gelen Kişi Sayısı"]
df["Yıl"] = df["Mülakat Planlanma Tarihi"].dt.year
df["Ay"] = df["Mülakat Planlanma Tarihi"].dt.month
df["Gün"] = df["Mülakat Planlanma Tarihi"].dt.day


features = ["Yıl", "Ay", "Gün", "Toplam Gelmesi Planlanan Kişi Sayısı"]
target = "Gelmeyen Sayısı"

X = df[features]
y = df[target]

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X, y)


def tarih_araligini_getir(baslangic, bitis):
    start = datetime.strptime(baslangic, "%Y-%m-%d")
    end = datetime.strptime(bitis, "%Y-%m-%d")
    return [start + timedelta(days=i) for i in range((end - start).days + 1)]


def tahmin_yap(tarih, planlanan):
    yil, ay, gun = tarih.year, tarih.month, tarih.day
    veri = pd.DataFrame([[yil, ay, gun, planlanan]], columns=features)
    tahmin = model.predict(veri)[0]
    return round(tahmin)


@app.route("/", methods=["GET", "POST"])
def index():
    detaylar = []
    sonuc = None
    tarih_listesi = []

    if request.method == "POST":
        if "tarih1" in request.form and "tarih2" in request.form and "submit" not in request.form:
            tarih1 = request.form["tarih1"]
            tarih2 = request.form["tarih2"]
            tarih_listesi = tarih_araligini_getir(tarih1, tarih2)
            return render_template("index.html", tarih_listesi=tarih_listesi)

        elif "submit" in request.form:
            i = 0
            toplam = 0
            while True:
                tarih_key = f"tarih_{i}"
                plan_key = f"planlanan_{i}"
                if tarih_key not in request.form:
                    break

                tarih_str = request.form[tarih_key]
                planlanan_str = request.form[plan_key]

                if not planlanan_str.strip().isdigit():
                    planlanan = 0
                else:
                    planlanan = int(planlanan_str)

                tarih = datetime.strptime(tarih_str, "%Y-%m-%d")
                tahmini_gelmeyecek = tahmin_yap(tarih, planlanan)

                detaylar.append({
                    "tarih": tarih.strftime("%d.%m.%Y"),
                    "planlanan": planlanan,
                    "gelmeyecek": tahmini_gelmeyecek
                })
                toplam += tahmini_gelmeyecek
                i += 1

            sonuc = f"Tahmini toplam gelmeyecek kişi sayısı: {toplam}"

    return render_template("index.html", sonuc=sonuc, detaylar=detaylar)


if __name__ == "__main__":
    app.run(debug=True)

#-------------------------------------------------------------
#-------------------------------------------------------------
#-------------------------------------------------------------
#-------------------------------------------------------------
