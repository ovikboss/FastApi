// Функция для получения данных
async function fetchBooks() {
    try {
        const response = await fetch(`http://127.0.0.1:8000/books`); // Пример API
        const data = await response.json();

        displayData(data);
    } catch (error) {
        console.error('Ошибка при получении данных:', error);
    }
}

// Функция для отображения данных на странице
function displayData(books) {
    const user_log = sessionStorage.getItem("isLoggedIn")


    const booksList = document.getElementById('user-list');
    booksList.innerHTML = '';

    books.forEach(book => {

        const subcribebutton = document.createElement("button")
        subcribebutton.textContent = "В избранное";
        subcribebutton.className = "btn btn-primary btn-lg float-end"  
        subcribebutton.id = `subscribe-item-${book.id}`;
        subcribebutton.disabled = "True"
        const divitem = document.createElement("div")
        const listItem = document.createElement('li');
        const buttonItem = document.createElement("button");
        divitem.className = "card"
        buttonItem.textContent = "Открыть";
        buttonItem.className = "btn btn-primary btn-lg float-end"  
        buttonItem.id = `fetch-item-${book.id}`;
        listItem.textContent = `Название: ${book.book_name}, Автор: ${book.author}, Жанр: ${book.genre}`;
        if (user_log){
                    subcribebutton.disabled = false
        }
        subcribebutton.addEventListener('click', () => {
            subscribe(book.id);
        });


        buttonItem.addEventListener('click', () => {
            sendData(book.id);
        });
        divitem.appendChild(listItem)
        listItem.appendChild(subcribebutton)
        listItem.appendChild(buttonItem);
        booksList.appendChild(divitem);
    });
}

function sendData(id) {
    // Сохранение данных в Local Storage
    localStorage.setItem('myData', id);
    // Переход на второй файл
    window.location.href = 'getbook.html';
}


function subscribe(book_id){
    try {
    const user_id = sessionStorage.getItem("userid")

    const response =  fetch(`http://127.0.0.1:8000/subscribe/${book_id}/${user_id}`);
    }catch(error){
        console.error('Ошибка при получении данных:', error);
    }
}


// Вызов функции для получения и отображения данных
fetchBooks();
