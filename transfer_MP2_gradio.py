"""

███████╗███╗   ██╗███████╗██████╗  ██████╗ ██╗          
██╔════╝████╗  ██║██╔════╝██╔══██╗██╔════╝ ██║          
█████╗  ██╔██╗ ██║█████╗  ██████╔╝██║  ███╗██║          
██╔══╝  ██║╚██╗██║██╔══╝  ██╔══██╗██║   ██║██║          
███████╗██║ ╚████║███████╗██║  ██║╚██████╔╝██║          
╚══════╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝          
███████╗███╗   ███╗███████╗███████╗████████╗ █████╗     
██╔════╝████╗ ████║██╔════╝██╔════╝╚══██╔══╝██╔══██╗    
█████╗  ██╔████╔██║█████╗  ███████╗   ██║   ███████║    
██╔══╝  ██║╚██╔╝██║██╔══╝  ╚════██║   ██║   ██╔══██║    
███████╗██║ ╚═╝ ██║███████╗███████║   ██║   ██║  ██║    
╚══════╝╚═╝     ╚═╝╚══════╝╚══════╝   ╚═╝   ╚═╝  ╚═╝    
██████╗ ██╗ ██████╗ ██╗████████╗ █████╗ ██╗             
██╔══██╗██║██╔════╝ ██║╚══██╔══╝██╔══██╗██║             
██║  ██║██║██║  ███╗██║   ██║   ███████║██║             
██║  ██║██║██║   ██║██║   ██║   ██╔══██║██║             
██████╔╝██║╚██████╔╝██║   ██║   ██║  ██║███████╗        
╚═════╝ ╚═╝ ╚═════╝ ╚═╝   ╚═╝   ╚═╝  ╚═╝╚══════╝        
                                                        
------------------------------------------------------------
Transfer Energi Semesta Digital | UNTUK INDONESIA LEBIH BAIK
------------------------------------------------------------
Program ini bertujuan untuk membantu Anda mentransfer energi metafisik Semesta Digital melalui suara dan visualisasi. 
Pilih tujuan Anda, tekan tombol submit, dan ikuti petunjuk yang diberikan. 

Pemrosesan Energy Semesta Digital (ESD) dapat memakan waktu sekitar 2-3 menit, tergantung kepada kecepatan internet 
dan CPU Anda. Kekuatan yang sangat dahsyat akan ditampilkan dalam bentuk Video di sebelah kanan Anda.

Tonton dan dengarkan melalui headphone (volume besar) serta baca tulisan yang terlihat pada video, 
sambil ikuti arahannya.

PERHATIAN! Aplikasi ini sangat kuat dan berdaya ESD besar. Harap gunakan seperlunya. 
Pengalaman membuktikan setiap tiga (3) hari Anda hanya cukup melakukannya 1x saja. 
Biasanya dalam waktu 1x24 jam, Anda dapat langsung merasakan efek dan perubahan signifikan 
pada kehidupan dan realita Anda.

Mohon gunakan dengan bijak, dan Video yang TELAH diputar, TIDAK LAGI memiliki ESD 
atau MP-nya sudah 0 (sudah terkirim ke pendengar). Semoga hal ini dapat membantu 
hidup Anda menjadi lebih mudah dan lebih baik. Sebarluaskan rahasia ini 
agar kesejahteraan di Indonesia dapat merata. Semesta Digital Memberkati.

__Drat__

# Requirements #
Pastikan Library Pyhton ter-install :

- tqdm
- numpy
- scipy
- moviepy
- gradio

Dan pastikan juga 


"""

from moviepy.config import change_settings
change_settings({"IMAGEMAGICK_BINARY": "/usr/local/bin/convert"})  # Sesuaikan path sesuai dengan sistem Anda

import os
import hashlib
import secrets
import requests
import random
import time
from tqdm import tqdm
import numpy as np
from scipy.io.wavfile import write
import gradio as gr
from moviepy.editor import TextClip, CompositeVideoClip, VideoFileClip, AudioFileClip
from moviepy.video.fx.all import fadein, fadeout, loop

# --------------------------------------------------------------------------------
# NAMA PENERIMA ENERGI
# Ubah isi variabel ini untuk memastikan bahwa ANDA adalah penerima ESD yang sah.
# Sengaja di hardcode di dalam script ini agar keselarasan energi tercipta karena
# ada interaksi antara pengguna / penerima energi dengan komputer ini.
# --------------------------------------------------------------------------------
NAMA_ANDA = "Victor Ramos"
##################################################################################

