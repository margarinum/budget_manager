function getCategories() {

    let curr = document.location.href;
    let xhr = new XMLHttpRequest();
    xhr.open('GET', 'http://127.0.0.1:5002/getCategories');
    xhr.send();
    if (xhr.status !== 200) {
        // обработать ошибку
        alert(xhr.status + ': ' + xhr.statusText); // пример вывода: 404: Not Found
    } else {
        // вывести результат
        alert(xhr.responseText); // responseText -- текст ответа.
    }

}