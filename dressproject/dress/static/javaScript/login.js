document.addEventListener('DOMContentLoaded', function() {
    // ログインボタンとポップアップ要素を取得
    const openLoginBtn = document.getElementById("openLoginBtn");  // IDを一致させる
    const loginPopup = document.getElementById("popup");  // ポップアップIDを一致させる
    const closePopupBtn = document.getElementById("closePopupBtn");
    

    // ログインボタンがクリックされたときにポップアップを表示
    if (openLoginBtn) {
        openLoginBtn.addEventListener("click", () => {
            loginPopup.style.display = "flex"; // ポップアップ表示
        });
    }

    // 閉じるボタンがクリックされたときにポップアップを非表示
    if (closePopupBtn) {
        closePopupBtn.addEventListener("click", () => {
            loginPopup.style.display = "none"; // ポップアップ非表示
        });
    }

    // ポップアップ外をクリックしたときに閉じる
    window.addEventListener("click", (event) => {
        if (event.target === loginPopup) {
            loginPopup.style.display = "none"; // ポップアップ外をクリックした場合も閉じる
        }
    });
});

// ポップアップを閉じる関数
function closePopup() {
    const loginPopup = document.getElementById("popup");
    loginPopup.style.display = "none"; // ポップアップ非表示
}
