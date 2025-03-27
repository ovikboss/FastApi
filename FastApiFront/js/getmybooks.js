async function fetchBook(){
    try {
        const user_id = sessionStorage.getItem("userid")
        console.log(`https://friskily-on-okapi.cloudpub.ru/user/${Number(user_id)}`)
        const response = await fetch(`https://backend.cloudpub.ru/user/${Number(user_id)}`);
        const data = await response.json();
        console.log(data)
        displayData(data);
    } catch (error) {
        console.error("Ошибка при получении данных", error)
    }
}
function displayData(books) {
    const booksList = document.getElementById('user-list');
    booksList.innerHTML = '';

    books.forEach(book => {
        const unsubcribebutton = document.createElement("button")
        unsubcribebutton.textContent = "Убрать";
        unsubcribebutton.className = "btn btn-primary btn-lg float-end"  
        unsubcribebutton.id = `unsubscribe-item-${book.id}`;
        const divitem = document.createElement("div")
        const listItem = document.createElement('li');
        const buttonItem = document.createElement("button");
        divitem.className = "card"
        buttonItem.textContent = "Открыть";
        buttonItem.className = "btn btn-primary btn-lg float-end"  
        buttonItem.id = `fetch-item-${book.id}`;

        listItem.textContent = `Название: ${book.book_name}, Автор: ${book.author}, Жанр: ${book.genre}`;

        unsubcribebutton.addEventListener('click', () => {
            unsubscribe(book.id);
        });

        buttonItem.addEventListener('click', () => {
            sendData(book.id);
        });
        divitem.appendChild(listItem)
        listItem.appendChild(unsubcribebutton)
        listItem.appendChild(buttonItem);
        booksList.appendChild(divitem);
    });
}
function unsubscribe(book_id){
    try {
    const user_id = sessionStorage.getItem("userid")

    const response =  fetch(`http://127.0.0.1:8000/unsubscribe/${book_id}/${user_id}`);
    }catch(error){
        console.error('Ошибка при получении данных:', error);
    }
}



function sendData(id) {
    // Сохранение данных в Local Storage
    localStorage.setItem('myData', id);
    // Переход на второй файл
    window.location.href = 'getbook.html';
}

fetchBook()