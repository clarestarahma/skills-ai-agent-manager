def clean_for_display(text):
    if not text: return ""
    # Pecah berdasarkan enter, buang spasi, buang yang kosong, gabung pakai koma
    items = [i.strip() for i in text.split('\n') if i.strip()]
    return ", ".join(items)