import subprocess
def abrir_programa(caminho):
    try:
        subprocess.Popen([caminho])
        print(f"{caminho} aberto com sucesso!")
    except FileNotFoundError:
        print(f"{caminho} não encontrado. Verifique o caminho do executável.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

def abrir_spotify_e_opera():
    caminho_spotify = r"C:\Users\SeuUser\AppData\Roaming\Spotify\Spotify.exe"
    caminho_opera = r"C:\Users\SeuUser\AppData\Local\Programs\Opera GX\opera.exe"
    
    abrir_programa(caminho_spotify)

    abrir_programa(caminho_opera)

if __name__ == "__main__":
    abrir_spotify_e_opera()