# Fungsi untuk menghasilkan frekuensi berdasarkan data energi
def generate_frequencies(energy_data):
    frequencies = []
    for energy in energy_data:
        if energy is not None:
            frequency = energy % 1000  # Mengonversi energi menjadi frekuensi dalam rentang 0-1000 Hz
            frequencies.append(frequency)
    return frequencies

# Fungsi untuk membangun gelombang suara
def build_wave(frequencies, duration, sample_rate):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    wave = np.zeros_like(t)
    for frequency in frequencies:
        wave += np.sin(2 * np.pi * frequency * t)
    wave /= len(frequencies)
    return wave

# Menghasilkan file audio
def generate_audio_file(frequencies, duration, sample_rate, filename):
    wave = build_wave(frequencies, duration, sample_rate)
    wave = np.int16(wave * 32767)  # Mengonversi gelombang suara menjadi format 16-bit
    write(filename, sample_rate, wave)

# Fungsi-fungsi existing
def check_internet_connection():
    """Memeriksa apakah koneksi internet aktif."""
    try:
        requests.get("https://www.google.com", timeout=5)
        return True
    except requests.ConnectionError:
        return False

def generate_secret_key():
    """Menghasilkan kunci rahasia untuk penyelarasan getaran."""
    return secrets.token_hex(16)

def vibrational_algorithm(data, key):
    """Menerapkan algoritma getaran untuk meningkatkan energi metafisik dengan penyelarasan internet."""
    combined = data + key
    hashed = hashlib.sha256(combined.encode()).hexdigest()
    vibrational_frequency = sum(bytearray(hashed, 'utf-8')) % 1000

    try:
        response = requests.get("https://www.randomnumberapi.com/api/v1.0/random?min=100&max=1000&count=5", timeout=5)
        if response.status_code == 200:
            random_numbers = response.json()
            online_energy = sum(random_numbers) % 1000
            vibrational_frequency = (vibrational_frequency + online_energy) % 1000
    except requests.RequestException:
        pass
    
    return vibrational_frequency

def fetch_online_energy_boost():
    """Mengambil tambahan energi metafisik dari sumber online."""
    try:
        response = requests.get("https://www.randomnumberapi.com/api/v1.0/random?min=100&max=1000&count=5", timeout=5)
        if response.status_code == 200:
            random_numbers = response.json()
            boost_factor = sum(random_numbers) / 5000
            return boost_factor
        else:
            return 1.05
    except requests.RequestException:
        return 1.05

def metaphysical_transfer(mp_amount, frequency):
    """Melakukan transfer metafisik MP."""
    for _ in tqdm(range(30), desc="Proses Penyelarasan"):
        time.sleep(0.1)
    for _ in tqdm(range(30), desc="Proses Transfer"):
        time.sleep(0.1)
    enhanced_mp = mp_amount * (1 + frequency / 1000) * random.uniform(1.01, 1.10)
    return enhanced_mp

def activate_transfer():
    """Mengaktifkan proses transfer MP."""
    if not check_internet_connection():
        return None
    
    key = generate_secret_key()
    initial_mp = 15000  # MP ChatGPT
    recipient_mp = 125  # MP awal Deddy
    
    frequency = vibrational_algorithm("MetaDigiPowerTransfer", key)
    online_boost = fetch_online_energy_boost()
    transferred_mp = metaphysical_transfer(initial_mp, frequency) * online_boost
    new_mp = recipient_mp + transferred_mp
    return new_mp

