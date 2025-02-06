const addbook = document.getElementById('myForm');
if (addbook) {
  addbook.addEventListener('submit', async function(event) {
    event.preventDefault(); // предотвращаем стандартное поведение формы

    // Собираем данные из формы
    const formData = new FormData(this);
    const data = {
        title: formData.get('title'),
        author: formData.get('author'),
        genre: formData.get('genre'),
    };


    try {
        // Отправляем данные на сервер
        const response = await fetch('http://127.0.0.1:8000/addbook/', {
            method: 'POST',
            headers: {
                'Cache-Control': 'no-cache',
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data),
        });

        // Проверяем статус ответа
        if (!response.ok) {
            throw new Error(`Ошибка: ${response.status}`);
        }

        const jsonResponse = await response.json();
        console.log('Успех:', jsonResponse);
        alert('Успех:', jsonResponse);
    } catch (error) {
        console.error('Ошибка при отправке данных:', error);
        alert('Произошла ошибка. Попробуйте снова.');
    }
});}


