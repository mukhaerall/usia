from flask import Flask, render_template, request, url_for
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('home.html')  # Pastikan ini sesuai dengan nama file Anda

@app.route('/usia', methods=['GET', 'POST'])
def cek_usia():
    if request.method == 'POST':
        # Ambil data dari form
        tahun_lahir = int(request.form['tahun_lahir'])
        tahun_sekarang = datetime.now().year
        usia = tahun_sekarang - tahun_lahir
        return render_template('cek_usia.html', usia=usia, tahun_lahir=tahun_lahir)
    return render_template('cek_usia.html', usia=None)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=2000)