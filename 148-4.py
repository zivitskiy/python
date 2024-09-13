professions: dict[str, list[str]] = {
    "людина-техніка": ["логічне мислення", "точність", "технічні знання", "уважність"],
    "людина-лідер": ["комунікабельність", "емпатія", "вміння слухати", "переконливість"],
    "людина-природа": ["спостережливість", "уважність", "любов до природи", "терплячість"]
}

def chquality(profession, quality) -> str:
    if profession in professions:
        if quality in professions[profession]:
            return f"Так, якість '{quality}' важлива для напряму '{profession}'."
        else:
            return f"Ні, якість '{quality}' не є важливою для напряму '{profession}'."
    else:
        return f"Напрям '{profession}' не знайдено в базі."

def main() -> None:
    print("Доступні професійні напрямки:")
    for prof in professions:
        print(f"- {prof}")

    chosen: str = input("\nОберіть напрямок: ").strip().lower()
    quality: str = input("Введіть якість для перевірки: ").strip().lower()

    result: str = chquality(chosen, quality)
    print(result)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
