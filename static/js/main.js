function splitText() {
    var data = document.getElementById('mail-naver');
    var splitted = data.replace("MSI","");
    data.innerHTML = splitted;
}