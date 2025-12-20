from PIL import Image
import os

def gerar_icones():
    # Verifica se a imagem original existe
    if not os.path.exists("logo_original.png"):
        print("❌ Erro: Salve a imagem da logo como 'logo_original.png' primeiro!")
        return

    try:
        # Abre a imagem original
        img = Image.open("logo_original.png")
        
        # Converte para RGB (garante que não haja problemas de transparência/formato)
        img = img.convert("RGB")

        # 1. Gerar Icone 512x512 (Alta resolução para Play Store)
        # Usamos LANCZOS para garantir a melhor qualidade no redimensionamento
        icon_512 = img.resize((512, 512), Image.Resampling.LANCZOS)
        icon_512.save("icon-512.png")
        print("✅ icon-512.png gerado com sucesso!")

        # 2. Gerar Icone 192x192 (Para tela inicial do Android)
        icon_192 = icon_512.resize((192, 192), Image.Resampling.LANCZOS)
        icon_192.save("icon-192.png")
        print("✅ icon-192.png gerado com sucesso!")

    except Exception as e:
        print(f"❌ Ocorreu um erro: {e}")

if __name__ == "__main__":
    gerar_icones()