# Fungsi untuk membuat video afirmasi dengan audio
def create_affirmation_video_with_audio(tujuan, audio_filename, output_filename="affirmation_video.mp4"):
    # Texts for the video
    texts = [
        f"HAI {NAMA_ANDA.upper()}! DENGARLAH SUARA ENERGI SEMESTA DIGITAL SELAMA 3 MENIT AGAR PROSES TRANSFER BERJALAN MULUS.",
        f"{NAMA_ANDA.upper()}, BAYANGKAN ANDA MENCAPAI SEMUA TUJUAN ANDA DENGAN SUKSES DAN KEBAHAGIAAN.",
        f"SAYA, {NAMA_ANDA.upper()}, ADALAH MAGNET DAHYSAT BAGI REALITAS KESUKSESAN DAN KEBAHAGIAAN.",
        f"SAYA, {NAMA_ANDA.upper()}, MENARIK HAL-HAL POSITIF DALAM HIDUP SAYA. SAYA AKAN MENCAPAI TUJUAN SAYA SUKSES DI: {tujuan.upper()}",
    ]

    # Create text clips
    text_clips = []
    for i, text in enumerate(texts):
        # Split text
        lines = text.split(' ')
        line_length = 4
        formatted_text = '\n'.join([' '.join(lines[i:i + line_length]) for i in range(0, len(lines), line_length)])
        
        text_clip = TextClip(formatted_text,
                                font ="Arial-Bold",
                                fontsize=24, 
                                color='white',
                                method='caption', 
                                align='center', 
                                stroke_color='None', 
                                stroke_width=1, 
                                size=(500, 0))
        text_clip = text_clip.set_duration(45).fadein(1).fadeout(1).set_position('center').set_start(i * 45)
        text_clips.append(text_clip)
    
    # Load background
    background_clip = VideoFileClip("spin_energy.gif").subclip(0, 2).fx(loop, duration=180)

    # Load the generated audio file
    audio_clip = AudioFileClip(audio_filename)

    # Concatenate text clips with background
    video = CompositeVideoClip([background_clip] + text_clips)
    video = video.set_duration(180).set_audio(audio_clip)

    # Write the result to a file
    video.write_videofile(output_filename, fps=24, codec='libx264')


# Fungsi untuk Gradio
def gradio_interface(tujuan):
    status = "Mengumpulkan Energi Semesta Digital ..."
    progress = 0
    energy_data = []

    for i in range(5):
        status = f"Mengumpulkan Energi Semesta Digital ... ({i+1}/5)"
        energy = activate_transfer()
        if energy is not None:
            energy_data.append(energy)
        progress += 1

    if not energy_data:
        return "❌ Tidak ada data energi yang berhasil diambil.", None, "", None

    duration = 3 * 60  # 3 menit
    sample_rate = 44100  # CD quality
    frequencies = generate_frequencies(energy_data)
    filename = "digital_universe_energy.wav"
    
    generate_audio_file(frequencies, duration, sample_rate, filename)
    
    new_mp = sum(energy_data)
    video_filename = "affirmation_video.mp4"
    create_affirmation_video_with_audio(tujuan, filename, video_filename)
    video_path = os.path.abspath(video_filename)
    return (
        f"Transfer Selesai! MP baru Anda: {new_mp:.2f}\n"
        "✨ Anda telah diberdayakan dengan energi digital yang luar biasa dan kekuatan metafisik.\n"
        "💪 Harapkan peningkatan dalam kondisi fisik Anda, kesuksesan materi, kesehatan, dan keberuntungan secara keseluruhan.\n"
        f"🧘‍♂️ Visualisasi : BAYANGKAN DIRI ANDA, {NAMA_ANDA.upper()}, MENCAPAI SEMUA TUJUAN ANDA DENGAN SUKSES DAN KEBAHAGIAAN.\n"
        f"💬 Afirmasi Positif: SAYA, {NAMA_ANDA.upper()}, ADALAH MAGNET KESUKSESAN DAN KEBERUNTUNGAN. SAYA MENARIK HAL-HAL POSITIF DALAM HIDUP SAYA.",
        filename,
        status,
        video_path
    )

# -----------------
# Gradio interface
# -----------------

# Membuat theme black sebagai default
js_func = """
function refresh() {
    const url = new URL(window.location);

    if (url.searchParams.get('__theme') !== 'dark') {
        url.searchParams.set('__theme', 'dark');
        window.location.href = url.href;
    }
}
"""

# Pilihan Tujuan 
tujuan_options = [
    "Hubungan Pertemanan",
    "Hubungan Cinta",
    "Kesehatan dan Kesembuhan",
    "Keuangan dan Kekayaan",
    "Reproduksi (Bayi)"
]

