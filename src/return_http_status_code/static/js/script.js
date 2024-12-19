function toggleLanguage () {
    const contentMatrix = {
        ja: document.getElementById("contentJapanese"),
        en: document.getElementById("contentEnglish")
    };
    const languageRadioButtons = document.querySelectorAll('input[name="languageRadioBtn"]');

    // 言語切り替え
    const switchLanguage = (language) => {
        Object.keys(contentMatrix).forEach((lang) => {
            contentMatrix[lang].classList.toggle("d-none", lang !== language);
        });
    };

    // 各ラジオボタンに言語切り替え処理を登録
    languageRadioButtons.forEach((button) => {
        button.addEventListener("change", () => {
            const selectedLangage = document.querySelector('input[name="languageRadioBtn"]:checked').value;
            switchLanguage(selectedLangage);
        });
    });

    // デフォルトの選択に基づいて初期化
    const defauleLanguage = document.querySelector('input[name="languageRadioBtn"]:checked').value;
    switchLanguage(defauleLanguage);
}

toggleLanguage();
