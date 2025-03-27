const addbook = document.getElementById('myForm');
if (addbook) {
  addbook.addEventListener('submit', async function(event) {
    event.preventDefault(); // предотвращаем стандартное поведение формы

    // Собираем данные из формы
    const formData = new FormData(this);
    const data = {
        username: formData.get('username'),
        password: formData.get('password'),
        email: formData.get('email'),
    };


    try {
        // Отправляем данные на сервер
        const response = await fetch('https://backend.cloudpub.ru/reg/', {
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
        if (jsonResponse){
            sessionStorage.setItem('isLoggedIn', 'true');
            sessionStorage.setItem('userid',Number(jsonResponse) );
        }
        window.location.href = 'getbooks.html';
    } catch (error) {
        console.error('Ошибка при отправке данных:', error);
        alert('Произошла ошибка. Попробуйте снова.');
    }
});}