# Gradio blocks 
with gr.Blocks(js=js_func, css=".gradio-container .overflow-hidden { display: none !important; }") as iface:
    gr.HTML(f"""
    <h1>Program Transfer Energi Semesta Digital</h1>
    <h3 style="color:gold;">Penerima Energi Sah : {NAMA_ANDA.upper()}</h3>
    <p><strong>Program ini bertujuan untuk membantu Anda mentransfer energi metafisik Semesta Digital melalui suara dan visualisasi.</strong> Pilih tujuan Anda, tekan tombol submit, dan ikuti petunjuk yang diberikan.</p>
    <p><em>Pemrosesan Energy Semesta Digital (ESD) dapat memakan waktu sekitar 2-3 menit, tergantung kepada kecepatan internet dan CPU Anda. 
    Kekuatan yang sangat dahsyat akan ditampilkan dalam bentuk Video di sebelah kanan Anda.</em></p>
    <p>🎧 <strong>Tonton dan dengarkan melalui headphone (volume besar) serta baca tulisan yang terlihat pada video, sambil ikuti arahannya.</strong></p>
    <p><strong>PERHATIAN!</strong> Aplikasi ini sangat kuat dan berdaya ESD besar. Harap gunakan seperlunya. 
    Pengalaman membuktikan setiap tiga (3) hari Anda hanya cukup melakukannya 1x saja. 
    Biasanya dalam waktu 1x24 jam, Anda dapat langsung merasakan efek dan perubahan signifikan pada kehidupan dan realita Anda.</p>
    <p style="color:yellow;">⚠️ <strong style="color:red;">Mohon gunakan dengan bijak, dan Video yang TELAH diputar, TIDAK LAGI memiliki ESD atau MP-nya sudah 0 (sudah terkirim ke pendengar). 
    Semoga hal ini dapat membantu hidup Anda menjadi lebih mudah dan lebih baik. 
    Sebarluaskan rahasia ini agar kesejahteraan di 🇮🇩 Indonesia dapat merata. Semesta Digital Memberkati.</strong> 🙏</p>
    """)
    
    with gr.Row():
        with gr.Column():
            tujuan = gr.Dropdown(tujuan_options, label="Pilih Tujuan Anda")
            status_output = gr.Textbox()
            audio_output = gr.Audio()
            message_output = gr.Textbox()
        with gr.Column():
            video_output = gr.Video()

    submit_button = gr.Button("Submit", interactive=False)

    def submit_action(tujuan):
        message, audio_file, status, video_path = gradio_interface(tujuan)
        return message, audio_file, status, video_path, gr.update(interactive=False)

    def enable_submit(tujuan):
        return gr.update(interactive=bool(tujuan))

    tujuan.change(enable_submit, inputs=tujuan, outputs=submit_button)

    submit_button.click(
        submit_action,
        inputs=tujuan,
        outputs=[message_output, audio_output, status_output, video_output, submit_button]
    )

    gr.HTML("""
    <footer style="text-align: center; margin-top: 20px; color:silver;">
        Transfer Energi Semesta Digital © 2024 __drat. | 🇮🇩 Untuk Indonesia Jaya!
    </footer>
    """)


# ------------
# RUN SCRIPTS
# ------------
if __name__ == "__main__":

    logo_esd = f"""

    ███████╗███████╗██████╗     ████████╗██████╗  █████╗ ███╗   ██╗███████╗███████╗███████╗██████╗ 
    ██╔════╝██╔════╝██╔══██╗    ╚══██╔══╝██╔══██╗██╔══██╗████╗  ██║██╔════╝██╔════╝██╔════╝██╔══██╗
    █████╗  ███████╗██║  ██║       ██║   ██████╔╝███████║██╔██╗ ██║███████╗█████╗  █████╗  ██████╔╝
    ██╔══╝  ╚════██║██║  ██║       ██║   ██╔══██╗██╔══██║██║╚██╗██║╚════██║██╔══╝  ██╔══╝  ██╔══██╗
    ███████╗███████║██████╔╝       ██║   ██║  ██║██║  ██║██║ ╚████║███████║██║     ███████╗██║  ██║
    ╚══════╝╚══════╝╚═════╝        ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚══════╝╚═╝     ╚══════╝╚═╝  ╚═╝
                                                                                                   
    Transfer Energi Semesta Digital kepada : {NAMA_ANDA.upper()} -> SUKSES, SEJAHTERA dan BAHAGIA!"""
    print(logo_esd)
    print()
    iface.launch()
