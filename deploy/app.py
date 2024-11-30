from flask import Flask, render_template, request

app = Flask(__name__)

# Data edukasi untuk chatbot
responses = {
    "hello": "Hai! Selamat datang di EduHIV. Apa yang bisa saya bantu hari ini?",
    "hiv": "HIV adalah virus yang menyerang sistem kekebalan tubuh. Apakah Anda ingin tahu tentang gejala, pencegahan, atau pengobatan?",
    "gejala": "Gejala awal HIV seringkali seperti flu: demam, sakit kepala, nyeri otot. Namun, banyak orang tidak menunjukkan gejala selama bertahun-tahun.",
    "pencegahan": "Pencegahan HIV meliputi penggunaan kondom, tidak berbagi jarum suntik, dan menggunakan PrEP (Pre-Exposure Prophylaxis).",
    "pengobatan": "HIV tidak bisa disembuhkan, tetapi dapat dikelola dengan ART (Antiretroviral Therapy) untuk hidup sehat.",
    "terima kasih": "Sama-sama! Jangan ragu untuk bertanya jika ada hal lain yang ingin Anda ketahui.",
    "default": "Maaf, saya tidak mengerti. Bisa dijelaskan lebih detail?"
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get_response", methods=["POST"])
def get_response():
    user_input = request.form["user_input"].lower()
    response = responses.get(user_input, responses["default"])
    return {"response": response}

if __name__ == "__main__":
    app.run(debug=True)
