async function fetchBook(){
    try {
        const id = localStorage.getItem('myData');
        const response = await fetch(`https://backend.cloudpub.ru/books/${id}`);
        const data = await response.json();
        console.log(data)
        displayData(data);
    } catch (error) {
        console.error("Ошибка при получении данных", error)
    }
}

function displayData(book) {
    const book_title = document.getElementById('book');



   
    book.forEach(book => {
    book_title.textContent = `Название: ${book.book_name}, Автор: ${book.author}, Жанр: ${book.genre}`;
    var iframe = document.getElementById('book_text');
    iframe.src =  `${book.text}`;
});
}

fetchBook()